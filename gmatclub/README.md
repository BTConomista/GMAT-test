# L'indice delle domande, da GMAT Club

[← Indice del libro](../README.md)

[GMAT Club](https://gmatclub.com) è un forum di preparazione al GMAT. Ogni domanda
ufficiale ha lì una discussione, e la comunità mantiene per ogni edizione della *Official
Guide* un **error log**: un foglio di calcolo con l'elenco completo delle domande del
libro. Quel foglio contiene due cose che noi non abbiamo, ed è il motivo per cui questa
cartella esiste.

## Cosa c'è qui

| File | Contenuto |
|:---|:---|
| `og-2025-2026.csv` | le 802 domande **stampate** nel libro, una per riga |
| `og-2025-2026-online.csv` | le 137 domande del solo *Online Question Bank* (G&T e MSR) |
| `estrai_indice.py` | rigenera i due CSV dalla fonte |
| [`materiali/`](materiali/README.md) | quindici allegati scaricati dal forum, e le loro versioni leggibili |

I due CSV e `materiali/` vengono dallo stesso sito ma non sono la stessa cosa. I CSV
parlano delle domande **del nostro libro**: sono l'indice che al capitolo 9 non abbiamo
ancora. `materiali/` invece raccoglie materiale che con la *Official Guide* non c'entra —
esercizi di altre fonti, guide di metodo, un error log — ed è descritto nel suo
[README](materiali/README.md), file per file.

Le colonne di `og-2025-2026.csv`:

| Colonna | Da dove viene | Cos'è |
|:---|:---|:---|
| `question` | libro | il numero della domanda, 1–802, continuo su tutto il libro |
| `section` | libro | `PS` `DS` `TPA` `RC` `CR` |
| `passage` | libro | solo per `RC`: a quale brano appartiene la domanda |
| `book_difficulty` | libro | `Easy` `Medium` `Hard` — la fascia in cui il libro la stampa |
| `book_concept` | libro | l'abilità che il libro le attribuisce (`Statistics`, `Main Idea`, …) |
| `page` | libro | pagina della domanda |
| `explanation_page` | libro | pagina della spiegazione |
| `oa` | GMAT Club | la risposta esatta |
| `gmatclub_id` | GMAT Club | identificativo interno del loro archivio |
| `gmatclub_difficulty` | GMAT Club | difficoltà **misurata**: `Easy` `Medium` `Hard` `Very Hard` |
| `gmatclub_percentile` | GMAT Club | percentile di difficoltà, da 0.05 a 0.95 |
| `gmatclub_category` | GMAT Club | argomento secondo la loro tassonomia, anche più d'uno |

Le prime sette colonne sono, di fatto, il **capitolo 9** del libro — la *GMAT Official
Guide Question Index*, che nel nostro indice è ancora da fare.

## A cosa serve

**1. La lista della spesa delle scansioni.** Sapere a quale pagina sta ogni domanda e ogni
spiegazione dice esattamente quali pagine servono per ogni capitolo che manca. Il capitolo
4, che abbiamo iniziato senza scansioni su disco, sta qui:

| Capitolo | Sezione | Domande | Pagine domande | Pagine spiegazioni |
|:---|:---:|:---:|:---:|:---:|
| 4 Quantitative Reasoning | PS | 1–272 | 82–124 | 127–223 |
| 6 Data Insights | DS | 273–409 | 258–274 | 276–335 |
| 6 Data Insights | TPA | 410–466 | 337–356 | 359–398 |
| 8 Verbal Reasoning | RC | 467–612 | 434–499 | 501–588 |
| 8 Verbal Reasoning | CR | 613–802 | 590–645 | 647–841 |

**2. Una chiave di risposta indipendente.** Le sezioni *Answer Key* (4.3, 6.5, 6.8, 8.5,
8.8) si trascriveranno dalle scansioni come tutto il resto. La colonna `oa` è il secondo
paio d'occhi: se una risposta trascritta e quella del CSV divergono, si guarda la pagina.

**3. Le fasce di difficoltà del libro, per intero.** Il libro raggruppa le domande in tre
blocchi e stampa un'intestazione all'inizio di ciascuno. Servono quando si trascrive:

| Sezione | Easy | Medium | Hard |
|:---|:---|:---|:---|
| PS | 1–96 (96) | 97–176 (80) | 177–272 (96) |
| DS | 273–319 (47) | 320–362 (43) | 363–409 (47) |
| TPA | 410–427 (18) | 428–450 (23) | 451–466 (16) |
| RC | 467–508 (42) | 509–563 (55) | 564–612 (49) |
| CR | 613–672 (60) | 673–738 (66) | 739–802 (64) |

In `book/ch04.md` l'intestazione trascritta dice *«Questions 1 to 96 — Difficulty:
Easy»*, e combacia.

**4. La discussione di ogni singola domanda.** Ogni domanda ufficiale ha un thread con il
testo completo, la spiegazione ufficiale, quelle degli utenti, e le statistiche reali:
quanti rispondono giusto e in quanto tempo. Le tre che abbiamo aperto:

| Domanda | Statistiche del thread |
|:---|:---|
| 1 | 15% (low) — 83% corretto in 02:22 — su 2634 tentativi |
| 3 | 5% (low) — 97% corretto in 01:00 — su 3677 tentativi |
| 20 | 15% (low) — 83% corretto in 01:44 — su 4158 tentativi |

Serve a capire una spiegazione del libro che non torna, e ad accorgersi che una domanda
che il libro mette fra le facili in realtà non lo è.

## Come si arriva alla discussione di una domanda

`gmatclub_id` **non è un indirizzo**: è l'identificativo del loro archivio interno, non il
numero del thread. `gmatclub.com/forum/viewtopic.php?t=102001` porta a tutt'altro. Ci sono
due strade che funzionano davvero.

**Cercare una frase del testo su un motore di ricerca**, con `site:gmatclub.com`. È il
metodo che non chiede niente a nessuno, e su tre domande su tre ha trovato il thread al
primo colpo:

| Domanda | Thread |
|:---|:---|
| 1 | [in-the-graduating-class-…-129382](https://gmatclub.com/forum/in-the-graduating-class-of-a-certain-college-48-percent-of-129382.html) |
| 3 | [during-a-trip-that-they-took-together-…-268647](https://gmatclub.com/forum/during-a-trip-that-they-took-together-carmen-juan-maria-a-268647.html) |
| 20 | [from-2000-to-2003-the-number-of-employees-…-268694](https://gmatclub.com/forum/from-2000-to-2003-the-number-of-employees-at-a-certain-company-increa-268694.html) |

**Filtrare per fonte**, se si ha un account. GMAT Club tagga le domande con l'edizione da
cui vengono, e ha un tag `OG 2025-2026` diverso per ogni tipo di domanda. L'indirizzo è
sempre `https://gmatclub.com/forum/search.php?search_id=tag&tag_id=<id>`:

| Tipo | `tag_id` |
|:---:|:---:|
| PS | 2067 |
| DS | 2063 |
| TPA | 2065 |
| RC | 2062 |
| CR | 2061 |
| G&T | 2064 |
| MSR | 2066 |

Gli stessi indirizzi accettano un secondo tag per argomento o per fascia di punteggio —
`Algebra` è 50, `Probability` 54, `Work and Rate Problems` 66, la fascia `705-805` è 1533.
L'elenco completo sta in [viewforumtags.php](https://gmatclub.com/forum/viewforumtags.php),
e le [directory per tipo di domanda](https://gmatclub.com/forum/gmat-ps-question-directory-by-topic-difficulty-127957.html)
sono la stessa cosa già impaginata.

## Verificare il capitolo 4 senza le scansioni

`screens/README.md` dice che `book/ch04.md` non è verificabile, perché le scansioni del
capitolo 4 non sono su disco. GMAT Club può **coprire una parte** di quel buco, ma non
tutta, ed è importante sapere quale.

Confronto fatto su tre domande, parola per parola:

| Cosa | Esito |
|:---|:---|
| Domanda 3, testo e cinque risposte | identico al repo |
| Domanda 20, testo e cinque risposte | identico al repo |
| Domanda 1, testo | **diverso** |

La domanda 1 nel repo dice *«48 percent of the students identify exclusively as male»*; il
thread di GMAT Club dice *«48 percent of the students are male»*. Non è un errore nostro:
il thread è di un'edizione precedente, e la 2025-2026 ha riscritto quella domanda. I numeri
e le risposte coincidono, le parole no.

Da cui la regola: **GMAT Club verifica i numeri, le cinque alternative e la risposta esatta;
non verifica la prosa.** Per la prosa serve la pagina, e non c'è scorciatoia.

## Quanto ci si può fidare

I CSV sono dati di terzi, ricostruiti a mano dalla comunità. Prima di usarli sono stati
controllati così:

- **Sei domande risolte a mano** (`ch04.md` 1–6) contro la colonna `oa`: 6 su 6.
- **Coerenza interna della fonte**: il tipo di domanda si legge in due schede costruite da
  persone diverse (l'indice del libro e la scheda per sezione). Coincidono su 802 su 802 —
  se non coincidessero lo script si fermerebbe.
- **Conteggi**: 802 domande stampate, 272 PS + 137 DS + 57 TPA + 146 RC + 190 CR. I totali
  per sezione e i tre blocchi di difficoltà combaciano con quanto stampa il libro.

Restano due limiti, da tenere presenti:

- **La fonte ha qualche buco, lasciato vuoto invece che indovinato.** Dieci righe su 802
  non hanno il numero di pagina (2 in TPA, 8 in CR) e due non hanno la risposta esatta (le
  domande 295 e 406, entrambe DS). Prima di appoggiarsi a una colonna conviene controllare
  che sia piena.
- **`gmatclub_difficulty` non è `book_difficulty`, e non deve esserlo.** Coincidono nel 47%
  dei casi: 273 domande sono più facili di come il libro le classifica, 146 più difficili.
  Il libro ordina per difficoltà stimata, GMAT Club misura sugli utenti. Sono due cose
  diverse, e le teniamo tutte e due.
I CSV riportano la fonte **alla lettera**, comprese le virgolette curve che compaiono in
qualche risposta lunga di MSR. Sono dati, non prosa del libro: normalizzarli vorrebbe dire
allontanarli dalla fonte, e vale la stessa regola del §5 di [CONVENZIONI.md](../CONVENZIONI.md).

## Come si rigenera

```
pip install openpyxl
python3 gmatclub/estrai_indice.py
```

Scarica il foglio principale, ricompone le sette schede per tipo di domanda con l'indice
del libro, e riscrive i due CSV. Se la fonte cambia struttura lo script si ferma con un
errore invece di produrre un CSV sbagliato in silenzio.

**La fonte.** Il thread è
[Error Log for GMAT Official Guide 2025-2026](https://gmatclub.com/forum/error-log-for-gmat-official-guide-445984.html),
e pubblica quattro fogli: quello principale — l'unico che usiamo, perché copre l'edizione
che stiamo trascrivendo — più tre supplementi per i volumi *Quantitative Review*, *Verbal
Review* e *Data Insights Review*, che sono libri diversi con una numerazione propria.

**Una cosa da sapere se ci si torna con degli script.** GMAT Club sta dietro Cloudflare:
`curl` prende 403 e un browser headless si becca la sfida JavaScript. Le pagine del forum
si leggono una alla volta con uno strumento che renda il JavaScript. I fogli Google invece
sono pubblici e si scaricano senza problemi — ed è per questo che lo script passa da lì.

## Il resto del sito

**I forum per tipo di domanda.** Uno per tipo, ognuno con la sua directory per argomento e
fascia di punteggio. Le fasce sono sette: `Sub 505`, `505-555`, `555-605`, `605-655`,
`655-705`, `705-805`, `805+`.

| Forum | Directory per argomento e difficoltà |
|:---|:---|
| [Problem Solving](https://gmatclub.com/forum/problem-solving-ps-140/) | [directory](https://gmatclub.com/forum/gmat-ps-question-directory-by-topic-difficulty-127957.html) |
| [Data Sufficiency](https://gmatclub.com/forum/data-sufficiency-ds-141/) | [directory](https://gmatclub.com/forum/ds-question-directory-by-topic-and-difficulty-128728.html) |
| [Two-Part Analysis](https://gmatclub.com/forum/two-part-analysis-tpa-455/) | [directory](https://gmatclub.com/forum/tpa-question-directory-by-topic-and-difficulty-447185.html) |
| [Graphs and Tables](https://gmatclub.com/forum/graphs-and-tables-g-t-457/) | — |
| [Multi-Source Reasoning](https://gmatclub.com/forum/multi-source-reasoning-msr-456/) | [directory](https://gmatclub.com/forum/msr-question-directory-by-topic-and-difficulty-447183.html) |
| [Reading Comprehension](https://gmatclub.com/forum/reading-comprehension-rc-137/) | [directory](https://gmatclub.com/forum/reading-comprehension-question-directory-topic-difficulty-129341.html) |
| [Critical Reasoning](https://gmatclub.com/forum/critical-reasoning-cr-139/) | [directory](https://gmatclub.com/forum/critical-reasoning-question-directory-topic-and-difficulty-128861.html) |

La profondità è molto diversa da forum a forum: Data Sufficiency ha 18.540 discussioni,
Two-Part Analysis 833, Graphs and Tables 938, Multi-Source Reasoning appena 184. Sui tipi
nuovi del GMAT Focus la comunità ha ancora poco materiale.

Per RC ogni discussione contiene **il brano per intero** più tutte le domande che ci stanno
sopra, e i filtri sono quelli della colonna `gmatclub_category` dei nostri CSV: `Humanities`
`Science` `Social Science` `Business`, e `Short Passage` / `Long Passage`. Quando arriveremo
al capitolo 8, i 36 brani della OG si ritrovano lì.

**[GMAT Math Book](https://gmatclub.com/forum/gmat-math-book-in-downloadable-pdf-format-130609.html)** —
manuale di matematica scritto dalla comunità, gratuito, aggiornato al GMAT Focus a gennaio
2025 (`GMAT Club Math Book 2024 v8.pdf`, 2,9 MB, scaricato 48.513 volte). Copre lo stesso
terreno del nostro capitolo 3 — teoria dei numeri, valore assoluto, algebra, geometria
analitica, deviazione standard, probabilità, combinatoria, successioni, resti, insiemi,
problemi di lavoro e di velocità — con molti più esempi. Il download chiede l'account; il
file sta in [`materiali/quant/`](materiali/README.md), ed è il materiale più aggiornato
che il forum pubblichi.

**[Recensione dell'edizione 2025-2026](https://gmatclub.com/forum/gmat-official-guide-2025-2026-review-446441.html)** —
circa il 15% di domande nuove rispetto alla 2024-2025. Il foglio principale ha anche una
scheda `OG 2024-2025 Index`: se servisse, permette di confrontare le due edizioni domanda
per domanda.

**[GMAT Club Tests](https://gmatclub.com/gmat-focus-tests/)** — 12 test adattivi completi e
40 sezionali, con un archivio di oltre 50.000 domande. Un test adattivo è gratuito; il
resto è a pagamento (da 99,95 $ per tre mesi). Non c'entra con la trascrizione, ma è la
parte del sito che sta dietro alle statistiche di difficoltà che usiamo.

## Cosa chiede l'account e cosa no

L'account è gratuito. Serve sapere dove serve, perché cambia cosa si può automatizzare:

| Cosa | Account |
|:---|:---|
| Leggere una discussione, testo e spiegazioni comprese | no |
| Directory per argomento e difficoltà | no |
| I fogli dell'error log, cioè i nostri CSV | no |
| Ricerca del forum e filtri per tag, `search.php` compreso | **sì** |
| Scaricare il Math Book in PDF | **sì** |
| Test e archivio domande | **sì**, e in gran parte a pagamento |

---

[← Indice del libro](../README.md)
