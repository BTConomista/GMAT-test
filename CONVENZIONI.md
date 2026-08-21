# Convenzioni e istruzioni per proseguire

Questo file è il patto di stile del repo. Se riprendi il lavoro dopo settimane, o se lo
riprende un'altra sessione, si parte da qui.

---

## 1. Cos'è questo repo

Una trascrizione fedele del *GMAT™ Official Guide 2025–2026* in Markdown, fatta a partire
dalle scansioni delle pagine del libro.

**Fedele** è la parola chiave: non si riscrive, non si migliora, non si riassume, non si
traduce. Il testo del libro è in inglese e resta in inglese. Si cambia solo il *supporto*:
da pagina stampata a Markdown.

```
README.md         indice del libro, rispecchia la Table of Contents
CONVENZIONI.md    questo file
book/             un file per capitolo: ch01.md, ch03.md, …
screens/          scansioni del libro, una sottocartella per capitolo
gmatclub/         l'indice delle 802 domande, ricavato da GMAT Club
gmatclub/materiali/  allegati del forum: esercizi, guide, flashcard, error log
```

---

## 2. Come si aggiunge del testo

1. Prendi le scansioni delle pagine (vedi [screens/README.md](screens/README.md)).
2. Trascrivi **una sezione per volta** — `3.2`, `1.4`, e così via.
3. Fai un commit per sezione (vedi §6).
4. Aggiorna l'indice in [README.md](README.md): togli il grigio, metti il link.

Un capitolo nuovo si chiama `book/chNN.md`, due cifre. Comincia con il titolo di capitolo
e il link di ritorno all'indice, e finisce con lo stesso link:

```markdown
# 4.0 Quantitative Reasoning

[← Indice del libro](../README.md)

…contenuto…

---

[← Indice del libro](../README.md)
```

---

## 3. Struttura dei titoli

Tre livelli, sempre gli stessi:

| Livello | Uso | Esempio |
|:---|:---|:---|
| `#` | capitolo | `# 3.0 Math Review` |
| `##` | sezione | `## 3.1 Value, Order, and Factors` |
| `###` | sottosezione numerata | `### 1. Numbers and the Number Line` |

Il terzo livello esiste solo dove il libro numera le sottosezioni — nel capitolo 3. Nel
capitolo 1 si arriva a `##` e basta.

**Non cambiare il testo di un titolo.** Gli ancoraggi dei link di GitHub si generano dal
testo del titolo: se lo modifichi, ogni link dell'indice che punta lì si rompe in
silenzio. L'ancora si ricava così: tutto minuscolo, via la punteggiatura, spazi in
trattini. `## 3.1 Value, Order, and Factors` → `#31-value-order-and-factors`.

---

## 4. Convenzioni del testo

### Paragrafi con lettera

Nel capitolo 3 ogni punto del libro è un paragrafo marcato con una lettera in grassetto,
e i paragrafi sono separati da una riga `---`:

```markdown
**A.** All ***real numbers*** match points on ***the number line***, and all points…

---

**B.** On the number line, points to the left of zero stand for ***negative*** numbers…
```

Un paragrafo = una riga fisica, per quanto lunga. Non si va a capo a mano.

### Termini definiti

Grassetto corsivo (`***così***`), **solo** dove il libro definisce il termine per la prima
volta. Nelle occorrenze successive è testo normale.

```markdown
An ***integer*** is any number in the set…
```

### Esempi

Citazione (`>`) che apre con l'etichetta in corsivo, riga `>` vuota, poi il contenuto.
Ogni riga dell'esempio è prefissata da `>`, comprese quelle vuote, altrimenti GitHub
spezza il riquadro in due.

```markdown
> *Example:*
>
> Since $28 = (7)(4)$, both 4 and 7 are divisors or factors of 28.
```

`*Example:*` se ce n'è uno, `*Examples:*` se più d'uno. Quando il libro numera gli
esempi si usa `i.` `ii.` `iii.` dentro il riquadro. La soluzione di un problema si
introduce con `*Solution:*` in linea.

