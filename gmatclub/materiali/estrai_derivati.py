#!/usr/bin/env python3
"""Ricava da ogni materiale di questa cartella una versione leggibile e cercabile.

I file originali sono di terzi e stanno qui come sono stati scaricati. Alcuni pero'
si leggono male: due sono .doc di Word 97 che LibreOffice rifiuta di aprire, uno e'
un PDF il cui livello di testo perde i trattini, un altro ha le formule solo come
immagini remote. Questo script apre gli originali e ne scrive accanto un derivato in
Markdown o in CSV, per poterci cercare dentro, citarli e collegarli al resto del repo.

Quello che lo script NON fa e' correggere la fonte. Vale la regola del CONVENZIONI.md
del repo, paragrafo 5: se l'originale sbaglia, il derivato sbaglia uguale. Le uniche
cose che cambiano sono di resa - le formule diventano LaTeX, il corsivo diventa
Markdown - e sono elencate una per una in README.md.

Uso:  python3 gmatclub/materiali/estrai_derivati.py
Serve pypdf, pypdfium2 e olefile.  Riscrive tutti i .md e .csv di questa cartella.

Due lettori di PDF e non uno perche' nessuno dei due basta da solo: pypdf espone la
matrice di testo, e senza quella il corsivo delle domande di CR si perderebbe;
pypdfium2 impagina meglio, e sul PDF delle soluzioni e' l'unico che non spezzi le
parole a meta' ("t he argument").
"""

import csv
import os
import re
import struct
import urllib.parse

import olefile
import pypdfium2
from pypdf import PdfReader

QUI = os.path.dirname(os.path.abspath(__file__))

# I .doc del 2005-2010 sono binari di Word 97. Il testo non e' un blocco unico: sta
# in pezzi elencati nella piece table, ognuno con la sua codifica.
FIB_FLAGS = 0x0A            # dove sta la parola di flag
FIB_CLX = 0x01A2            # dove stanno posizione e lunghezza della piece table
PEZZO_COMPRESSO = 0x40000000  # bit che dice: 8 bit cp1252, non 16 bit UTF-16

# Word delimita i campi (INCLUDEPICTURE, HYPERLINK, PAGEREF) con tre caratteri di
# controllo: inizio, separatore fra istruzione e risultato, fine.
CAMPO_INIZIO, CAMPO_SEP, CAMPO_FINE = "\x13", "\x14", "\x15"

# Le formule delle spiegazioni di Bunuel sono immagini servite da un CGI che rende
# LaTeX. L'indirizzo contiene il LaTeX: le formule si recuperano senza scaricare nulla.
MIMETEX = re.compile(r'INCLUDEPICTURE\s+"[^"]*mimetex\.cgi\?([^"]*)"[^\x14]*')
HYPERLINK = re.compile(r'HYPERLINK\s+"([^"]*)"[^\x14]*')


# ---------------------------------------------------------------- lettura dei .doc

def testo_word97(percorso):
    """Il testo di un .doc di Word 97, con i marcatori di campo lasciati dentro.

    I marcatori servono dopo, per distinguere una formula da una parola qualsiasi.
    """
    with olefile.OleFileIO(percorso) as ole:
        doc = ole.openstream("WordDocument").read()
        flag = struct.unpack("<H", doc[FIB_FLAGS:FIB_FLAGS + 2])[0]
        tabella = ole.openstream("1Table" if flag & 0x0200 else "0Table").read()

    inizio, lunghezza = struct.unpack("<II", doc[FIB_CLX:FIB_CLX + 8])
    clx = tabella[inizio:inizio + lunghezza]

    # La Clx e' una sequenza di blocchi: 0x01 sono proprieta' da saltare, 0x02 e' la
    # piece table vera e propria.
    piece, i = None, 0
    while i < len(clx):
        if clx[i] == 1:
            i += 3 + struct.unpack("<H", clx[i + 1:i + 3])[0]
        elif clx[i] == 2:
            n = struct.unpack("<I", clx[i + 1:i + 5])[0]
            piece = clx[i + 5:i + 5 + n]
            break
        else:
            break
    if piece is None:
        raise ValueError(f"{percorso}: piece table non trovata")

    # La piece table e' fatta di due array: n+1 posizioni di carattere, poi n descrittori
    # da 8 byte. Il descrittore dice dove sta il pezzo e con quale codifica.
    n = (len(piece) - 4) // 12
    posizioni = struct.unpack(f"<{n + 1}I", piece[:4 * (n + 1)])
    descrittori = piece[4 * (n + 1):]

    pezzi = []
    for k in range(n):
        fc = struct.unpack("<I", descrittori[k * 8 + 2:k * 8 + 6])[0]
        quanti = posizioni[k + 1] - posizioni[k]
        if fc & PEZZO_COMPRESSO:
            da = (fc & ~PEZZO_COMPRESSO) // 2
            pezzi.append(doc[da:da + quanti].decode("cp1252", "replace"))
        else:
            pezzi.append(doc[fc:fc + quanti * 2].decode("utf-16-le", "replace"))

    testo = "".join(pezzi)
    return testo.replace("\r", "\n").replace("\x07", "\t").replace("\x0b", "\n")


