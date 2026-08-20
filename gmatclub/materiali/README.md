# I materiali scaricati da GMAT Club

[← L'indice delle domande](../README.md) · [← Indice del libro](../../README.md)

Undici allegati presi dall'archivio di GMAT Club, più una versione leggibile di quelli
che leggibili non erano. Non sono materiale ufficiale GMAC e non c'entrano con la
trascrizione della *Official Guide*: stanno qui perché sono il complemento naturale del
libro — esercizi in più, metodo, e un paio di cose che il libro non copre affatto.

**La cosa più importante da sapere prima di aprirli.** Tranne le flashcard verbal, che
sono del 2025, tutto il resto è del **2005–2013**. Nessuno di questi file sa cosa sia il
GMAT Focus: parlano di Sentence Correction, di AWA, di un esame da quattro ore. Il
ragionamento che insegnano è ancora valido — CR e RC non sono cambiati, e la matematica
nemmeno — ma il contorno no.

---

## Cosa c'è

| File | Peso | Cos'è | Come sta |
|:---|---:|:---|:---|
| [`quant/quant-700-800-problems.pdf`](quant/quant-700-800-problems.pdf) | 720 KB | 892 problemi di quant divisi per argomento, Sandeep Gupta, 2009 | 🟨 incompleto |
| [`quant/math-shortcuts-manoscritti.pdf`](quant/math-shortcuts-manoscritti.pdf) | 996 KB | 42 pagine di appunti **scritti a mano** su scorciatoie di calcolo, 2006 | 🟨 scansione |
| [`quant/ds-700-plus-bunuel.doc`](quant/ds-700-plus-bunuel.doc) | 988 KB | 51 domande di Data Sufficiency risolte da Bunuel, 2010 | ✅ |
| [`verbal/cr-700-800-domande.pdf`](verbal/cr-700-800-domande.pdf) | 696 KB | 302 domande di Critical Reasoning per tipo, 2008 | ⚠️ senza risposte |
| [`verbal/comprehensive-cr-guide.pdf`](verbal/comprehensive-cr-guide.pdf) | 844 KB | *The Monster CR Strategy Guide*, 32 pagine di metodo, 2010 | ✅ |
| [`verbal/slingfox-cr-notes.doc`](verbal/slingfox-cr-notes.doc) | 72 KB | Appunti di CR in cinque passi, più problemi ostici | ✅ |
| [`verbal/3000-rcs-lsat-gmat-gre.doc`](verbal/3000-rcs-lsat-gmat-gre.doc) | 7,2 MB | 117 brani di RC del GMAT con chiave, più GRE e LSAT, 2005 | ✅ |
| [`verbal/verbal-flashcards-2025.pdf`](verbal/verbal-flashcards-2025.pdf) | 188 KB | 18 flashcard di CR e RC, settembre 2025 | 🟨 3 tagliate |
| [`metodo/the-one-thing-on-the-gmat.pdf`](metodo/the-one-thing-on-the-gmat.pdf) | 1000 KB | Venti membri raccontano cosa avrebbero voluto sapere, 2011 | ✅ |
| [`metodo/trianglock-error-log.xlsx`](metodo/trianglock-error-log.xlsx) | 816 KB | Template di error log in Excel, senza macro | 🟨 da ripulire |
| [`diagnostic-test-v6.2.pdf`](diagnostic-test-v6.2.pdf) | 500 KB | Test diagnostico di GMAT Club su carta, novembre 2013 | ✅ |

Il Data Sufficiency sta sotto `quant/` perché di matematica si tratta, ma nel GMAT Focus
non è più una sezione a sé: le domande di DS stanno dentro **Data Insights**, come dice
il [README dell'indice](../README.md).

---

## Le versioni leggibili

Cinque di questi file si leggono male: due sono `.doc` di Word 97 che LibreOffice si
rifiuta di aprire, uno ha le formule solo come immagini remote, uno perde i trattini
quando ne estrai il testo. Accanto a ciascuno c'è un derivato in Markdown o in CSV,
prodotto da [`estrai_derivati.py`](estrai_derivati.py).

| Derivato | Contenuto |
|:---|:---|
| [`quant/ds-700-plus-bunuel.md`](quant/ds-700-plus-bunuel.md) | Le 51 domande di DS con la spiegazione intera, le formule in LaTeX e il link alla discussione |
| [`quant/quant-700-800-indice.csv`](quant/quant-700-800-indice.csv) | Le 892 domande di quant: sezione, numero, PS o DS, pagina del PDF, incipit |
| [`verbal/cr-700-800-domande.md`](verbal/cr-700-800-domande.md) | Le 302 domande di CR, con il corsivo della domanda e le cinque alternative |
| [`verbal/cr-700-800-indice.csv`](verbal/cr-700-800-indice.csv) | Le stesse 302, una riga per domanda, per cercarle e incrociarle |
| [`verbal/3000-rcs-indice.csv`](verbal/3000-rcs-indice.csv) | I 117 brani di RC: gruppo, quante domande, **la chiave di risposta**, quante parole |
| [`verbal/slingfox-cr-notes.md`](verbal/slingfox-cr-notes.md) | Gli appunti, con i titoli marcati |
| [`verbal/verbal-flashcards-2025.md`](verbal/verbal-flashcards-2025.md) | Le 18 carte, domanda e risposta appaiate |

**I derivati non correggono niente.** Vale il §5 di [CONVENZIONI.md](../../CONVENZIONI.md):
se la fonte sbaglia, il derivato sbaglia uguale. Cambia solo la resa, e solo in questi
punti:

- le formule di Bunuel, che nel `.doc` sono immagini servite da un CGI, diventano LaTeX —
  lo stesso LaTeX che stava scritto nell'indirizzo dell'immagine, non una ritrascrizione;
- il corsivo del PDF di CR diventa `*corsivo*`;
- i dollari della prosa sono protetti con `\$`, altrimenti GitHub li scambia per
  delimitatori di formula;
- il tipo `PS`/`DS` nell'indice quant è **dedotto** dalla presenza delle due affermazioni
  numerate, non letto dalla fonte. È l'unica colonna di quei CSV che non viene dal file.

Per rigenerarli:

```
pip install pypdf olefile
python3 gmatclub/materiali/estrai_derivati.py
```

Lo script finisce con due controlli e si ferma se saltano: che tutte le domande di CR
abbiano cinque alternative, e che per ogni brano di RC il numero di domande contate nel
testo coincida con il numero di risposte nella chiave. Al momento tornano tutti e due —
302 domande su 302, 117 brani su 117, 860 domande e 860 risposte.

---

## Scheda per scheda

### `quant/quant-700-800-problems.pdf` — 892 problemi

Otto argomenti, ma **il topic 3 non c'è**: si salta dal 2 al 4. Le sezioni, con la pagina
del PDF in cui cominciano:

| Sezione | Pagine | Domande | di cui DS |
|:---|:---:|---:|---:|
| Topic 1 — General Arithmetic | 1–16 | 164 | 58 |
| Topic 2 — Statistics | 17–30 | 171 | 81 |
| Topic 4 — Numbers | 31–45 | 195 | 63 |
| Topic 5 — Geometry | 46–59 | 80 | 34 |
| Topic 6 — Co-ordinate Geometry | 60–63 | 31 | 11 |
| Topic 7 — Permutations and Combinations | 64–68 | 66 | 6 |
| Topic 8 — Probability | 71–76 | 69 | 12 |
| Miscellaneous — Word Problems | 77–82 | 56 | 23 |
| Calculations, Exponents, Basic Algebra | 83–86 | 60 | 25 |

I 313 problemi marcati `DS` sono un terzo del totale, e nel Focus non stanno più in
quant: sono la materia prima per la parte di Data Insights.

Tre cose da sapere prima di usarlo:

1. **Le risposte ci sono per un topic solo.** Le pagine 69–70 danno la chiave del Topic 7,
   domande 1–66. Per gli altri 826 problemi non c'è nulla.
2. **Il file si interrompe a metà.** L'ultima pagina finisce sulla domanda 67 di
   *Calculations, Exponents, Basic Algebra*, in mezzo a una frase.
3. **Il livello di testo perde i trattini.** Nel PDF si legge `three-digit`, ma chi ne
   estrae il testo — noi, un lettore di schermo, una ricerca — trova `threeHdigit`. È un
   difetto della codifica del font, e si vede anche nell'indice CSV.

### `quant/math-shortcuts-manoscritti.pdf` — appunti a mano

Non è un manuale: sono 42 pagine di quaderno a righe di qualcuno, passate in una
fotocopiatrice Canon nel giugno 2006. Non c'è nessun livello di testo — è tutto immagine
in bianco e nero a circa 200 dpi — quindi non si può cercare dentro, e non c'è derivato.

Il contenuto è buono e denso: moltiplicazioni rapide (×5 come ×10÷2, il trucco dell'11,
i numeri che finiscono per 10), massima potenza che divide un fattoriale, formule di
insiemi e probabilità con i diagrammi di Venn a due e tre cerchi.

**Va letto con la matita in mano, non preso per buono.** A pagina 26 c'è scritto
$P(A \cup B) > P(A) + P(B)$, che è falso — l'unione non può superare la somma — e nella
formula di inclusione-esclusione a tre insiemi l'ultimo termine è scritto
$P(A \cup B \cup C)$ dove il senso vuole $P(A \cap B \cap C)$. Sono appunti personali con
gli errori che hanno gli appunti personali.

### `quant/ds-700-plus-bunuel.doc` — 51 domande, non 700

**Il titolo inganna.** «700+» è la fascia di difficoltà, non il numero di domande: dentro
ce ne sono **51**, numerate da 1 a 55 con le 16–19 assenti già nella fonte.

Detto questo, è il file migliore del lotto. Le domande sono raccolte e risolte da
**Bunuel**, che sul forum è il riferimento per il quant, e ogni domanda ha la spiegazione
completa — spesso due, per due strade diverse — e il link alla sua discussione. Gli
argomenti più battuti sono le disuguaglianze (13, contando le combinazioni con modulo e
problemi a parole), le proprietà dei numeri (10 fra le due grafie), la geometria analitica
(7) e i resti (3).

Le formule non sono testo: sono immagini che il `.doc` chiede a `gmatclub.com/cgi-bin/mimetex.cgi`,
un CGI che rende LaTeX. Sono 960 immagini per 554 formule distinte, e aperto oggi — con
quel server ormai fuori uso — il documento le mostra come altrettanti riquadri vuoti. Ma **il LaTeX è dentro l'indirizzo dell'immagine**, e da lì si recupera
senza scaricare nulla: è quello che fa il derivato.

### `verbal/cr-700-800-domande.pdf` — 302 domande, zero risposte

Dalla raccolta *The 700-800 Club*, aprile 2008. Otto tipi di domanda:

| Topic | Domande |
|:---|---:|
| 1 — Conclusion | 36 |
| 2 — Assumptions | 34 |
| 3 — Weaken | 37 |
| 4 — Strengthen | 22 |
| 5 — Evaluate | 12 |
| 6 — Paradox | 17 |
| 7 — Boldface | 34 |
| 8 — Miscellaneous | 110 |

Il topic 8 numera **due volte da capo**, 1–10 e poi 1–100: non è un errore di lettura, è
così nella fonte, e il derivato tiene le due serie separate.

Tre difetti, in ordine di gravità:

1. **Le risposte non ci sono.** Stanno in `CR 700 to 800 club Solutions.pdf`, un file a
   parte da 1,3 MB che non abbiamo. Senza quello, sono 302 domande su cui allenarsi senza
   sapere se hai indovinato.
2. **Le alternative non sono marcate A–E.** Nell'originale sono puntini elenco, senza
   lettera — verificato guardando la pagina, non solo il testo estratto. Con le soluzioni
   alla mano bisognerà contare le posizioni.
3. **L'ultima pagina è un errore di stampa.** La pagina 75 contiene
   `ERROR: undefined / OFFENDING COMMAND: DeleteMe`: il PDF è stato generato male nel 2008
   con Ghostscript. Il contenuto vero finisce a pagina 73.

### `verbal/comprehensive-cr-guide.pdf` — la guida al CR

Trentadue pagine di metodo, novembre 2010, titolo vero *The Monster CR Strategy Guide*.
Non è un prodotto editoriale: è il compendio che uno studente si è fatto leggendo i
manuali in circolazione, e lo dichiara in prima pagina — «I do NOT claim to have created
the content by myself», con l'elenco delle fonti in fondo. Deconstruction in cinque passi,
le tre famiglie di domande, la negazione dell'assunzione, le trappole ricorrenti.

Copre lo stesso terreno del capitolo 7 della *Official Guide*, che nel repo è ancora da
trascrivere.

### `verbal/slingfox-cr-notes.doc` — 72 KB ben spesi

Gli appunti di un utente storico del forum. Cinque passi, poi i tipi di domanda con la
tattica giusta per ciascuno, poi una sezione di problemi ostici. Sono appunti personali e
si vede — ci sono i refusi di chi scrive di fretta (*stimlus*, *your are being ask*) — ma
il contenuto è la stessa sostanza della guida qui sopra in un decimo dello spazio.

### `verbal/3000-rcs-lsat-gmat-gre.doc` — il pezzo grosso

Sette megabyte, 394.800 parole, compilato da una comunità cinese nel febbraio 2005 (le
intestazioni di sezione sono in cinese). Dentro c'è, in quest'ordine: **117 brani di
Reading Comprehension del GMAT**, poi i test GRE cartacei No. 2–No. 9, poi i GRE dal 1990
al 1999, poi le sezioni di RC di 29 LSAT, e in fondo **le chiavi di risposta di tutto**.

L'indice CSV copre i 117 brani GMAT, che sono la parte che serve:

| Gruppo | Brani | Domande |
|:---|---:|---:|
| GMAT New (63) | 63 | 464 |
| GMAT Extra (22) | 22 | 183 |
| GMAT Old OG (15) | 15 | 125 |
| OG New (17) | 17 | 88 |

860 domande in tutto, e per **tutte e 860** la chiave c'è: il conteggio delle domande nel
testo e il conteggio delle risposte nella chiave coincidono su tutti e 117 i brani. I
brani vanno da 197 a 691 parole, mediana 393 — la colonna `parole` serve a scegliere un
brano corto o lungo secondo cosa vuoi allenare.

Quando arriverà il turno del capitolo 8, i brani dei gruppi *Old OG* e *OG New* sono
edizioni vecchie della *Official Guide*: vanno confrontati, non dati per equivalenti.

### `verbal/verbal-flashcards-2025.pdf` — 18 carte

L'unico file recente: 17 settembre 2025. Trentasette pagine che sono 18 carte più il
frontespizio — domanda su una pagina, risposta sulla successiva. Otto carte di CR di
metodo, sette di CR con una domanda vera e la risposta commentata, sei di RC.

**In tre carte la risposta è tagliata a metà parola** — «track who s», «restate in your
ow», «introduce, e». Non è l'estrazione: il testo sfora dal riquadro della diapositiva e
nel PDF non c'è proprio. Il file è stato generato da PowerPoint con `python-pptx`, e chi
l'ha fatto non ha ricontrollato le ultime tre.

### `metodo/the-one-thing-on-the-gmat.pdf` — 20 debriefing

© 2011. Venti membri del forum, punteggi da 590 a 770, rispondono a una domanda sola:
cosa avrei voluto sapere prima di dare il GMAT. Il post più letto del forum sul *come* si
studia invece che sul *cosa*.

Molto regge ancora: fai i test simulati presto e spesso, non startene fermo su una domanda,
la resistenza a stare seduto conta quanto il ripasso. Altro no: gli interventi su AWA e
sugli idiom parlano di sezioni che il Focus non ha più, e uno si chiede come verrà pesata
«la nuova sezione Integrated Reasoning».

### `metodo/trianglock-error-log.xlsx` — il template di error log

Sei fogli: le istruzioni e cinque schede identiche, una per fonte di domande, da 1.000
righe l'una. Per ogni domanda registri tipo, data, secondi impiegati, la risposta che hai
dato, **come** ci sei arrivato (la sapevi / per esclusione / a caso) e la risposta giusta;
il foglio calcola percentuale di risposte esatte, media dei tempi, media mobile sulle
ultime dieci, e colora le domande da rivedere.

Due cose prima di usarlo:

- **È pre-Focus.** I tipi di domanda sono PS, DS, RC, CR e **SC**: mancano Two-Part
  Analysis, Graphs and Tables e Multi-Source Reasoning, e c'è Sentence Correction che non
  esiste più. Le colonne dei tipi si cambiano in riga 6, colonne K–O.
- **Ci sono dentro i dati di esempio dell'autore**: 16 righe compilate nella prima scheda
  e 6 in ognuna delle altre. Vanno cancellate prima di cominciare, o i tuoi numeri
  partiranno sporchi.

Niente macro — il file è `.xlsx`, non `.xlsm`, e nell'archivio non c'è nessun
`vbaProject.bin`. Si apre ovunque senza avvisi di sicurezza.

### `diagnostic-test-v6.2.pdf` — il diagnostico

Dieci pagine, GMAT Club, novembre 2013. Domande di quant e verbal ordinate per argomento,
pensate per capire dove sei senza bruciare un test adattivo.

Il livello di testo c'è ma **le formule sono illeggibili**: erano oggetti equazione di
Word e nell'estrazione i radicali spariscono (`289324 = ?` sta per una radice). Va letto
come PDF impaginato, non come testo, e per questo non ha derivato.

---

## Cosa manca

L'elenco da cui vengono questi file ne aveva quattordici. Tre non li abbiamo:

| Mancante | Peso | Perché conta |
|:---|---:|:---|
| **CR 700 to 800 club Solutions.pdf** | 1,3 MB | Le risposte delle 302 domande di CR qui sopra. È il buco più grave dei tre |
| GMAT Club Math Book 2024 v8.pdf | 2,86 MB | L'unico materiale del forum davvero aggiornato al Focus, gennaio 2025. Copre lo stesso terreno del capitolo 3 con molti più esempi |
| GMAT-Club-Math-Flashcards-2025.pdf | 363 KB | Il gemello quant delle flashcard verbal |

Si scaricano dall'archivio allegati di GMAT Club, che chiede l'account (gratuito):

- [`CR 700 to 800 club Solutions.pdf`](https://gmatclub.com/forum/download/file.php?id=18142)
- [`GMAT Club Math Book 2024 v8.pdf`](https://gmatclub.com/forum/download/file.php?id=76387)
- [`GMAT-Club-Math-Flashcards-2025.pdf`](https://gmatclub.com/forum/download/file.php?id=85859)

Il server risponde `503` alle richieste automatiche: vanno scaricati da un browser
già autenticato. Quando arrivano, il file delle soluzioni va in `verbal/` accanto alle
domande, e conviene aggiungere allo script una funzione che le appaia una a una.

---

## Da dove vengono, e i loro indirizzi

Tutti dall'archivio allegati del forum, `gmatclub.com/forum/download.php`. Il nome qui è
stato normalizzato; questo è il nome originale e il link da cui riscaricarlo:

| Qui | Nome originale | Link |
|:---|:---|:---|
| `quant/quant-700-800-problems.pdf` | Quant 700 - 800 level problems.pdf | [18066](https://gmatclub.com/forum/download/file.php?id=18066) |
| `quant/math-shortcuts-manoscritti.pdf` | Quantitative-GMAT-Math-Shortcuts.pdf | [10830](https://gmatclub.com/forum/download/file.php?id=10830) |
| `quant/ds-700-plus-bunuel.doc` | 700+ GMAT Data Sufficiency Questions With Explanations.doc | [12634](https://gmatclub.com/forum/download/file.php?id=12634) |
| `verbal/cr-700-800-domande.pdf` | cr 700 to 800 level practice questions.pdf | [18141](https://gmatclub.com/forum/download/file.php?id=18141) |
| `verbal/comprehensive-cr-guide.pdf` | Comprehensive Critical Reasoning Guide.pdf | [13452](https://gmatclub.com/forum/download/file.php?id=13452) |
| `verbal/slingfox-cr-notes.doc` | Slingfox CR Notes.doc | [11892](https://gmatclub.com/forum/download/file.php?id=11892) |
| `verbal/3000-rcs-lsat-gmat-gre.doc` | 3000_RCs_LSAT_GMAT_GRE.doc | [5144](https://gmatclub.com/forum/download/file.php?id=5144) |
| `verbal/verbal-flashcards-2025.pdf` | GMAT_Club_Verbal_Flashcards_v2025.pdf | [85860](https://gmatclub.com/forum/download/file.php?id=85860) |
| `metodo/the-one-thing-on-the-gmat.pdf` | The one thing on the GMAT.pdf | [15741](https://gmatclub.com/forum/download/file.php?id=15741) |
| `metodo/trianglock-error-log.xlsx` | Trianglock_GMAT Error Log-2.xlsx | [10068](https://gmatclub.com/forum/download/file.php?id=10068) |
| `diagnostic-test-v6.2.pdf` | Diagnostic_Test_v6.2.pdf | [21665](https://gmatclub.com/forum/download/file.php?id=21665) |

Sono materiale della community, caricato dagli utenti sul forum: né ufficiale GMAC, né
verificato da nessuno. Stanno qui a uso personale di studio, come il resto del repo.

---

[← L'indice delle domande](../README.md) · [← Indice del libro](../../README.md)
