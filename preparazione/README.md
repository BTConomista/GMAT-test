# Come si prepara l'esame

[← Indice del libro](../README.md)

Due documenti di ricerca sull'ecosistema intorno al GMAT: cosa esiste, cosa vale, cosa
costa. Non sono materiale d'esame — per quello ci sono [`book/`](../book) e
[`gmatclub/materiali/`](../gmatclub/materiali/README.md) — sono la mappa che dice cosa
farne.

| File | Cosa c'è dentro |
|:---|:---|
| [`guide.md`](guide.md) | Le guide da leggere: study plan, quant, verbal, Data Insights, timing, punteggio, debrief, cosa comprare |
| [`strumenti-e-costi.md`](strumenti-e-costi.md) | Gli strumenti del forum, le risorse gratuite fuori da GMAT Club, i trial, sei miti smontati, il tariffario completo e l'Italia |

Compilati il 20 e il 21 agosto 2026. Sono documenti di terzi come tutto il resto di
`gmatclub/`: si riportano come sono, e le osservazioni stanno qui sotto invece che dentro
il testo — stessa regola del §5 di [CONVENZIONI.md](../CONVENZIONI.md).

L'unica modifica fatta al testo è meccanica: `strumenti-e-costi.md` rimandava a un file
chiamato `guide-gmat-focus.md`, che qui si chiama `guide.md`.

---

## Cosa ho verificato

I due documenti dichiarano da soli cosa non hanno potuto confermare, e lo fanno bene —
`guide.md` chiude con «Note sulla verifica», `strumenti-e-costi.md` con un §11 «Non
verificato» lungo trenta righe. È la parte migliore di tutti e due: non c'è quasi niente
affermato senza dire da dove viene.

Quello che segue è il controllo che potevo fare io, e che loro non potevano: **incrociarli
con i dati che il repo ha già**.

### Regge

**La struttura dell'esame.** 21 + 23 + 20 = 64 domande, 45 minuti a sezione = 2h15.
Coerente.

**La formula del punteggio.** `(Q + V + DI − 180) × 20/3 + 205` dà esattamente 205 al
minimo (60+60+60) e 805 al massimo (90+90+90). Un'osservazione sulla resa: la frase
«arrotondata al multiplo di 5 più vicino che finisce per 5» confonde — vuol dire che la
scala **va di 10 in 10**, cioè 205, 215, 225 … 805, sessantuno valori possibili.

**Il Math Book.** `guide.md` §4 lo dà per aggiornato al Focus, con la geometria piana
rimossa. Ora il file è nel repo e si può controllare: è l'**8ª edizione, maggio 2024**, e
il suo indice ha *Functions / Coordinate Geometry* ma nessun capitolo di geometria piana.
Confermato. *(Da correggere invece l'elenco HTML da cui era partita la raccolta dei
materiali, che lo dava «aggiornato a gennaio 2025».)*

**L'error log.** `guide.md` §9 dice che GMAT Club non ha un template scaricabile pensato
per le tre sezioni del Focus. Il template che abbiamo lo conferma dall'interno: le sue
colonne sono PS, DS, RC, CR e **SC** — mancano TPA, G&T e MSR.

**Il `.xlsm`.** Entrambi i documenti raccomandano l'`.xlsx` senza macro. Verificato
aprendo l'archivio: nessun `vbaProject.bin`.

### Non regge, o regge a metà

**Il Verbal non è 50/50.** `guide.md` §2 presenta una tabella con Quant, Verbal e Data
Insights come se venissero tutte dalla stessa analisi di bb. Ma bb ha analizzato **277
domande di Problem Solving**: la riga del quant ha una fonte, le altre due no. E i numeri
del libro vero raccontano un'altra cosa:

| | Nella tabella di `guide.md` | Nella *Official Guide 2025-2026* |
|:---|:---|:---|
| Verbal | CR ~50% · RC ~50% | CR 190 · RC 146 → **57% / 43%** |
| Data Insights | DS ~50% | DS 137 su 331 di materiale DI → **41%** |

La composizione del libro non è la composizione dell'esame — il libro stampa esercizi, non
un modello del test. Ma allora **nemmeno la tabella può essere presentata come la
composizione dell'esame** senza dire da dove viene. Vale come ordine di grandezza, non
come blueprint.