def scioglie_campi(testo):
    """Sostituisce i campi di Word con il loro contenuto utile.

    Una formula diventa $LaTeX$, un collegamento diventa il suo indirizzo, tutto il
    resto del campo sparisce. I dollari gia' presenti nel testo si proteggono prima,
    altrimenti GitHub li scambia per delimitatori di formula.
    """
    testo = testo.replace("$", r"\$")
    testo = testo.replace("\xa0", " ").replace("\x01", "")

    def formula(m):
        # unquote e non unquote_plus: nei LaTeX il segno + e' un piu', non uno spazio.
        latex = urllib.parse.unquote(m.group(1)).strip()
        return f"${latex}$" if latex else ""

    fuori = []
    for pezzo in testo.split(CAMPO_INIZIO):
        if CAMPO_SEP not in pezzo:
            fuori.append(pezzo)
            continue
        istruzione, _, resto = pezzo.partition(CAMPO_SEP)
        risultato, _, dopo = resto.partition(CAMPO_FINE)
        if MIMETEX.search(istruzione):
            fuori.append(MIMETEX.sub(formula, istruzione).strip() + dopo)
        elif HYPERLINK.search(istruzione):
            fuori.append(risultato.strip() + dopo)
        else:
            fuori.append(risultato + dopo)

    ripulito = "".join(fuori)
    for c in (CAMPO_INIZIO, CAMPO_SEP, CAMPO_FINE):
        ripulito = ripulito.replace(c, "")
    return re.sub(r"[ \t]+\n", "\n", ripulito)


# ---------------------------------------------------------------- lettura dei PDF

def pagine_pdf(percorso):
    """Il testo di un PDF, una stringa per pagina."""
    return [p.extract_text() or "" for p in PdfReader(percorso).pages]


def pagine_pdf_corsivo(percorso, shear=0.3):
    """Come pagine_pdf, ma segna il corsivo con gli asterischi del Markdown.

    Nel PDF delle domande di CR il corsivo non e' un font a se': e' il font tondo
    inclinato dalla matrice di testo. Il terzo coefficiente della matrice vale zero
    sul testo dritto e circa 0,32 su quello inclinato, e questa e' l'unica traccia
    del corsivo che sopravvive all'estrazione.
    """
    apre, chiude = "\x02", "\x03"
    pagine = []
    for pagina in PdfReader(percorso).pages:
        pezzi = []
        pagina.extract_text(
            visitor_text=lambda t, cm, tm, fd, fs: pezzi.append((tm[2] > shear, t))
        )
        fuori, dentro = [], False
        for inclinato, t in pezzi:
            if inclinato != dentro:
                fuori.append(apre if inclinato else chiude)
            dentro = inclinato
            fuori.append(t)
        if dentro:
            fuori.append(chiude)

        # Un corsivo che finisce a fine riga lascia il segno di chiusura all'inizio
        # della riga dopo, cioe' davanti al primo punto elenco. Lo si riporta indietro,
        # altrimenti quella risposta non si riconosce piu' come tale.
        testo = "".join(fuori)
        testo = re.sub(r"(\s+)" + chiude, chiude + r"\1", testo)
        pagine.append(testo.replace(apre, "*").replace(chiude, "*"))
    return pagine


def pagine_pdfium(percorso):
    """Il testo di un PDF letto da PDFium, una stringa per pagina.

    Sul PDF delle soluzioni di CR pypdf inserisce spazi dentro le parole, perche' il
    file del 2008 porta nel flusso di contenuto la spaziatura del testo giustificato.
    PDFium ricostruisce le parole intere.
    """
    documento = pypdfium2.PdfDocument(percorso)
    return [documento[i].get_textpage().get_text_range().replace("\r", "")
            for i in range(len(documento))]


def righe_pulite(testo):
    """Le righe non vuote di un testo, ripulite dagli spazi ai bordi."""
    return [r.strip() for r in testo.split("\n") if r.strip()]


def incipit(testo, quanti=90):
    """Le prime parole di un testo, su una riga sola, per stare in una cella di CSV."""
    piatto = re.sub(r"\s+", " ", testo).strip()
    return piatto[:quanti].rstrip() + ("..." if len(piatto) > quanti else "")


def scrivi(nome, contenuto):
    with open(os.path.join(QUI, nome), "w", encoding="utf-8") as f:
        f.write(contenuto)
    print(f"  scritto {nome} ({len(contenuto):,} caratteri)")


