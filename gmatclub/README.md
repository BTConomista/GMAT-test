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

**4. La discussione di ogni singola domanda.** Ogni domanda ufficiale ha un thread su GMAT
Club con la spiegazione ufficiale, quelle degli utenti, e le statistiche reali: quanti
rispondono giusto e in quanto tempo. Il thread della nostra domanda 1, per esempio, dice
*«15% (low) — 83% (02:22) correct — based on 2634 sessions»*. Utile per capire una
spiegazione del libro che non torna, e per accorgersi che una domanda che il libro mette
fra le facili in realtà non lo è.

## Quanto ci si può fidare

I CSV sono dati di terzi, ricostruiti a mano dalla comunità. Prima di usarli sono stati
controllati così:

- **Sei domande risolte a mano** (`ch04.md` 1–6) contro la colonna `oa`: 6 su 6.
- **Coerenza interna della fonte**: il tipo di domanda si legge in due schede costruite da
  persone diverse (l'indice del libro e la scheda per sezione). Coincidono su 802 su 802 —
  se non coincidessero lo script si fermerebbe.
- **Conteggi**: 802 domande stampate, 272 PS + 137 DS + 57 TPA + 146 RC + 190 CR. I totali
  per sezione e i tre blocchi di difficoltà combaciano con quanto stampa il libro.

Restano tre limiti, da tenere presenti:

- **La fonte ha qualche buco, lasciato vuoto invece che indovinato.** Dieci righe su 802
  non hanno il numero di pagina (2 in TPA, 8 in CR) e due non hanno la risposta esatta (le
  domande 295 e 406, entrambe DS). Prima di appoggiarsi a una colonna conviene controllare
  che sia piena.
- **`gmatclub_difficulty` non è `book_difficulty`, e non deve esserlo.** Coincidono nel 47%
  dei casi: 273 domande sono più facili di come il libro le classifica, 146 più difficili.
  Il libro ordina per difficoltà stimata, GMAT Club misura sugli utenti. Sono due cose
  diverse, e le teniamo tutte e due.
- **`gmatclub_id` non è un indirizzo.** È l'identificativo del loro archivio interno, non
  il numero del thread: `gmatclub.com/forum/viewtopic.php?t=102001` porta a tutt'altro. Per
  arrivare alla discussione di una domanda si cerca su un motore di ricerca una frase
  presa dal testo, con `site:gmatclub.com`. La domanda 1 sta
  [qui](https://gmatclub.com/forum/in-the-graduating-class-of-a-certain-college-48-percent-of-129382.html).

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

## Il resto del sito, in breve

Cose viste esplorando, che potrebbero servire più avanti:

- **I forum per tipo di domanda** ([PS](https://gmatclub.com/forum/problem-solving-ps-140/),
  [DS](https://gmatclub.com/forum/data-sufficiency-ds-141/),
  [CR](https://gmatclub.com/forum/critical-reasoning-cr-139/),
  [RC](https://gmatclub.com/forum/reading-comprehension-rc-137/)), filtrabili per argomento
  e per fascia di punteggio (`Sub 505`, `505-555`, … `805+`).
- **Il [GMAT Math Book](https://gmatclub.com/forum/gmat-math-book-in-downloadable-pdf-format-130609.html)**,
  un manuale di matematica scritto dalla comunità e scaricabile in PDF. Copre lo stesso
  terreno del nostro capitolo 3, con più esempi.
- **La [recensione dell'edizione 2025-2026](https://gmatclub.com/forum/gmat-official-guide-2025-2026-review-446441.html)**:
  quanto è cambiato rispetto alla 2024-2025 (circa il 15% di domande nuove). Il foglio ha
  anche una scheda `OG 2024-2025 Index`, che permette di confrontare le due edizioni
  domanda per domanda.
- Test di pratica, *question of the day*, error log interattivo e calcolatore di punteggio,
  tutti dal menu **RESOURCES**.

---

[← Indice del libro](../README.md)
