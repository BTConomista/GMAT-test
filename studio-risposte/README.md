# ⚠️ Materiale di studio — NON è una fonte

> **Quello che sta in questa cartella non va usato come riferimento, né citato, né copiato
> altrove. Non è il libro. Sono risposte che ci siamo calcolati da soli.**

## Cos'è

Un tentativo di risolvere le domande del capitolo 4 ragionandoci sopra, con il percorso
logico scritto per esteso. Serve a noi, per capire come si affrontano, dove si sbaglia, e
quali tipi di domanda danno più problemi.

Nient'altro.

## Cosa NON è

**Non è la chiave delle risposte del libro.** Quella è un'altra cosa, sta altrove, ed è
l'unica che conta:

> Le risposte ufficiali vanno in **[`book/ch04.md`](../book/ch04.md), sezione 4.3 Answer
> Key**, trascritte dalle scansioni come tutto il resto del libro.

Se le due fonti si contraddicono, **ha ragione `ch04.md`**, sempre e senza discussione. Il
libro è la verità; questa cartella è un esercizio.

## Perché la distinzione è importante

Tutto il resto del repo segue una regola sola: si trascrive quello che il libro dice, e non
si corregge nemmeno quando il libro sbaglia. Ogni riga di `book/` è stata confrontata con la
scansione della pagina da cui viene.

Questo file no. **Qui dentro non c'è niente di verificato contro una fonte:** sono
conclusioni tirate fuori da un ragionamento, e un ragionamento può essere sbagliato. Mescolare
le due cose vanificherebbe il lavoro di verifica fatto su tutto il resto.

Da cui la regola:

- ✅ leggerlo per studiare, per confrontarsi, per capire un procedimento
- ❌ usarlo per riempire la sezione 4.3, per correggere `ch04.md`, o come fonte in qualunque
  altro contesto

## Come è stato prodotto

Ogni domanda è stata risolta **due volte, da due agenti indipendenti**. Il secondo non
riceveva il ragionamento del primo: risolveva da zero e solo alla fine confrontava la propria
lettera con quella dell'altro. Dove le due risposte divergono, è segnato: sono i punti in cui
fidarsi meno.

A entrambi era vietato aprire la sezione 4.3 del libro. Non è un vezzo: se avessero potuto
sbirciare la chiave, il file non misurerebbe più niente.

Ed è proprio questo che permette una **taratura**: del capitolo 4 conosciamo le risposte
ufficiali delle prime 29 domande. Confrontando le nostre con quelle, si vede quanto il metodo
azzecca — e quel numero dice quanto prendere sul serio le altre 238.

## I due file, e perché sono due

| File | Cos'è |
|:---|:---|
| `risposte-ragionate.md` | **la prova alla cieca.** Le 267 domande risolte senza sapere nulla delle risposte ufficiali |
| `risposte-tarate.md` | **la revisione.** Le stesse risposte dopo aver confrontato le prime 29 con la chiave del libro |

L'ordine non è un dettaglio, è tutto il senso dell'esercizio.

`risposte-ragionate.md` viene scritto e **congelato prima** che chiunque apra la sezione 4.3.
Una volta chiuso non si tocca più, nemmeno per correggere un errore che salta all'occhio: è
la fotografia di quanto un ragionamento autonomo azzecca, e ritoccarla a posteriori la
renderebbe una misura di niente.

Solo dopo si guarda la chiave delle 29 risposte note. Il confronto dice due cose: **quante ne
prendiamo** — un numero che si estende per stima alle altre 238 — e soprattutto **che tipo di
errori facciamo**. Il secondo è più prezioso del primo: se il metodo sbaglia sistematicamente,
per dire, le domande di probabilità condizionata, allora si sa dove andare a guardare fra le
238 di cui non conosciamo la risposta.

`risposte-tarate.md` raccoglie quel lavoro. Resta comunque materiale di studio, non una fonte:
vale l'avvertenza in cima a questa pagina.

Le domande **165–169** non ci sono in nessuno dei due: mancano anche da `book/ch04.md`, perché
le pagine che le contengono non sono mai arrivate.