### Matematica

LaTeX, che GitHub rende in modo nativo.

| Cosa | Come |
|:---|:---|
| in linea nel testo | `$x^2 + 1$` |
| formula isolata | `$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$` |
| frazione **in linea** | `\dfrac` — resta leggibile a corpo testo |
| frazione **isolata** | `\frac` |
| catena di passaggi | `$$\begin{aligned} … \\ … \end{aligned}$$` |
| separatore di migliaia | `1{,}000` dentro la matematica, `1,000` in prosa |

I numeri e i simboli citati nella prosa vanno dentro `$…$`, non lasciati in testo nudo:
si scrive `$5 \times 9 = 45$`, non `5 × 9 = 45`.

### Figure

Il libro ha figure che il Markdown non può riprodurre. Si ricostruiscono così: titolo in
grassetto su riga propria, poi il disegno in un blocco di codice, poi una didascalia in
citazione che descrive a parole quello che il disegno mostra.

````markdown
**The Coordinate Plane**

```
        y
        |
--------+-------→ x
```

> Quadrant I: $x > 0$, $y > 0$ — Quadrant II: $x < 0$, $y > 0$
````

La didascalia non è decorativa: è lì perché chi legge con uno screen reader, o su un
terminale, deve poter capire la figura senza vederla.

### Tabelle

Tabelle GFM, colonne centrate (`:---:`) salvo la prima colonna di etichette, che va a
sinistra (`:---`). Se una cella deve contenere più righe si usa `<br>`.

### Caratteri

ASCII, con due sole eccezioni: i trattini tipografici nella prosa (`—`, `–`) e i simboli
dentro i disegni ASCII (`→`, `●`, `∩`). Virgolette **dritte** (`"`), mai curve. Il simbolo
`™` si riproduce dove il libro ce l'ha.

---

## 5. La regola che conta più di tutte: i refusi del libro non si correggono

Se il libro sbaglia, **il repo sbaglia uguale**. Questa è una trascrizione, non
un'edizione critica.

Esempio vero, in `3.1` §2 D: il libro scrive

> When 142 is divided by 13, the remainder is 12 because 132 = (13 × 10) + 12.

Quel `132` è un refuso: dovrebbe essere `142`. Il repo lo riporta com'è ed **è giusto
così**. Chi lo "aggiusta" sta introducendo una divergenza dalla fonte.

Se trovi qualcosa che sembra un errore: non toccarlo, segnalalo. Al massimo si annota qui
sotto, in §8.

---

## 6. Git

- **Si lavora solo sul branch `claude/check`.** Non se ne creano altri, non si pusha
  altrove. `claude/check` è anche il branch di default del repo.
- Un commit per sezione trascritta, non uno per capitolo: se qualcosa va storto si torna
  indietro di poco.
- Messaggi in inglese, all'imperativo, nella forma già usata nella storia del repo:

```
Add section 3 (Percents) to ch03.md
Add chapter 3.4 section 1 (Statistics) to ch03.md
```

---

## 7. Le scansioni

Le pagine del libro stanno in `screens/`, organizzate per capitolo e sezione, con un
numero progressivo continuo (001–074) che segue l'ordine di lettura. Lo schema dei nomi e
lo stato della copertura sono in [screens/README.md](screens/README.md).

Due cose da sapere prima di fidarsi:

- **Le immagini incollate in chat non arrivano su disco.** Arrivano nel contesto del
  modello come contenuto del messaggio, non come file. Per archiviarle davvero servono i
  file veri, allegati o messi a mano nella cartella.
- **Un nome che salta una sezione non significa che la sezione manchi.** Quando una
  pagina ne copre tre, il nome cita solo la prima e l'ultima.

---

## 8. Verifiche già fatte

Traccia di cosa è già stato controllato contro le scansioni, per non rifare due volte lo
stesso lavoro. Chi verifica una sezione la aggiunge qui.