**I due documenti si contraddicono sullo Starter Kit gratuito.** `guide.md` §11 dice
«~90 domande reali + i primi 2 mock»; `strumenti-e-costi.md` §4 dice «70 domande ufficiali
più i Practice Exam 1 e 2». Novanta o settanta: uno dei due sbaglia, e nessuno dei due lo
segnala.

**E sui reset dei mock ufficiali.** `guide.md` §1 li dà per «gratuiti e **resettabili**».
`strumenti-e-costi.md` §4 dice che si possono ripetere ma non resettare a metà, che
ripetendoli rivedi domande già fatte, e che quindi «valgono davvero una volta ciascuno» —
e nel suo §11 mette il numero di reset fra le cose non verificate. La seconda versione è
più prudente e va preferita: **usane uno all'inizio e uno alla fine**, e considerali
spesi.

**«56 URL controllati».** I link esterni in `guide.md` sono 91, di cui 84 distinti. Il
conto di 56 riguarderà solo i thread e non i download, ma non è detto nel testo.

**I link non sono riverificabili da qui.** GMAT Club sta dietro Cloudflare e risponde 403
o 503 a qualunque richiesta automatica — è la stessa cosa scritta in
[`gmatclub/README.md`](../gmatclub/README.md) e nel §12 di `guide.md`. Che i 56 URL
fossero attivi il 20 agosto 2026 resta una dichiarazione dell'autore, non una cosa che ho
potuto ricontrollare.

---

## Il dato che nessuno dei due documenti ha

Il repo può aggiungere una cosa che le due ricerche non potevano sapere: **come sono
distribuiti davvero i tipi di domanda nella *Official Guide***, presi
dall'[indice delle 802 domande](../gmatclub/README.md). E il confronto con il nostro
eserciziario di CR dice dove allenarsi e dove no.

| Tipo di CR | Nella *Official Guide* (190 domande) | Nel nostro [eserciziario](../gmatclub/materiali/verbal/cr-700-800-domande.md) (302) |
|:---|---:|---:|
| Weaken | 45 · **24%** | 37 · 12% |
| Strengthen | 36 · **19%** | 22 · 7% |
| Assumption | 21 · 11% | 34 · 11% |
| Bold Face | 21 · 11% | 34 · 11% |
| Resolve Paradox | 18 · 10% | 17 · 6% |
| Evaluate Argument | 13 · 7% | 12 · 4% |
| Inference / Conclusion | 9 · 5% | 36 · 12% |
| **Complete the Passage** | 10 · **5%** | **0** |
| **Logical Flaw** | 5 · 3% | **0** |
| Altri e combinazioni | 12 · 6% | — |
| Miscellaneous *(non tipizzate)* | — | 110 · 36% |

Tre cose da portarsi via:

1. **Weaken e Strengthen sono il 43% del CR nella OG, e il 20% del nostro eserciziario.**
   Se ti alleni solo su quel file, ti alleni poco sui due tipi più frequenti.
2. **Complete the Passage non esiste nel nostro eserciziario.** È il 5% delle domande di
   CR del libro — quelle che finiscono con un vuoto da riempire. Per quelle servono le
   domande del libro o le raccolte del forum.
3. Il 36% del nostro file è marcato *Miscellaneous* e non è tipizzato, quindi il confronto
   è indicativo. Ma lo scarto su Weaken e Strengthen è troppo grande per essere solo
   quello.

Per la Reading Comprehension lo stesso indice dà le materie dei 36 brani della OG, contate
sulle 146 domande che ci stanno sopra: **Science 37%**, **Business 28%**, **Social Science
24%**, **Humanities 12%**. Brani lunghi e corti si dividono esattamente a metà, 70 domande
contro 71.

Serve a scegliere su cosa allenarsi: se sbagli sempre i brani scientifici, stai sbagliando
il tipo più frequente. I 117 brani di
[`3000-rcs-indice.csv`](../gmatclub/materiali/verbal/3000-rcs-indice.csv) hanno la colonna
`parole` per pescare un brano lungo o corto a seconda di cosa vuoi allenare.

---

## Cosa manca ancora, in concreto

`guide.md` §12 elenca 17 PDF scaricabili. Di quelli, **14 sono già in
[`gmatclub/materiali/`](../gmatclub/materiali/README.md)**. Ne restano tre:

