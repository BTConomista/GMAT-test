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

Le pagine del libro vanno in `screens/chNN/`. Come nominarle, e perché le immagini
incollate in chat non arrivano su disco, sta in [screens/README.md](screens/README.md) —
leggilo prima di dare per scontato che una foto sia stata archiviata.

---

## 8. Punti aperti

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
- **I rimandi fra capitoli sono link solo dove il capitolo esiste.** In `ch01.md` il
  rimando a "Chapter 3" è un link a `ch03.md`; quelli a Chapter 4, 5, 6, 7 e 8 sono testo
  semplice, perché puntare a file inesistenti darebbe 404. Quando aggiungi un capitolo,
  cerca il suo nome negli altri file e attiva i rimandi.