| Sezione | Confrontata con | Esito |
|:---|:---|:---|
| 3.1 (tutte e cinque le sottosezioni) | scansioni delle pagine 3.1 | ✅ nessuno scostamento di contenuto |
| 3.2 (tutte e sette le sottosezioni) | scansioni delle pagine 3.2 | 🔧 2 scostamenti trovati e corretti |
| 3.3 (per intero, §1–§6) | scansioni delle pagine 3.3 | 🔧 5 scostamenti trovati e corretti |
| 3.4 (per intero, §1–§6) | scansioni delle pagine 3.4 | 🔧 5 scostamenti trovati e corretti |
| 3.5 (per intero, 7 fogli) | scansioni a pagina intera delle pagine 3.5 | ✅ nessuno scostamento |

Sul metodo: il confronto è stato fatto paragrafo per paragrafo (A, B, C, …) più un diff
parola per parola su testo normalizzato — sciogliendo il LaTeX in notazione piana, così le
differenze di sola resa non producono falsi positivi. Verificati uno a uno anche i valori
numerici, i termini marcati come definiti e l'ordine degli esempi.

Due cose emerse, entrambe **corrette così come stanno**, perché il libro dice esattamente
questo:

- `3.1` §2 D — `132 = (13 × 10) + 12`, dove il senso vorrebbe `142` (vedi §5).
- `3.1` §5 B — il libro scrive `final 2 digits` parlando di 180 e `final two digits`
  parlando di 121, nello stesso elenco. L'incoerenza è sua, non nostra.
- `3.2` §3 G — nella catena di passaggi il libro scrive `3x − 5 = 0 or x + 5 = 0`, dove il
  senso vorrebbe `3x + 5 = 0`. Refuso suo: il repo lo riproduce.
- `3.4` §4 E — nella frazione `{6}/|{2, 4, 6}|` il libro omette le barre di cardinalità al
  numeratore, pur mettendole nella frazione gemella subito sopra. Asimmetria sua.
- `3.4` §4 G — «Since $A \cap B$ is a subset of $A$», dove il ragionamento richiede
  $A \cap C$. Refuso suo.
- `3.4` §6 A — definendo la sequenza **geometrica**, il libro scrive «The first term of an
  *arithmetic* sequence is $a_1 = bc$». Refuso suo, e istruttivo: la trascrizione l'aveva
  corretto in «geometric», ed è stato necessario **rimetterlo sbagliato**.

Gli scostamenti trovati erano invece nostri, e sono stati corretti: in `3.2` §4 B la
trascrizione aveva **aggiunto** le parole `, reversing the inequality` a un'annotazione che
nel libro dice solo `(multiply both sides by -2)`; in `3.2` §6 G aveva `the equation` invece
di `this equation`; in `3.3` §2 H l'esempio aveva perso l'incipit `The mixed number`.

In `3.3` §6 B la trascrizione abbreviava in `km` le quattro frazioni dell'esempio del viaggio
di 600 km, dove il libro scrive `kilometers` per esteso. Vale la pena ricordarlo come regola:
**le unità di misura si riportano come le scrive il libro.** Abbreviare è riscrivere, anche
quando il significato non cambia.

### Il libro non è coerente con sé stesso, e va bene così

La `3.5` è la scheda riassuntiva di quello che `3.1`–`3.4` spiegano per esteso, e in più punti
**dice una cosa diversa**. Non è un errore di trascrizione: è il libro. Le due versioni vanno
riprodotte entrambe come stanno, senza armonizzarle.

| Punto | In `3.5` | In `3.1`–`3.2` |
|:---|:---|:---|
| Disuguaglianza triangolare | `\|x+y\| < \|x\|+\|y\|` (stretta) | `≤` (larga) |
| Resto della divisione | `0 < r < x` | `0 ≤ r < x` |
| Ruoli di $x$ e $y$ nel quoziente | «dividing $x$ by $y$», poi `y = xq + r` | «dividing $y$ by $x$» |
| Sottrazione | `x − y = −(y−x) = −y + x` | `… = x + (−y)` |
| Radici della quadratica | «distinte se `b²−4ac ≥ 0`» | «unless `b²−4ac ≤ 0`» |
| Passo 2 della deviazione standard | «differences between each of the $n$ values and the mean» | «between the mean and each of the $n$ values» |