| File | Peso | Perché prenderlo |
|:---|---:|:---|
| [`ADVANCED OVERLAPPING SETS PROBLEMS.pdf`](https://gmatclub.com/forum/download/file.php?id=18937) | 408 KB | Le due formule dei Venn a tre insiemi, «almeno due» contro «esattamente due», con 11 esempi. Gli insiemi sovrapposti sono l'8% del DS nella OG |
| [`CR_Quick_Reference_Rev0.pdf`](https://gmatclub.com/forum/download/file.php?id=25370) | 588 KB | Scheda di consultazione rapida sul CR, complemento della *Monster Guide* che già abbiamo |
| [`Flashcards - Quantitative Review by Miguelmick 2024.pdf`](https://gmatclub.com/forum/download/file.php?id=85768) | 1,07 MB | Terzo mazzo di flashcard di quant, 2024 |

Quando arrivano: i primi due in `gmatclub/materiali/quant/` e `verbal/`, il terzo in
`quant/`. Poi si aggiorna il catalogo e, se hanno un testo estraibile, si aggiunge una
funzione a `estrai_derivati.py`.

**Il download chiede l'account e non parte da uno script:** vanno presi da un browser già
autenticato, come tutti gli altri.

---

## Da dove si comincia, con quello che c'è già

Le due ricerche dicono cosa esiste al mondo. Questo dice cosa fare lunedì mattina con
quello che è già su disco.

**Prima di tutto, una volta sola.** Il [test diagnostico](../gmatclub/materiali/diagnostic-test-v6.2.pdf)
su carta, per sapere da dove parti senza bruciare un mock ufficiale. È del 2013, quindi
ignora la parte di Sentence Correction se la incontri.

**Le tre letture di orientamento**, in quest'ordine: il §2 di [`guide.md`](guide.md#2-da-dove-si-comincia--4-letture-di-orientamento),
poi [*The one thing on the GMAT*](../gmatclub/materiali/metodo/the-one-thing-on-the-gmat.pdf),
poi il §7 di `guide.md` sul timing. Un'ora in tutto, e ti risparmia settimane.

**Poi si divide.**

| Se lavori su | Parti da | Poi |
|:---|:---|:---|
| Teoria di quant | [`gmat-club-math-book-2024.pdf`](../gmatclub/materiali/quant/gmat-club-math-book-2024.pdf) | I problemi per argomento con [`quant-700-800-indice.csv`](../gmatclub/materiali/quant/quant-700-800-indice.csv) |
| Data Sufficiency | Le [51 domande di Bunuel](../gmatclub/materiali/quant/ds-700-plus-bunuel.md), spiegate a fondo | La *DS Question Directory* linkata in `guide.md` §6 |
| Critical Reasoning | La [*Monster CR Guide*](../gmatclub/materiali/verbal/comprehensive-cr-guide.pdf) per il metodo | Le [302 domande](../gmatclub/materiali/verbal/cr-700-800-domande.md) con le [soluzioni](../gmatclub/materiali/verbal/cr-700-800-soluzioni.md) accanto |
| Reading Comprehension | Il §5 di `guide.md` | I [117 brani](../gmatclub/materiali/verbal/3000-rcs-indice.csv), scelti per lunghezza |
| Ripasso veloce | I due mazzi di flashcard [quant](../gmatclub/materiali/quant/math-flashcards-2025.md) e [verbal](../gmatclub/materiali/verbal/verbal-flashcards-2025.md) | — |

**Il buco vero resta Data Insights**, e i due documenti lo dicono senza girarci intorno.
Su Data Sufficiency il materiale gratuito basta e avanza; su Multi-Source Reasoning, Table
Analysis e Graphics Interpretation no, e in `gmatclub/materiali/` non c'è nulla — perché
non esiste nulla di gratuito che valga. Le due strade indicate sono l'*Official Guide Data
Insights Review* e i video di GMAT Ninja, che secondo `strumenti-e-costi.md` §4 sono
l'unica copertura video seria e gratuita di quella sezione.

**Due abitudini da prendere il primo giorno**, dai due documenti:

- cliccare **START** sul timer di GMAT Club a ogni domanda, perché è quello che alimenta
  l'error log automatico e ti dà anche 1 punto Rewards al giorno;
- tenere un error log che classifichi l'errore **per causa** — buco di contenuto, tempo,
  disattenzione — e non per argomento. Il [template](../gmatclub/materiali/metodo/trianglock-error-log.xlsx)
  che abbiamo va prima ripulito dai dati d'esempio e riadattato ai tipi del Focus.

---

[← Indice del libro](../README.md) · [I materiali scaricati](../gmatclub/materiali/README.md)