def scrivi_csv(nome, intestazione, righe):
    with open(os.path.join(QUI, nome), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(intestazione)
        w.writerows(righe)
    print(f"  scritto {nome} ({len(righe)} righe)")


# ---------------------------------------------------------------- Data Sufficiency

INTESTAZIONE_DS = re.compile(r"(?m)^(\d{1,3})\.\s+(.+)$")
DISCUSSIONE = re.compile(r"(?m)^Discussed at:\s*(\S+)\s*$")


def domande_ds(testo):
    """Le domande del .doc di Bunuel: numero, argomento, corpo.

    Il numero e l'argomento stanno sulla stessa riga. Dentro le spiegazioni pero'
    ci sono elenchi numerati che hanno la stessa forma, quindi si accetta una
    intestazione solo se il numero cresce rispetto all'ultima accettata.
    """
    trovate, ultimo = [], 0
    for m in INTESTAZIONE_DS.finditer(testo):
        n = int(m.group(1))
        if n <= ultimo or n > ultimo + 12:
            continue
        ultimo = n
        trovate.append((n, m.group(2).strip(), m.start(), m.end()))

    for i, (n, argomento, _, fine) in enumerate(trovate):
        finora = trovate[i + 1][2] if i + 1 < len(trovate) else len(testo)
        yield n, argomento, testo[fine:finora].strip()


def ds_markdown():
    """quant/ds-700-plus-bunuel.md - le domande di DS con spiegazione."""
    origine = os.path.join(QUI, "quant", "ds-700-plus-bunuel.doc")
    testo = scioglie_campi(testo_word97(origine))
    domande = list(domande_ds(testo))

    fuori = [
        "# 700+ Data Sufficiency, con le spiegazioni di Bunuel",
        "",
        "[<- I materiali](../README.md)",
        "",
        "Trascrizione di `quant/ds-700-plus-bunuel.doc`, raccolto e risolto da **Bunuel**",
        "su GMAT Club nel settembre 2010. Il *700+* del titolo e' la fascia di difficolta',",
        f"non il numero di domande: le domande sono **{len(domande)}**, numerate da 1 a 55 con",
        "le 16-19 assenti gia' nella fonte.",
        "",
        "Cambia solo la resa. Le formule, che nel .doc sono immagini servite da un CGI, sono",
        "qui in LaTeX - lo stesso LaTeX che stava scritto nell'indirizzo dell'immagine. Il",
        "testo e' quello di Bunuel, refusi compresi.",
        "",
        "---",
        "",
    ]

    for n, argomento, corpo in domande:
        corpo = DISCUSSIONE.sub(
            lambda m: f"[Discussione su GMAT Club]({m.group(1)})", corpo
        )
        fuori += [f"## {n}. {argomento}", "", corpo, "", "---", ""]

    fuori += ["[<- I materiali](../README.md)", ""]
    scrivi("quant/ds-700-plus-bunuel.md", "\n".join(fuori))
    return domande


# ---------------------------------------------------------------- Critical Reasoning

TOPIC_CR = re.compile(r"Critical Reasoning Topic (\d+):\s*(\w+)")
# Lo spazio dopo il punto a volte manca ("100.Vervet monkeys"), ma dopo il punto non
# ci puo' essere una cifra, altrimenti si scambiano per domande i numeri decimali.
NUMERO_CR = re.compile(r"^(\d{1,3})\.\s*(?=[^\d])(.+)$")
# Le alternative sono puntini elenco quasi ovunque, ma le domande di provenienza LSAT
# raccolte nel topic 8 le marcano A-E oppure (A)-(E). Servono tutte e tre le forme.
OPZIONE_CR = re.compile(r"^(?:\u2022|[A-E]\.|\([A-E]\))\s*(.*)$")


def blocchi_cr(pagine):
    """Le domande del PDF di CR, raggruppate per topic.

    Ogni pagina si apre con il proprio numero su una riga da sola: si scarta. Una
    domanda comincia con "N. ", una opzione di risposta con un punto elenco, e le
    righe che non cominciano ne' con l'uno ne' con l'altro proseguono quella prima.
    """
    topic, domande, corrente, blocco = None, [], None, 1
    fuori = []
    salta = ("The 700-800 Club", "Critical Reasoning")

    def chiudi():
        if corrente:
            domande.append(corrente)

    for numero_pagina, pagina in enumerate(pagine, start=1):
        if "OFFENDING COMMAND" in pagina:
            continue          # l'ultima pagina del PDF e' un errore di stampa, non testo
        righe = righe_pulite(pagina)
        if righe and righe[0].isdigit():   # il numero di pagina, in testa a ogni foglio
            righe = righe[1:]
        for riga in righe:
            if riga in salta:
                continue
            t = TOPIC_CR.search(riga)
            if t:
                chiudi()
                corrente = None
                if topic:
                    fuori.append((topic, domande))
                topic, domande, blocco = (int(t.group(1)), t.group(2)), [], 1
                continue
            if topic is None:
                continue
            m = NUMERO_CR.match(riga)
            if m:
                chiudi()
                n = int(m.group(1))
                # Il topic 8 raccoglie due serie di domande, e la seconda riparte da 1.
                # Il calo del numero e' l'unico segnale che una serie e' finita.
                if corrente and n <= corrente["numero"]:
                    blocco += 1
                corrente = dict(numero=n, blocco=blocco, pagina=numero_pagina,
                                testo=[m.group(2)], opzioni=[])
            elif corrente is None:
                continue
            elif OPZIONE_CR.match(riga):
                corrente["opzioni"].append([OPZIONE_CR.match(riga).group(1)])
            elif corrente["opzioni"]:
                corrente["opzioni"][-1].append(riga)
            else:
                corrente["testo"].append(riga)

    chiudi()
    if topic:
        fuori.append((topic, domande))
    return fuori


def unisci(pezzi):
    """Rimette insieme le righe di un paragrafo spezzato dall'impaginazione."""
    return re.sub(r"\s+", " ", " ".join(pezzi)).strip()


def cr_derivati(risposte=None):
    """verbal/cr-700-800-domande.md e verbal/cr-700-800-indice.csv.

    risposte, se passato, e' la mappa restituita da cr_soluzioni(): la lettera finisce
    nel CSV ma non nel Markdown delle domande, che resta pulito per esercitarsi.
    """
    risposte = risposte or {}
    origine = os.path.join(QUI, "verbal", "cr-700-800-domande.pdf")
    gruppi = blocchi_cr(pagine_pdf_corsivo(origine))
    totale = sum(len(d) for _, d in gruppi)

    fuori = [
        "# Critical Reasoning 700-800 - le domande",
        "",
        "[<- I materiali](../README.md)",
        "",
        f"Trascrizione di `verbal/cr-700-800-domande.pdf`: **{totale} domande** in",
        f"{len(gruppi)} topic, dalla raccolta *The 700-800 Club* del 2008. Il topic 8",
        "numera due volte da capo, e qui le due serie restano separate come nella fonte.",
        "",
        "**Qui le risposte non ci sono, apposta.** Stanno nelle",
        "[soluzioni](cr-700-800-soluzioni.md), che le commentano una per una, e nella",
        "colonna `risposta` di [`cr-700-800-indice.csv`](cr-700-800-indice.csv). Le",
        "alternative non sono marcate A-E nemmeno nell'originale - sono puntini elenco, e",
        "qui restano tali: **la lettera delle soluzioni e' una posizione**, A il primo",
        "puntino, E il quinto.",
        "",
        "Il corsivo della domanda vera e propria, in coda a ogni stimolo, e' quello del",
        "PDF. I dollari sono protetti con la barra rovesciata perche' sono valute, non",
        "formule.",
        "",
        "---",
        "",
    ]

    righe_csv = []
    for (numero, nome), domande in gruppi:
        fuori += [f"## Topic {numero} - {nome.title()}", ""]
        blocco = 1
        for d in domande:
            if d["blocco"] != blocco:
                blocco = d["blocco"]
                fuori += [f"*Qui la numerazione della fonte riparte da capo "
                          f"(serie {blocco} del topic {numero}).*", ""]
            testo = unisci(d["testo"]).replace("$", r"\$")
            opzioni = [unisci(o).replace("$", r"\$") for o in d["opzioni"]]
            fuori += [f"**{d['numero']}.** {testo}", ""]
            fuori += [f"- {o}" for o in opzioni] + [""]
            righe_csv.append([numero, nome.title(), d["blocco"], d["numero"],
                              d["pagina"], len(opzioni),
                              risposte.get((numero, d["blocco"], d["numero"]), ""),
                              incipit(testo)])
        fuori += ["---", ""]

    fuori += ["[<- I materiali](../README.md)", ""]
    scrivi("verbal/cr-700-800-domande.md", "\n".join(fuori))
    scrivi_csv("verbal/cr-700-800-indice.csv",
               ["topic", "topic_nome", "blocco", "domanda", "pagina_pdf", "opzioni",
                "risposta", "incipit"],
               righe_csv)
    return righe_csv


# ------------------------------------------------- soluzioni di Critical Reasoning

# Le sezioni delle soluzioni hanno i nomi dei topic delle domande, con maiuscole
# incoerenti fra loro. L'ordine e' lo stesso, e da li' si ricava il numero del topic.
TOPIC_SOL = re.compile(r"(?m)^\s*(Conclusion|Assumptions|WEAKEN|STRENGTHEN|Evaluate|"
                       r"Paradox|Boldface|Miscellaneous)\s*$")
NUMERO_SOL = re.compile(r"(?m)^\s*(\d{1,3})\.\s*(?=$|[A-Z\u201c\"(])")

# La risposta esatta e' scritta in prosa, e ogni contributore la scrive a modo suo.
# Sono i sei modi che compaiono nel file. Il gruppo catturato e' sempre la lettera.
RISPOSTA_SOL = [
    re.compile(r"\(([A-E])\)\s*CORRECT"),
    re.compile(r"(?m)^([A-E])\.\s*CORRECT"),
    # Senza (?i) sulla lettera: "the correct answer is deceptive" darebbe "d".
    re.compile(r"(?i:correct answer(?: choice)? is\s*)\(?([A-E])\)?(?![A-Za-z])"),
    re.compile(r"(?s)[Aa]nswer choice \(([A-E])\)\s*:?[^.]{0,60}?is the correct answer"),
    re.compile(r"(?s)[Aa]nswer choice \(([A-E])\)\s*:?[^.]{0,40}?\bCORRECT\b"),
    re.compile(r"(?s)[Aa]nswer choice \(([A-E])\)\s*:?[^.]{0,40}?[Tt]his (?:is the )?correct answer"),
    re.compile(r"(?i:\bhence,?\s*)\(?([A-E])\)?\s+is (?:better|correct)"),
]


def blocchi_soluzioni(testo):
    """Le soluzioni, una per (topic, serie, numero), con la lettera della risposta.

    Come nelle domande, il topic 8 numera due volte da capo. Qui pero' la numerazione
    va letta con due cautele in piu': un numero puo' ripetersi a cavallo di un salto
    di pagina, e dentro le spiegazioni ci sono elenchi numerati. Si accetta un numero
    solo se prosegue la serie; se cala, e' una serie nuova solo quando riparte da 1.
    """
    tagli = [(m.group(1), m.start(), m.end()) for m in TOPIC_SOL.finditer(testo)]
    fuori = {}
    for k, (nome, _, fine) in enumerate(tagli):
        finora = tagli[k + 1][1] if k + 1 < len(tagli) else len(testo)
        sezione = testo[fine:finora]
        marcatori, tenuti, ultimo, serie = list(NUMERO_SOL.finditer(sezione)), [], 0, 1
        for j, m in enumerate(marcatori):
            n = int(m.group(1))
            if n > ultimo + 5 or n == ultimo:
                continue
            if n < ultimo:
                if n != 1:
                    continue
                serie += 1
            ultimo = n
            fin = marcatori[j + 1].start() if j + 1 < len(marcatori) else len(sezione)
            tenuti.append((serie, n, sezione[m.end():fin].strip()))
        for serie, n, corpo in tenuti:
            piatto = " ".join(corpo.split())
            lettere = {g.group(1) for p in RISPOSTA_SOL for g in p.finditer(piatto)}
            fuori[(k + 1, serie, n)] = dict(
                lettera=list(lettere)[0] if len(lettere) == 1 else "",
                corpo=corpo)
    return fuori


def cr_soluzioni():
    """verbal/cr-700-800-soluzioni.md, e la mappa (topic, serie, numero) -> risposta."""
    origine = os.path.join(QUI, "verbal", "cr-700-800-soluzioni.pdf")
    soluzioni = blocchi_soluzioni("\n".join(pagine_pdfium(origine)))
    con_lettera = sum(1 for v in soluzioni.values() if v["lettera"])

    fuori = [
        "# Critical Reasoning 700-800 - le soluzioni",
        "",
        "[<- I materiali](../README.md) - [Le domande](cr-700-800-domande.md)",
        "",
        f"Trascrizione di `verbal/cr-700-800-soluzioni.pdf`: **{len(soluzioni)} soluzioni**",
        "commentate alternativa per alternativa, non solo la lettera giusta.",
        "",
        "Le domande sono in [`cr-700-800-domande.md`](cr-700-800-domande.md), e li' le",
        "alternative non hanno lettera: sono puntini elenco. **La lettera qui indica la",
        "posizione**: A e' il primo puntino, E il quinto.",
        "",
        f"La lettera della risposta e' stata riconosciuta in **{con_lettera}** soluzioni su",
        f"{len(soluzioni)}. Nelle altre la fonte non la dichiara in una forma riconoscibile -",
        "la spiegazione c'e' lo stesso e dice qual e', ma a parole.",
        "",
        "---",
        "",
    ]
    for (topic, serie, numero) in sorted(soluzioni):
        v = soluzioni[(topic, serie, numero)]
        etichetta = f"Topic {topic}"
        if topic == 8:
            etichetta += f", serie {serie}"
        titolo = f"## {etichetta} - {numero}"
        if v["lettera"]:
            titolo += f"  \u2192  **{v['lettera']}**"
        fuori += [titolo, "", v["corpo"].replace("$", r"\$"), "", "---", ""]

    fuori += ["[<- I materiali](../README.md)", ""]
    scrivi("verbal/cr-700-800-soluzioni.md", "\n".join(fuori))
    return {k: v["lettera"] for k, v in soluzioni.items()}

# ---------------------------------------------------------------- Quant 700-800

SEZIONE_QUANT = re.compile(
    r"^(GMAT Quant Topic \d+.*|MISCELLANEOUS QUESTIONS|ANSWERS|"
    r"Calculations, Exponents, Basic Algebra)\s*$")
NUMERO_QUANT = re.compile(r"^(\d{1,3})\.\s*(?=[^\d])(.+)$")

# Il nome del topic sta sulla riga sotto l'intestazione, ma non sempre e non in modo
# uniforme: nel topic 1 l'estrazione lo spezza sul capolettera, nel 4 e nel 5 la riga
# sotto e' il nome di una parte, non del topic. Letti a mano dalle pagine 1, 17, 31,
# 46, 60, 64 e 71 del PDF.
NOMI_QUANT = {
    "GMAT Quant Topic 1": "Topic 1 - General Arithmetic",
    "GMAT Quant Topic 2": "Topic 2 - Statistics",
    "GMAT Quant Topic 4 (Numbers)": "Topic 4 - Numbers",
    "GMAT Quant Topic 5: Geometry": "Topic 5 - Geometry",
    "GMAT Quant Topic 6": "Topic 6 - Co-ordinate Geometry",
    "GMAT Quant Topic 7": "Topic 7 - Permutations and Combinations",
    "GMAT Quant Topic 8": "Topic 8 - Probability",
}
STATEMENT_DS = re.compile(r"\(1\).+\(2\)|^\(1\)", re.S)


def quant_csv():
    """quant/quant-700-800-indice.csv - dove sta ogni problema, e di che tipo e'.

    Il PDF non ha un indice e non e' completo: il topic 3 non c'e', le risposte
    coprono un topic solo e l'ultima pagina si interrompe a meta'. Questo CSV serve a
    vedere il buco prima di mettersi a studiare, non a rimediarci.

    Il tipo non e' scritto da nessuna parte e si deduce: se sotto la domanda ci sono
    le due affermazioni numerate (1) e (2), e' Data Sufficiency, altrimenti e' Problem
    Solving. Le due affermazioni sono la forma stessa del DS, quindi il segnale e'
    affidabile - ma resta una deduzione nostra, non un dato della fonte.
    """
    pagine = pagine_pdf(os.path.join(QUI, "quant", "quant-700-800-problems.pdf"))

    righe, risposte = [], {}
    sezione, corrente = "(senza intestazione)", None

    def chiudi():
        if not corrente:
            return
        testo = unisci(corrente["testo"])
        if sezione == "ANSWERS":
            risposte[corrente["numero"]] = incipit(testo, 60)
        else:
            tipo = "DS" if STATEMENT_DS.search(testo) else "PS"
            righe.append([NOMI_QUANT.get(sezione, sezione), corrente["numero"], tipo,
                          corrente["pagina"], "", incipit(testo)])

    for numero_pagina, pagina in enumerate(pagine, start=1):
        for riga in righe_pulite(pagina):
            if riga.startswith(("Page ", "- ")) and len(riga) < 12:
                continue          # i numeri di pagina, in due formati diversi
            s = SEZIONE_QUANT.match(riga)
            if s:
                chiudi()
                corrente, sezione = None, s.group(1).strip()
                continue
            m = NUMERO_QUANT.match(riga)
            # Nella pagina delle risposte una voce e' lunga tre parole; nel resto del
            # file una riga cosi' corta e' quasi sempre una coda di elenco.
            if m and (sezione == "ANSWERS" or len(m.group(2)) > 25):
                chiudi()
                corrente = dict(numero=int(m.group(1)), pagina=numero_pagina,
                                testo=[m.group(2)])
            elif corrente:
                corrente["testo"].append(riga)
    chiudi()

    # Le risposte stampate nel file coprono un topic solo, il settimo.
    nome7 = NOMI_QUANT["GMAT Quant Topic 7"]
    for r in righe:
        if r[0] == nome7:
            r[4] = risposte.get(r[1], "")

    scrivi_csv("quant/quant-700-800-indice.csv",
               ["sezione", "domanda", "tipo", "pagina_pdf", "risposta", "incipit"],
               righe)
    return righe


# ---------------------------------------------------------------- 3000 RC

GRUPPI_RC = {"63": "GMAT New (63)", "22": "GMAT Extra (22)",
             "15": "GMAT Old OG (15)", "17": "OG New (17)"}
BRANO_RC = re.compile(r"Passage (\d{1,3}) \((\d{1,3})/(\d{1,3})\)")
# Nei primi tre gruppi le domande di ogni brano ripartono da 1; nell'ultimo la
# numerazione e' continua e arriva a tre cifre.
FINE_GMAT = "GRE  RC (No. 2"
DOMANDA_RC = re.compile(r"(?m)^(\d{1,3})\.\s*(?=[^\d])")


def rc3000_csv():
    """verbal/3000-rcs-indice.csv - i 117 brani GMAT, con lunghezza e chiave.

    Il .doc dice tre volte le stesse cose: due indici, poi i brani, poi in fondo una
    tabella di risposte con le stesse intestazioni. Le tre parti si distinguono da
    cosa segue l'intestazione di un brano - una tabulazione e un numero di pagina
    nell'indice, la prosa nel corpo, lettere nella tabella.

    Il gruppo di un brano non si legge dall'intestazione di sezione, che nel corpo e'
    in cinese, ma dal denominatore: "Passage 64 (1/22)" e' il primo dei 22 extra.
    """
    testo = scioglie_campi(testo_word97(
        os.path.join(QUI, "verbal", "3000-rcs-lsat-gmat-gre.doc")))
    taglio = testo.rindex("Passage 1 (1/63)")
    corpo, chiave = testo[:taglio], testo[taglio:]

    # Dopo il 117esimo brano il file prosegue con GRE e LSAT, che qui non si indicizzano.
    chiave = chiave[:chiave.index(FINE_GMAT)]

    # Nel corpo l'intestazione e' seguita da un a capo e dalla prosa; negli indici da
    # una tabulazione. Si tengono solo le prime.
    brani = [m for m in BRANO_RC.finditer(corpo) if corpo[m.end():m.end() + 1] == "\n"]
    # L'intestazione GRE compare gia' negli indici: si cerca dopo l'ultimo brano, non
    # dall'inizio, altrimenti il taglio cade prima ancora che i brani comincino.
    fine_gmat = corpo.index(FINE_GMAT, brani[-1].end())

    risposte = {}
    tagli = list(BRANO_RC.finditer(chiave))
    for i, m in enumerate(tagli):
        fine = tagli[i + 1].start() if i + 1 < len(tagli) else len(chiave)
        pezzo = chiave[m.end():fine]
        risposte[int(m.group(1))] = "".join(
            c for c in pezzo.split() if len(c) == 1 and c in "ABCDE")

    righe = []
    for i, m in enumerate(brani):
        fine = brani[i + 1].start() if i + 1 < len(brani) else fine_gmat
        blocco = corpo[m.end():fine].strip()
        numero = int(m.group(1))
        prima_domanda = DOMANDA_RC.search(blocco)
        brano = blocco[:prima_domanda.start()] if prima_domanda else blocco
        chiave_brano = risposte.get(numero, "")
        righe.append([GRUPPI_RC[m.group(3)], numero,
                      len(DOMANDA_RC.findall(blocco)), len(chiave_brano),
                      chiave_brano, len(unisci([brano]).split()), incipit(brano)])

    scrivi_csv("verbal/3000-rcs-indice.csv",
               ["gruppo", "brano", "domande", "risposte_note", "risposte", "parole",
                "incipit"], righe)
    return righe


# ---------------------------------------------------------------- Slingfox

TITOLI_SLINGFOX = ("General Commentary:", "Major CR Question Types:",
                   "TRICKY CR PROBLEMS")


def slingfox_markdown():
    """verbal/slingfox-cr-notes.md - gli appunti, con i titoli marcati."""
    testo = scioglie_campi(testo_word97(
        os.path.join(QUI, "verbal", "slingfox-cr-notes.doc")))

    fuori = [
        "# Slingfox - appunti di Critical Reasoning",
        "",
        "[<- I materiali](../README.md)",
        "",
        "Trascrizione di `verbal/slingfox-cr-notes.doc`, appunti di un utente storico del",
        "forum. Il testo e' suo, refusi compresi (*stimlus*, *your are being ask*): sono",
        "appunti personali, non una guida pubblicata, e restano come sono.",
        "",
        "---",
        "",
    ]
    for riga in testo.split("\n")[1:]:
        riga = riga.strip()
        if not riga:
            continue
        if riga in TITOLI_SLINGFOX:
            fuori += ["", f"## {riga.rstrip(':')}", ""]
        elif riga.startswith("Step #"):
            fuori += ["", f"### {riga}", ""]
        else:
            fuori += [riga.replace("$", r"\$"), ""]

    fuori += ["---", "", "[<- I materiali](../README.md)", ""]
    scrivi("verbal/slingfox-cr-notes.md", "\n".join(fuori))


# ---------------------------------------------------------------- flashcard verbal

def carte_flashcard(pagine):
    """Le carte di un mazzo: titolo, domanda, risposta.

    Domanda e risposta stanno su due pagine consecutive. La pagina della risposta si
    riconosce dal piede, che contiene la parola Answer - vale per tutti e due i mazzi
    del 2025, benche' lo scrivano in modo diverso.
    """
    carte, aperta = [], None
    for pagina in pagine:
        righe = righe_pulite(pagina)
        if len(righe) < 2:
            continue
        corpo = "\n".join(righe[1:-1])
        if "Answer" in righe[-1] and aperta:
            aperta["risposta"] = corpo
            carte.append(aperta)
            aperta = None
        else:
            aperta = dict(titolo=righe[0], domanda=corpo, risposta="")
    return carte


def scrivi_flashcard(nome_file, titolo, sottotitolo, pagine):
    """Scrive il Markdown di un mazzo e segnala le risposte tagliate nella fonte."""
    carte = carte_flashcard(pagine)
    # Una risposta che finisce con una lettera minuscola e nessuna punteggiatura e'
    # stata tagliata dal riquadro della diapositiva: nel PDF quel testo non c'e'.
    tagliate = [c for c in carte if re.search(r"[a-z] ?$", c["risposta"])]

    fuori = [f"# {titolo}", "", "[<- I materiali](../README.md)", "", sottotitolo, "",
             f"Sono **{len(carte)} carte**, domanda e risposta appaiate.", ""]
    if tagliate:
        fuori += [f"In **{len(tagliate)}** la risposta si interrompe a meta' parola. Non e'",
                  "l'estrazione: il testo sfora dal riquadro della diapositiva e nel PDF non",
                  "c'e'. Le carte interessate sono segnate qui sotto.", ""]
    fuori += ["---", ""]

    for c in carte:
        fuori += [f"## {c['titolo']}", "", c["domanda"].replace("$", r"\$"), ""]
        if c in tagliate:
            fuori += ["> La risposta e' troncata nella fonte.", ""]
        fuori += [c["risposta"].replace("$", r"\$"), "", "---", ""]

    fuori += ["[<- I materiali](../README.md)", ""]
    scrivi(nome_file, "\n".join(fuori))
    return carte, tagliate


def flashcards_markdown():
    """I due mazzi del 2025, verbal e quant."""
    verbal = scrivi_flashcard(
        "verbal/verbal-flashcards-2025.md",
        "GMAT Club Verbal Flashcards 2025",
        "Trascrizione di `verbal/verbal-flashcards-2025.pdf`, datato 17 settembre 2025 e\n"
        "generato da PowerPoint con python-pptx. Critical Reasoning e Reading Comprehension.",
        pagine_pdf(os.path.join(QUI, "verbal", "verbal-flashcards-2025.pdf"))[1:])
    quant = scrivi_flashcard(
        "quant/math-flashcards-2025.md",
        "GMAT Club Math Flashcards 2025",
        "Trascrizione di `quant/math-flashcards-2025.pdf`, stesso giorno e stesso\n"
        "generatore del mazzo verbal. Aritmetica, statistica, probabilita', word problems.\n"
        "Ogni carta ha cinque alternative e la risposta dichiarata.",
        pagine_pdf(os.path.join(QUI, "quant", "math-flashcards-2025.pdf"))[1:])
    return verbal, quant


# ---------------------------------------------------------------- tutto insieme

def main():
    print("Data Sufficiency:")
    ds = ds_markdown()
    print("Critical Reasoning:")
    risposte = cr_soluzioni()
    cr = cr_derivati(risposte)
    print("Quant:")
    quant = quant_csv()
    print("3000 RC:")
    rc = rc3000_csv()
    print("Slingfox:")
    slingfox_markdown()
    print("Flashcard:")
    (carte_verbal, _), (carte_quant, _) = flashcards_markdown()

    # Due controlli che valgono la pena: se saltano, l'estrazione e' andata storta e
    # meglio accorgersene qui che dopo, studiando su un file sbagliato.
    storte = [c for c in cr if c[5] != 5]
    if storte:
        raise SystemExit(f"CR: {len(storte)} domande non hanno cinque alternative")
    scoppiate = [r for r in rc if r[2] != r[3]]
    if scoppiate:
        raise SystemExit(f"3000 RC: {len(scoppiate)} brani senza chiave corrispondente")

    print(f"\n{len(ds)} domande di DS, {len(cr)} di CR, {len(quant)} problemi di quant,")
    print(f"{len(rc)} brani di RC con {sum(r[2] for r in rc)} domande,")
    print(f"{len(carte_verbal)} flashcard verbal e {len(carte_quant)} quant.")


if __name__ == "__main__":
    main()