Quella sulle radici si contraddice **dentro lo stesso riquadro**: due righe dopo aver detto
`≥ 0`, il libro spiega che con `= 0` la radice è una sola. Va lasciata così.

Nota di metodo: la `3.5` è stata trascritta da scansioni in cui alcune pagine erano tagliate a
metà, e poi riverificata su una seconda serie a pagina intera. Il controllo è partito dai
**conteggi** — quante righe ha ogni tabella nella fonte, quante nel repo — prima di leggere
alcunché: è il modo più affidabile per accorgersi che una riga è caduta sul salto di pagina.
Tutti i totali coincidevano.

### Un errore da non ripetere

In `3.4` §2 G il libro compone «*empty set*» in corsivo semplice, mentre tutti i termini
definiti dei paragrafi vicini sono in grassetto corsivo. Una revisione di formattazione,
guardando solo la coerenza interna del file, ha concluso che fosse una svista e l'ha
«uniformato» a `***empty set***`. Il confronto con le scansioni ha poi mostrato che il corsivo
semplice era quello giusto: l'incoerenza era del libro, e andava conservata.

La lezione vale in generale: **la coerenza interna del file non è una prova.** Quando una
convenzione risulta violata in un punto solo, le spiegazioni sono due — è una svista nostra,
oppure è così nel libro — e il file da solo non permette di distinguerle. Senza la pagina
sottomano, si segnala e si aspetta; non si uniforma.

---

## 9. Punti aperti

Cose sospese, da decidere o da verificare. Chi le risolve le cancella da qui.

- **3.5 Reference Sheets non è trascritta.** È l'ultima sezione del capitolo 3, ed è
  l'unico buco rimasto in quel capitolo. Servono le scansioni.
- **La figura "The Number Line" è resa in modo diverso dalle altre due.** Usa un blocco
  `$$…$$` con frecce LaTeX, mentre "The Coordinate Plane" e "A Venn Diagram of Two
  Intersecting Sets" usano un blocco di codice con disegno ASCII. Da uniformare — ma
  significa ridisegnare la figura, quindi è una scelta da fare, non una svista da correggere
  di nascosto.
- **Il bullet delle proprietà aritmetiche.** In `3.1` §5 C i tre gruppi di formule sono
  introdotti da `**· Addition and Subtraction**` con un punto mediano (`·`, U+00B7). Nel
  libro il carattere è un vero bullet (`•`). Da decidere se allinearsi al libro o
  trasformarli in un elenco Markdown vero.
- **La numerazione del capitolo 5 va confermata.** Dall'indice fotografato risulta che
  `5.0 Data Insights Review` arrivi fino a `5.3 Data Patterns`, ma quella voce cade
  esattamente sul taglio fra due schermate: se esistessero `5.4` o `5.5` non si
  vedrebbero. Da verificare sull'indice vero prima di trascrivere il capitolo 5.
- **Dove sta «LINES IN THE COORDINATE PLANE».** Nel libro quel riquadro non ha sopra di sé un
  titolo di foglio centrato: compare dopo `SOLVING INEQUALITIES` e prima del foglio *Rates,
  Ratios, and Percents*. Dalle scansioni non si stabilisce se appartenga al foglio *Factoring,
  Quadratic Equations, and Inequalities* o se sia un foglio a sé. Nel repo sta sotto il primo.
  Da confermare su una copia cartacea, dove l'impaginazione è più leggibile.
- **I rimandi fra capitoli sono link solo dove il capitolo esiste.** In `ch01.md` il
  rimando a "Chapter 3" è un link a `ch03.md`; quelli a Chapter 4, 5, 6, 7 e 8 sono testo
  semplice, perché puntare a file inesistenti darebbe 404. Quando aggiungi un capitolo,
  cerca il suo nome negli altri file e attiva i rimandi.
