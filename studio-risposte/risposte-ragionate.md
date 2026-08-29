# Risposte ragionate — prova alla cieca

> ⚠️ **Materiale di studio, non una fonte.** Le risposte ufficiali stanno in
> [`book/ch04.md`](../book/ch04.md) §4.3. Dove le due si contraddicono, ha ragione `ch04.md`.
> Vedi [README.md](README.md).

## Come è stato prodotto

Le 267 domande del capitolo 4 risolte **senza vedere nessuna risposta ufficiale**. Agli agenti
era vietato aprire la sezione 4.3 del libro, che contiene la chiave delle prime 29.

Ogni blocco è stato risolto **due volte, da due agenti indipendenti**. Il secondo non riceveva
il ragionamento del primo: risolveva da zero e confrontava solo alla fine la propria lettera.

**Questo file è congelato.** È stato scritto prima che chiunque aprisse la chiave, e non viene
più modificato — nemmeno dove il confronto successivo mostra un errore. Correggerlo a
posteriori lo trasformerebbe nella fotografia di un ragionamento che ha già visto le risposte,
cioè in una misura di niente. Le correzioni vivono in `risposte-tarate.md`.

Le domande **165–169** non compaiono: mancano anche da `book/ch04.md`.

## Legenda

La **confidenza** è dichiarata dall'agente che ha risolto:

- **alta** — calcolo verificato, il risultato coincide esattamente con un'opzione
- **media** — il ragionamento regge ma l'enunciato è ambiguo o ha richiesto un'interpretazione
- **bassa** — non convinto, o scelta per esclusione senza risolvere davvero

---

### 1 → **B**

Probabilità di avere 25 anni o più = 0,48·0,40 + 0,52·0,20 = 0,192 + 0,104 = 0,296. Quindi P(meno di 25 anni) = 1 − 0,296 = 0,704, cioè circa 0,70.

<sub>confidenza: alta</sub>

### 2 → **E**

Se le prime 2 carte estratte non sono azioni, restano 46 carte di cui ancora tutte le 8 che rappresentano azioni. La probabilità che la terza sia un'azione è 8/46 = 4/23.

<sub>confidenza: alta</sub>

### 3 → **D**

Totale miglia = 4 × 80 = 320. Carmen+Juan+Maria = 72+78+83 = 233. Rafael = 320 − 233 = 87.

<sub>confidenza: alta</sub>

### 4 → **C**

Commissione = 15% di 500 = 75, più 20% dei restanti 1300 − 500 = 800, cioè 160. Totale 75 + 160 = 235 dollari.

<sub>confidenza: alta</sub>

### 5 → **D**

Con quinto valore 1: lista 1,2,3,4,5 → media 15/5 = 3, mediana 3 (uguali, I vale). Con 2: 2,2,3,4,5 → media 16/5 = 3,2, mediana 3 (diversi, II non vale). Con 6: 2,3,4,5,6 → media 20/5 = 4, mediana 4 (uguali, III vale). Quindi I e III soltanto.

<sub>confidenza: alta</sub>

### 6 → **D**

Se il minimo di S è a (dispari), S = a, a+2, …, a+18 e la media è il valore centrale a+9. Se il minimo di T è b (pari), T = b, b+2, …, b+8 con media b+4. Dato a = b+7, la differenza è (a+9) − (b+4) = (b+16) − (b+4) = 12.

<sub>confidenza: alta</sub>

### 7 → **E**

I valori della tabella sono 5, 4, 3, 4, 2; ordinati: 2, 3, 4, 4, 5, quindi la mediana (terzo valore) è 4. Nota: l'enunciato del libro parla di 'carts' mentre la tabella riporta 'Number in line' (refuso), ma i dati numerici sono quelli usati.

<sub>confidenza: alta</sub>

### 8 → **C**

La somma è telescopica: tutti i termini intermedi (1/3, 1/4, 1/5) si cancellano e resta 1/2 − 1/6 = 3/6 − 1/6 = 2/6 = 1/3.

<sub>confidenza: alta</sub>

### 9 → **A**

Dalla retta numerica: p < −1 < q < r < 0 < s < 1. I prodotti qs e rs sono negativi (scartati); qr è positivo ma prodotto di due numeri di modulo minore di 1, quindi piccolo; pq e pr sono positivi con |p| > 1. Poiché q è più a sinistra di r, |q| > |r|, quindi pq = |p||q| > |p||r| = pr. Il maggiore è pq.

<sub>confidenza: alta</sub>

### 10 → **B**

Sia e la quota di ogni dipendente: 2 proprietari ricevono 3e ciascuno, quindi 2·3e + 10·e = 16e = 48.000, da cui e = 3.000 e ogni proprietario riceve 3e = 9.000 dollari.

<sub>confidenza: alta</sub>

### 11 → **D**

500 × 0,80 = 400 euro ricevuti; ne spende 3/4, quindi ne restano 400/4 = 100 euro. Ricambiati a 1,20 dollari per euro: 100 × 1,20 = 120 dollari.

<sub>confidenza: alta</sub>

### 12 → **E**

Conteggio dalla figura: x compare 3 volte in alto e 2 in basso = 5; y compare 2 in alto e 1 in basso = 3; quindi x o y = 8. v compare 1 in alto e 1 in basso = 2; w compare 2 volte in basso = 2; quindi v o w = 4. Rapporto 8:4 = 2:1.

<sub>confidenza: alta</sub>

### 13 → **D**

Dalla tabella: x+y = 80, y+z = 120, x+z = 160. Sommando: 2(x+y+z) = 360, quindi x+y+z = 180. Le biglie verdi in R sono z = 180 − (x+y) = 180 − 80 = 100.

<sub>confidenza: alta</sub>

### 14 → **B**

Per usare tutti i tulipani con lo stesso rapporto in ogni bouquet, il numero di bouquet deve dividere sia 15 sia 85; il massimo è MCD(15,85) = 5 (ogni bouquet: 3 bianchi e 17 rossi).

<sub>confidenza: alta</sub>

### 15 → **C**

Rapporti smaltito/riciclato: A 142.800/16.700 ≈ 8,55; B 48.000/8.800 ≈ 5,45; C 51.400/13.000 ≈ 3,95; D 20.300/3.900 ≈ 5,21; E 16.200/3.300 ≈ 4,91. Il più basso è quello della contea C.

<sub>confidenza: alta</sub>

### 16 → **E**

125% di 5 = 1,25 × 5 = 6,25.

<sub>confidenza: alta</sub>

### 17 → **E**

Paga giornaliera = 6 × 15 = 90 dollari; tempo totale (lavoro + spostamenti) = 6 + 1,5 = 7,5 ore. Tariffa oraria complessiva = 90/7,5 = 12 dollari l'ora.

<sub>confidenza: alta</sub>

### 18 → **D**

Miglia per gallone = (miglia/ora) ÷ (galloni/ora) = 32/24 = 4/3.

<sub>confidenza: alta</sub>

### 19 → **E**

30 mm in 1 ora = 30 mm in 3.600 secondi, quindi 1 mm richiede 3.600/30 = 120 secondi.

<sub>confidenza: alta</sub>

### 20 → **B**

'Aumentato di un fattore 1/4' significa moltiplicato per 1+1/4 = 5/4; 'diminuito di un fattore 1/3' significa moltiplicato per 1−1/3 = 2/3. Se N è il numero nel 2000: N·(5/4)·(2/3) = N·5/6 = 100, quindi N = 120. La formulazione 'by a factor of' è ambigua nel libro, ma solo questa lettura dà un'opzione presente.

<sub>confidenza: alta</sub>

### 21 → **C**

Tasso di R = 10.000/9 ≈ 1111,1 scatole/ora; tasso di S = 5.000/3 = 15.000/9 ≈ 1666,7 scatole/ora. Lavorando per lo stesso tempo t, le quote sono proporzionali ai tassi: R/(R+S) = (10000/9)/((10000/9)+(15000/9)) = 10000/25000 = 2/5 = 40%. Verificato con Fraction: 2/5.

<sub>confidenza: alta</sub>

### 22 → **B**

Sia b il numero di monete da 25 cent e 16-b quelle da 10 cent: 10(16-b) + 25b = 235 → 160 + 15b = 235 → 15b = 75 → b = 5. Controllo: 5 monete da 25 = 125 cent, 11 da 10 = 110 cent, totale 235 cent = $2,35.

<sub>confidenza: alta</sub>

### 23 → **C**

Costo di 5 dozzine = 5 × $2,80 = $14,00. 5 dozzine = 60 uova, vendute a 3 per $0,90 → 60/3 = 20 gruppi × $0,90 = $18,00 di ricavo. Profitto lordo = 18,00 − 14,00 = $4,00.

<sub>confidenza: alta</sub>

### 24 → **C**

Divisibile sia per 2 sia per 3 significa divisibile per 6: {6, 12, 18, 24} = 4 carte. Divisibile per 7: {7, 14, 21} = 3 carte. I due insiemi sono disgiunti (il primo multiplo comune sarebbe 42 > 24), quindi 4 + 3 = 7 casi favorevoli su 24: probabilità 7/24.

<sub>confidenza: alta</sub>

### 25 → **C**

Uguaglio i due compensi: 35.000 = 10.000 + 0,20·S → 0,20·S = 25.000 → S = 125.000. Verifica: 20% di $125.000 = $25.000, più $10.000 di stipendio = $35.000.

<sub>confidenza: alta</sub>

### 26 → **E**

Con 1 < x < y < z confronto E = z(x+y) = zx + zy con le altre. E vs B: B = zy + z e zx > z perché x > 1, quindi E > B > A (y > x). E vs D: E − D = (zx+zy) − (yx+yz) = x(z−y) > 0. E vs C: E − C = (zx+zy) − (xy+xz) = y(z−x) > 0. Quindi E è sempre il maggiore.

<sub>confidenza: alta</sub>

### 27 → **C**

Sia X = {n, ..., n+7} (8 interi). Aggiungendo 4 si ottiene {n+4, ..., n+11}; sottraendo 4 si ottiene {n−4, ..., n+3}. I due blocchi sono contigui ma disgiunti, quindi Y = {n−4, ..., n+11} contiene 16 interi distinti. 16 − 8 = 8 interi in più.

<sub>confidenza: alta</sub>

### 28 → **B**

Denominatore: 1,03 × 4,86 = 5,0058. Quoziente: 60,2/5,0058 = 12,026 (calcolo python3). L'opzione più vicina è 12.

<sub>confidenza: alta</sub>

### 29 → **B**

Sia h = hardcover nonfiction; paperback nonfiction = h + 20; paperback fiction = 2(h + 20). Totale: h + (h+20) + (2h+40) = 4h + 60 = 140 → 4h = 80 → h = 20. Verifica: 20 + 40 + 80 = 140.

<sub>confidenza: alta</sub>

### 30 → **B**

Somma: 1,4 + 1/5 = 1,4 + 0,2 = 1,6. Il 35% di 1,6 = 0,35 × 1,6 = 0,56.

<sub>confidenza: alta</sub>

### 31 → **A**

x/50 + x/25 = x/50 + 2x/50 = 3x/50 = 0,06x. Poiché 0,06x = 6% di x, la risposta è 6%.

<sub>confidenza: alta</sub>

### 32 → **E**

Consumo: 5 galloni ogni 2 ore = 2,5 galloni/ora. Con 3,75 galloni: 3,75/2,5 = 1,5 ore = 90 minuti. Alla velocità di 1 miglio al minuto, 90 minuti = 90 miglia.

<sub>confidenza: alta</sub>

### 33 → **A**

Il denominatore 100 + 1/999 ≈ 100,001, praticamente 100. Quindi 999/100,001 ≈ 9,9899 (calcolo python3), che è vicinissimo a 10.

<sub>confidenza: alta</sub>

### 34 → **B**

Sia Y la popolazione di City Y, allora X = 0,5Y. Totale = X + Y = 1,5Y. Rapporto: 0,5Y/1,5Y = 1/3 = 33 1/3%.

<sub>confidenza: alta</sub>

### 35 → **E**

Costo totale = 250 + 375 = 625; con profitto lordo totale 250 il ricavo totale è 875. Se una bici è venduta a 450, l'altra è venduta a 875 − 450 = 425. Caso 1: la bici a 450 è quella da $250 → l'altra (costo 375) dà profitto 425 − 375 = 50 (non tra le opzioni). Caso 2: la bici a 450 è quella da $375 → l'altra (costo 250) dà profitto 425 − 250 = 175, che è l'opzione E. (L'opzione A $75 è la trappola: è il profitto della bici venduta a 450 nel caso 2.)

<sub>confidenza: alta</sub>

### 36 → **E**

k² = m² implica k = m oppure k = −m, quindi nessuna delle due singole uguaglianze è obbligatoria (es. k=2, m=−2 smentisce A e C; k=2, m=2 smentisce B e D). L'unica conseguenza sempre vera è |k| = |m|, poiché √(k²) = |k| e √(m²) = |m|.

<sub>confidenza: alta</sub>

### 37 → **D**

Ore totali = 15 + 20 + 30 = 65. Quota di Makoto = 15/65 = 3/13 del totale. Pagamento = (3/13) × 780 = 180 (verificato con Fraction).

<sub>confidenza: alta</sub>

### 38 → **B**

Per x = 1, 2, 3, 4 si ottiene y = 4^x − 3 = 1, 13, 61, 253 (calcolo python3), che coprono le opzioni A, C, D, E. Il valore 7 richiederebbe 4^x = 10, impossibile per x intero positivo, quindi 7 non può essere un valore di y.

<sub>confidenza: alta</sub>

### 39 → **D**

Prezzo scontato per lattina = 0,40 × (1 − 0,15) = $0,34. 72 lattine = 3 confezioni da 24, quindi tutte scontate: 72 × 0,34 = $24,48.

<sub>confidenza: alta</sub>

### 40 → **C**

Sia n il numero: n ÷ (2/3) = 9/2 → n = (9/2) × (2/3) = 18/6 = 3. Verifica: 3 ÷ (2/3) = 3 × 3/2 = 9/2.

<sub>confidenza: alta</sub>

### 41 → **D**

La quantità di benzina comprata la scorsa settimana è 26.40/1.65 = 16 galloni. Questa settimana gli stessi 16 galloni costano 16 × 1.82 = $29.12. La differenza è 29.12 − 26.40 = $2.72. In alternativa: 16 × (1.82 − 1.65) = 16 × 0.17 = 2.72.

<sub>confidenza: alta</sub>

### 42 → **B**

Affitto = 25% di 2,200 = $550, quindi il resto è 2,200 − 550 = $1,650. Il cibo è il 30% del resto: 0.30 × 1,650 = $495. (Attenzione alla trappola A/D: 165 è il 30% di 550 e 660 è il 30% dell'intero stipendio.)

<sub>confidenza: alta</sub>

### 43 → **B**

Sommando le due equazioni: (2x+y) + (x+2y) = 7 + 5, cioè 3x + 3y = 12, da cui x + y = 4. Quindi (x+y)/3 = 4/3.

<sub>confidenza: alta</sub>

### 44 → **E**

Sia Z = z. Allora Y = 2z e X = 4Y = 8z. Il rapporto X:Z = 8z:z = 8:1.

<sub>confidenza: alta</sub>

### 45 → **B**

Totale membri = 78 + 9,209 + 35,509 + 27,909 + 2,372 = 75,077. La percentuale dei fellows è 9,209/75,077 = 0.12266, cioè circa 12.3%. L'opzione più vicina è 12%.

<sub>confidenza: alta</sub>

### 46 → **E**

Calcolo diretto con python3: S = 1 + 1/4 + 1/9 + ... + 1/100 = 1.54977. Quindi S < 2. Anche a stima: i termini dopo il primo sono 0.25, 0.111, 0.0625, 0.04, 0.0278, 0.0204, 0.0156, 0.0123, 0.01, la cui somma è circa 0.55, quindi S ≈ 1.55 < 2.

<sub>confidenza: alta</sub>

### 47 → **D**

Le unità difettose su 20,000 vanno da 0.003 × 20,000 = 60 a 0.005 × 20,000 = 100. Il rimborso pieno è $2,500 per unità, quindi il costo va da 60 × 2,500 = $150,000 a 100 × 2,500 = $250,000.

<sub>confidenza: alta</sub>

### 48 → **A**

La resa LaTeX del libro sembra imprecisa: presa alla lettera, √(4.2 × 1,590)/15.7 = √6,678/15.7 = 81.72/15.7 ≈ 5.21, valore che tra le opzioni date ha come più vicino comunque 20. Con la lettura probabilmente intesa, √(4.2 × 1,590 / 15.7) = √425.4 ≈ 20.6, di nuovo vicinissimo a 20. Entrambe le interpretazioni portano ad A.

<sub>confidenza: **media**</sub>

### 49 → **B**

√17 ≈ 4.123 (tra 4 e 4.25 perché 4.1² = 16.81) e √47 ≈ 6.856 (tra 6.8 e 6.9 perché 6.86² ≈ 47.06). La somma è 10.979, che arrotondata all'intero più vicino è 11.

<sub>confidenza: alta</sub>

### 50 → **D**

Le ore oltre le 40 sono 48 − 40 = 8, pagate 22 $/h: 8 × 22 = $176. Restano 816 − 176 = $640 per le prime 40 ore, quindi x = 640/40 = 16.

<sub>confidenza: alta</sub>

### 51 → **A**

7/8 + 1/9 = 63/72 + 8/72 = 71/72 ≈ 0.9861. Dividere per 1/2 equivale a moltiplicare per 2: 71/36 ≈ 1.972, valore più vicino a 2.

<sub>confidenza: alta</sub>

### 52 → **D**

Se x = 10a + b, allora y = 10b + a, quindi x + y = 11a + 11b = 11(a+b): 11 è sempre un fattore. Gli altri no: con a=1, b=2 si ha x+y = 33, che non è divisibile per 6, 9, 10 né 14.

<sub>confidenza: alta</sub>

### 53 → **C**

La successione parte da −5 e cresce di 1: −5, −4, −3, −2, −1, 0, 1, 2 (8 termini). Gli unici positivi sono 1 e 2 (lo zero non è positivo), quindi due.

<sub>confidenza: alta</sub>

### 54 → **E**

Il numero totale di scatole necessarie è s/r (divisione esatta, nessuna arancia avanza). Se n sono già piene, ne restano da riempire s/r − n.

<sub>confidenza: alta</sub>

### 55 → **B**

I: 2a > b + c è falsa, perché a < b e a < c implicano 2a < b + c. II: c − a > b − a equivale a c > b, vera per ipotesi. III: c/a < b/a, essendo a > 0, equivale a c < b, falsa. Quindi solo II.

<sub>confidenza: alta</sub>

### 56 → **B**

Le deviazioni standard (di popolazione) calcolate con python3 sono: A = 3.54, B = 10.0, C = 2.45, D = 1.58, E = 7.07. B ha i valori 10, 30, 30, 10 con media 20 e scarti tutti di 10, la dispersione maggiore in assoluto; E oscilla tra 50 e 70 con media 60 ma con scarti minori. Quindi B.

<sub>confidenza: alta</sub>

### 57 → **A**

Costo variabile per unità = 40% di $2 = $0.80, quindi il margine di contribuzione è 2 − 0.80 = $1.20 per unità. Il pareggio richiede 5,040/1.20 = 4,200 unità.

<sub>confidenza: alta</sub>

### 58 → **D**

Il profitto per unità è 1.20 − 0.65 = $0.55. Per coprire l'investimento iniziale di $9,900 servono 9,900/0.55 = 18,000 unità. Verifica: 18,000 × 1.20 = 21,600 = 9,900 + 18,000 × 0.65 = 9,900 + 11,700.

<sub>confidenza: alta</sub>

### 59 → **D**

L'aumento percentuale si calcola sulla base D: (181 − 79)/79 = 102/79 = 1.291, cioè circa 129% in più. L'opzione più vicina è 125%. (Attenzione: 181/79 ≈ 229% è il rapporto, non l'eccedenza.)

<sub>confidenza: alta</sub>

### 60 → **D**

Sia C la capacità: n = (7/9)C − (1/3)C = (7/9 − 3/9)C = (4/9)C. Quindi C = (9/4)n = 2.25n.

<sub>confidenza: alta</sub>

### 61 → **B**

Somma algebrica delle 5 variazioni: -280 +350 -620 +100 -400 = -850 metri. Partendo da 850 m sopra Town X, l'arrivo e' a 850 - 850 = 0 m rispetto a Town X, cioe' alla stessa quota di Town X.

<sub>confidenza: alta</sub>

### 62 → **A**

Gli x alberi producono complessivamente 10x bushel su un raccolto totale di 350. La frazione richiesta e' 10x/350 = x/35. Le opzioni C, D, E sono quantita' assolute, non frazioni; B sarebbe la parte NON prodotta dagli x alberi.

<sub>confidenza: alta</sub>

### 63 → **D**

Sia n il numeratore: n/(n+16) = 0,80 → n = 0,8n + 12,8 → 0,2n = 12,8 → n = 64. Il denominatore e' 64 + 16 = 80 (verifica: 64/80 = 0,8). Attenzione alla trappola B, che e' il numeratore.

<sub>confidenza: alta</sub>

### 64 → **D**

La quota di affitto di Jonathan e' 525 - 250 (deposito una tantum) = 275 dollari. Poiche' i tre pagano quote uguali, l'affitto mensile totale e' 3 x 275 = 825 dollari.

<sub>confidenza: alta</sub>

### 65 → **A**

Sia J la bolletta di gennaio: F = (3/2)J. Con 40 dollari in piu': (1,5J + 40)/J = 5/3 → 40 = (5/3 - 3/2)J = J/6 → J = 240. Verifica: F = 360, (360+40)/240 = 400/240 = 5/3.

<sub>confidenza: alta</sub>

### 66 → **B**

Sia t l'ora del rilevamento: Ben ha guidato (t-8) ore a 20 mph, Al (t-11) ore a 40 mph. 20(t-8) + 40(t-11) = 240 → 60t - 600 = 240 → 60t = 840 → t = 14, cioe' le 2:00 p.m. Verifica: Ben 6 h x 20 = 120 mi, Al 3 h x 40 = 120 mi, totale 240 mi.

<sub>confidenza: alta</sub>

### 67 → **B**

Con s = 2.000 si ha s/1.000 = 2, quindi (s/1.000)^2 = 4 e f = 3r x 4 = 12r. Risolvendo per r: r = f/12.

<sub>confidenza: alta</sub>

### 68 → **D**

La popolazione parte da 3 e raddoppia alla fine di ogni mese: dopo n mesi vale 3 x 2^n. Per n = 10 si ottiene 3(2^10) = 3.072.

<sub>confidenza: alta</sub>

### 69 → **C**

Il testo ha un refuso di resa: 9/(5C) va letto come (9/5)C, la formula standard F = (9/5)C + 32. Da 85 = 1,8C + 32 segue C = 53/1,8 = 29,44..., che arrotondato e' 29 gradi Celsius.

<sub>confidenza: **media**</sub>

### 70 → **E**

Poniamo y = 5k: 3x = 200 - 20k, quindi 200 - 20k deve essere divisibile per 3, cioe' 2 - 2k ≡ 0 (mod 3) → k ≡ 1 (mod 3). Per k = 1, 4, 7 si ottengono rispettivamente x = 60, 40, 20 (k = 10 darebbe x = 0, non positivo). Tutti e tre sono multipli di 10, mentre 3, 6, 7 e 8 non dividono tutti i valori (es. 40 non e' multiplo di 3, 60 non e' multiplo di 8).

<sub>confidenza: alta</sub>

### 71 → **E**

I: (√82 + √82)^2 = (2√82)^2 = 4 x 82 = 328, intero. II: 82√82 = 82^1,5, irrazionale, non intero. III: (√82)(√82)/82 = 82/82 = 1, intero. Quindi solo I e III.

<sub>confidenza: alta</sub>

### 72 → **C**

[(x+2)^2 + (x-2)^2]/2 = [(x^2 + 4x + 4) + (x^2 - 4x + 4)]/2 = (2x^2 + 8)/2 = x^2 + 4. I termini lineari si cancellano.

<sub>confidenza: alta</sub>

### 73 → **C**

x^2 - 2 < 0 equivale a x^2 < 2, cioe' |x| < √2, ovvero -√2 < x < √2. Le opzioni A, B e D escludono meta' dell'intervallo, mentre E e' troppo ampia (x = 1,5 darebbe x^2 = 2,25 > 2).

<sub>confidenza: alta</sub>

### 74 → **B**

Poiche' non inizia mai un libro il giorno in cui ne finisce un altro, ogni libro richiede ceil(pagine/50) giorni: 6, 3, 3, 4, 4, 1, 5, 2, 4, 3, 3, 5. I giorni cumulati sono 6, 9, 12, 16, 20, 21, 26, 28, ... : l'ottavo libro si conclude esattamente il giorno 28. Quindi alla fine del 28° giorno ha finito 8 libri.

<sub>confidenza: alta</sub>

### 75 → **D**

Le vendite totali sono x in entrambi gli anni; i produttori dell'Europa occidentale ne vendono 0,42x nel 1990 e 0,33x nel 1993. La diminuzione e' 0,42x - 0,33x = 0,09x, cioe' il 9% di x.

<sub>confidenza: alta</sub>

### 76 → **A**

(k+2)(k^3 - k) = (k+2) x k(k-1)(k+1): contiene il prodotto di tre interi consecutivi (k-1)k(k+1), sempre divisibile per 2 e per 3, quindi per 6. Il resto e' 0 (verificato con python3 per k da 1 a 49: l'insieme dei resti e' {0}).

<sub>confidenza: alta</sub>

### 77 → **D**

Ogni frazione supera 1/2; le differenze esatte sono 4/7-1/2 = 1/14, 5/9-1/2 = 1/18, 6/11-1/2 = 1/22, 7/13-1/2 = 1/26, 9/16-1/2 = 1/16. La piu' piccola e' 1/26 ≈ 0,0385, quindi 7/13 e' la piu' vicina a 1/2.

<sub>confidenza: alta</sub>

### 78 → **D**

p - (1 - p^2)/p = (p^2 - 1 + p^2)/p = (2p^2 - 1)/p. Uguagliando a r/p e moltiplicando per p (p ≠ 0) si ottiene r = 2p^2 - 1.

<sub>confidenza: alta</sub>

### 79 → **C**

Da |z|/w = 1 segue |z| = w, quindi w > 0 e z = w oppure z = -w. Elevando al quadrato in entrambi i casi si ha z^2 = w^2, sempre vera; A e B possono essere false (z puo' avere l'uno o l'altro segno), mentre D ed E falliscono, ad esempio, per z = -1, w = 1.

<sub>confidenza: alta</sub>

### 80 → **E**

Sia n il numero: n = (2/3)n + 108 → n - (2/3)n = 108 → n/3 = 108 → n = 324. Verifica: due terzi di 324 sono 216, e 216 + 108 = 324.

<sub>confidenza: alta</sub>

### 81 → **D**

Le ore in eccesso sono x-50, che corrispondono a 2(x-50) intervalli da 30 minuti. Ogni intervallo costa 0,40 dollari, quindi il supplemento vale 0,40·2(x-50) = 0,80(x-50). Totale: c + 0,80(x-50), cioè l'opzione D. L'opzione C sbaglia perché fattura 0,40 per ora anziché per mezz'ora.

<sub>confidenza: alta</sub>

### 82 → **B**

La riduzione di velocità è 100 - 47 = 53 km/h. Convertendo: 53 × 0,625 = 33,125 miglia orarie, quindi circa 33. Attenzione al distrattore C (53), che è la riduzione in km/h non convertita.

<sub>confidenza: alta</sub>

### 83 → **B**

Da 5x - 8 = 12 segue 5x = 20 e x = 4. Poiché x = y + 3, si ha y = 4 - 3 = 1. Risposta B (D=4 è il valore di x, distrattore).

<sub>confidenza: alta</sub>

### 84 → **E**

Ore registrate totali: 4 (martedì) + 2 (giovedì) = 6. Ore viste: da 1 a 2 il mercoledì più da 2 a 3 il venerdì, cioè da 3 a 5 in totale (e il materiale registrato è sempre sufficiente: il mercoledì ci sono già 4 ore disponibili, il venerdì 6 meno il visto). Quindi h = 6 - (visto) varia tra 6-5 = 1 e 6-3 = 3, cioè 1 ≤ h ≤ 3.

<sub>confidenza: alta</sub>

### 85 → **E**

Con a + b = 50 e 80a + 90b = 4270, sostituendo a = 50 - b: 4000 + 10b = 4270, quindi b = 27 ballerini nel gruppo B. Costo dei costumi B = 27 × 90 = 2.430 dollari. (Il gruppo A costa 23 × 80 = 1.840, distrattore A.)

<sub>confidenza: alta</sub>

### 86 → **D**

Dosaggio tipico per 120 libbre: 120/15 = 8 unità da 2 cc = 16 cc. Il prescritto è 18 cc, quindi l'eccesso relativo è (18-16)/16 = 2/16 = 0,125 = 12,5%. Nota: 11% circa sarebbe (18-16)/18, errore di base sbagliata.

<sub>confidenza: alta</sub>

### 87 → **D**

Da u = f(t) = √t - 10 si ricava √t = u + 10 e quindi t = (u + 10)². Il quadrato va applicato all'intera somma, non solo a u.

<sub>confidenza: alta</sub>

### 88 → **D**

Sia n il numero: 0,35n - 15 = 0,25n, da cui 0,10n = 15 e n = 150. Verifica: 35% di 150 = 52,5; 52,5 - 15 = 37,5 = 25% di 150.

<sub>confidenza: alta</sub>

### 89 → **D**

Se w e r sono le rose bianche e rosse, w + r = 30 e P(bianca) = 2·P(rossa) implica w = 2r. Quindi 3r = 30, r = 10 e w = 20.

<sub>confidenza: alta</sub>

### 90 → **C**

Il 20% degli intervistati telefonicamente è 3, quindi gli intervistati telefonici sono 3/0,20 = 15. Questi sono il 60% dei rispondenti: totale = 15/0,60 = 25.

<sub>confidenza: alta</sub>

### 91 → **D**

(-3)^(-2) = 1/(-3)² = 1/9, positivo perché l'esponente pari elimina il segno. Risposta D.

<sub>confidenza: alta</sub>

### 92 → **C**

I 6 prezzi formano una progressione aritmetica con ragione 0,25. Somma = 6a + 0,25(0+1+2+3+4+5) = 6a + 3,75 = 8,25, quindi 6a = 4,50 e a = 0,75 (il vaso più piccolo). Il più grande è 0,75 + 5(0,25) = 2,00 dollari.

<sub>confidenza: alta</sub>

### 93 → **A**

Con r = s + 6 e s ≥ 1: A = 2r = 2s+12; B = 2s; C = r+s = 2s+6; D = 2r-s = s+12; E = 2s-r = s-6. A supera B, C ed E immediatamente; A - D = (2s+12)-(s+12) = s > 0 poiché s è un intero positivo. Quindi A è sempre il maggiore.

<sub>confidenza: alta</sub>

### 94 → **C**

Il 15% dei primi 50.000 dà 7.500 dollari di commissione. Restano 24.000 - 7.500 = 16.500 dollari al 10%, quindi l'eccedenza è 16.500/0,10 = 165.000. Prezzo di vendita = 50.000 + 165.000 = 215.000 dollari.

<sub>confidenza: alta</sub>

### 95 → **B**

E = 2H e E = 3M, quindi H = E/2 e M = E/3. Il rapporto H:M = (1/2):(1/3) = 3:2. Controprova numerica: se E = 6, allora H = 3 e M = 2.

<sub>confidenza: alta</sub>

### 96 → **E**

Applicando la formula con d = 800 e y = 8: 800 × (8+1)/24 = 800 × 9/24 = 800 × 0,375 = 300 milligrammi.

<sub>confidenza: alta</sub>

### 97 → **A**

Le somme maggiori di 9 sono 10 (3 casi: 4+6, 5+5, 6+4), 11 (2 casi) e 12 (1 caso), in totale 6 esiti favorevoli su 36. Probabilità = 6/36 = 1/6. Enumerazione verificata con python3: 6/36 = 0,1667.

<sub>confidenza: alta</sub>

### 98 → **B**

I primi tre giorni sono sabato, domenica e lunedì. Tornare a casa alla fine di lunedì richiede: niente pioggia sabato (0,8), niente pioggia domenica (0,8) e pioggia lunedì (0,2). Prodotto = 0,8 × 0,8 × 0,2 = 0,128.

<sub>confidenza: alta</sub>

### 99 → **E**

Sia b il numero di chi ama entrambe; chi non ama nessuna delle due è 2b. Principio di inclusione-esclusione: 60 + 80 - b + 2b = 200, cioè 140 + b = 200, quindi b = 60 e 'nessuna delle due' = 120. Verifica della partizione: solo sci 0, entrambe 60, solo pattinaggio 20, nessuna 120, totale 200.

<sub>confidenza: alta</sub>

### 100 → **E**

Si applicano le relazioni date dall'interno verso l'esterno: m ⊕ p = n; poi n ⊕ q = q; infine q ⊕ p = r. Quindi [(m⊕p)⊕q]⊕p = r. (Le relazioni n⊕r = m e p⊕q = p non servono e fungono da distrattori; nota che ⊕ non è commutativo, dato che p⊕q ≠ q⊕p.)

<sub>confidenza: alta</sub>

### 101 → **A**

Le prime 24 ore costano x dollari forfettari. Le ore eccedenti sono 36 - 24 = 12, ciascuna a y dollari, quindi 12y. Costo totale = x + 12y.

<sub>confidenza: alta</sub>

### 102 → **D**

1 metro cubo = 1.000.000 cm3, quindi la massa e' 7,3 g/cm3 x 10^6 cm3 = 7.300.000 grammi. Dividendo per 1.000 g/kg si ottengono 7.300 kg.

<sub>confidenza: alta</sub>

### 103 → **C**

Moltiplico entrambi i membri di z + (1-2z^2)/z = w/z per z (lecito perche' z != 0): z^2 + 1 - 2z^2 = w. Semplificando, w = 1 - z^2 = -z^2 + 1.

<sub>confidenza: alta</sub>

### 104 → **C**

Per definizione (a,b,c)Theta(d,e,f) = ad + be + cf. Quindi (1)(1) + (-2)(1/2) + (3)(1/3) = 1 - 1 + 1 = 1.

<sub>confidenza: alta</sub>

### 105 → **B**

Escludendo i 4 studenti con 0 assenze, restano 3+10+3+5+3 = 24 studenti. In ordine crescente: posizioni 1-3 valgono 1, posizioni 4-13 valgono 2, 14-16 valgono 3, 17-21 valgono 4, 22-24 valgono 5 o piu'. La mediana e' la media del 12esimo e 13esimo valore, entrambi 2, quindi 2.

<sub>confidenza: alta</sub>

### 106 → **C**

Da d/c = b/a segue c/d = a/b, quindi x/y = c/d = a/b. I: invertendo x/y = a/b si ha y/x = b/a, vera. II: da x/y = a/b si ha bx = ay, cioe' x/a = y/b, vera. III: y/a = x/b equivarrebbe a by = ax, che non discende da bx = ay (controesempio x=1, y=2, a=1, b=2: x/y=1/2=a/b, ma y/a=2 mentre x/b=1/2). Quindi solo I e II.

<sub>confidenza: alta</sub>

### 107 → **B**

[t] e' il ceiling (minimo intero >= t). [x/2] = 0 richiede -1 < x/2 <= 0, cioe' -2 < x <= 0. Fra le opzioni solo -3/2 rientra in quell'intervallo: -3/2 / 2 = -0.75 e ceiling(-0.75) = 0. Il valore -2 e' escluso perche' ceiling(-1) = -1.

<sub>confidenza: alta</sub>

### 108 → **B**

a^2 + 2a - 24 = 0 si fattorizza in (a+6)(a-4) = 0, quindi le radici sono 4 e -6; lo stesso vale per b. Poiche' a != b, uno vale 4 e l'altro -6, dunque a + b = -2 (equivalentemente, la somma delle radici e' -2 per Vieta).

<sub>confidenza: alta</sub>

### 109 → **E**

I voti degli indipendenti sono 0,4N e da questi lei ha ricevuto 8.000 voti (numero fisso, non una percentuale). I voti dei registrati a un partito sono 0,6N e ne riceve il 10%, cioe' 0,06N. Totale = 0,06N + 8.000.

<sub>confidenza: alta</sub>

### 110 → **B**

Primi 4 mesi: C = I + 32.000 quindi P = I - C = -32.000 al mese, totale -128.000. Mesi successivi (3): I = C + 36.000 quindi P = +36.000, totale +108.000. Ultimi 5 mesi: P = +10.000, totale +50.000. Somma: -128.000 + 108.000 + 50.000 = 30.000.

<sub>confidenza: alta</sub>

### 111 → **E**

Sia n il numero di unita' di P; allora le unita' di Q sono 2n. Ricavo totale = 20n + 17(2n) = 54n su 3n unita' vendute, quindi la media e' 54n/3n = 18 dollari per unita'.

<sub>confidenza: alta</sub>

### 112 → **B**

17 viaggi x 4 boccioni = 68 boccioni. 68 = 7 x 9 + 5, quindi 9 cartoni pieni e uno con 5 boccioni. Per completarlo servono 7 - 5 = 2 boccioni.

<sub>confidenza: alta</sub>

### 113 → **E**

Sia D il numero di democratici l'anno scorso: repubblicani R = D + 20 e totale T = 2D + 20. Quest'anno il totale e' lo stesso e i repubblicani sono D + 18. Impongo D + 18 = (2/3)(2D + 20): 3D + 54 = 4D + 40, quindi D = 14 e T = 48. Verifica: repubblicani quest'anno 32 = (2/3)(48).

<sub>confidenza: alta</sub>

### 114 → **D**

I depositi sono 1, 2, ..., 50 dollari nelle 50 settimane, con somma 50x51/2 = 1.275. Aggiungendo il saldo iniziale: 800 + 1.275 = 2.075 dollari (python3: 800+sum(range(1,51)) = 2075).

<sub>confidenza: alta</sub>

### 115 → **B**

2,7 miliardi di libbre = 2.700 milioni di libbre; la differenza rispetto al 2007 e' 2.700 - 980 = 1.720 milioni di libbre. Convertendo: 1.720 / 8,6 = 200 milioni di galloni.

<sub>confidenza: alta</sub>

### 116 → **B**

4 macchine producono x in 6 giorni, quindi una macchina produce x/24 al giorno. Per fare 3x in 4 giorni serve una produzione di 3x/4 al giorno; il numero di macchine e' (3x/4)/(x/24) = 18.

<sub>confidenza: alta</sub>

### 117 → **C**

Testo le quattro operazioni su 6 Delta 3: 9 (addizione) e 18 (moltiplicazione) violano <= 3; 3 (sottrazione) e 2 (divisione) la rispettano. Quindi Delta e' sottrazione o divisione. I: 2-2 = 0 ma 2/2 = 1, non necessaria. II: vale solo per la divisione, non necessaria. III: 4-2 = 2 e 4/2 = 2, vera in entrambi i casi.

<sub>confidenza: alta</sub>

### 118 → **A**

0,25n = 0,375m implica n/m = 0,375/0,25 = 3/2. Quindi 12n/m = 12 x 3/2 = 18.

<sub>confidenza: alta</sub>

### 119 → **A**

Ho enumerato con python3 tutte le permutazioni delle cifre 1,2,3,6,7,8 divise in due numeri di tre cifre e cercato la differenza positiva minima: il minimo e' 29, dato da 316 - 287. La logica dietro: si sceglie una coppia di centinaia consecutive (3 e 2), si minimizza il numero maggiore con le cifre piu' piccole rimaste (316) e si massimizza il minore con le piu' grandi (287).

<sub>confidenza: alta</sub>

### 120 → **D**

I consumatori che hanno indicato una delle quattro tecniche elencate sono il 35+22+18+15 = 90% del totale intervistato. Coupon piu' esposizioni in negozio sono 22+18 = 40%. La frazione richiesta e' 40/90 = 4/9.

<sub>confidenza: alta</sub>

### 121 → **E**

Se il 65% è full-time, il 35% è part-time; la differenza è il 30% del totale. Quindi 0,30·T = 5.100 → T = 5.100/0,30 = 17.000 (verificato con python3). Controllo: 65% di 17.000 = 11.050 full-time e 35% = 5.950 part-time, differenza 5.100. Corrisponde all'opzione E.

<sub>confidenza: alta</sub>

### 122 → **A**

C(90) = 100.000·90/(100−90) = 9.000.000/10 = 900.000 dollari; C(80) = 100.000·80/(100−80) = 8.000.000/20 = 400.000 dollari. La differenza è 900.000 − 400.000 = 500.000 dollari (confermato con python3). Risposta A.

<sub>confidenza: alta</sub>

### 123 → **E**

Ponendo u = xy l'equazione x²y² − xy = 6 diventa u² − u − 6 = 0, cioè (u−3)(u+2) = 0, quindi xy = 3 oppure xy = −2 (entrambi compatibili con xy ≠ 0). Da xy = 3 segue y = 3/x (III) e da xy = −2 segue y = −2/x (II); invece y = 1/(2x) darebbe xy = 1/2, che non risolve l'equazione, quindi I è esclusa. Valgono II e III: opzione E.

<sub>confidenza: alta</sub>

### 124 → **E**

Sommare la stessa costante a tutti i dati trasla la distribuzione: anche la media aumenta di 1, quindi ogni scarto (valore − media) resta identico. Poiché la deviazione standard dipende solo dagli scarti dalla media, essa non cambia e resta d. Risposta E.

<sub>confidenza: alta</sub>

### 125 → **D**

Prendo 100 senior: 80 fanno calcolo, e il 60% di questi (48) fa anche fisica. Poiché il 10% non fa né l'una né l'altra, chi fa almeno una delle due è 90; quindi chi fa solo fisica è 90 − 80 = 10. Il totale di chi fa fisica è 48 (entrambe) + 10 (solo fisica) = 58%. Risposta D.

<sub>confidenza: alta</sub>

### 126 → **B**

Dividere per 10^k sposta la virgola a sinistra di k posti. Con k = 2 si ottiene 5.610,37/100 = 56,1037, la cui cifra delle unità è 6 (verificato con python3). Gli altri casi non funzionano: k = 1 dà 561,037 (unità 1), k = 3 dà 5,61037 (unità 5), k = −1 dà 56.103,7 (unità 3), k = −2 dà 561.037 (unità 7). Risposta B.

<sub>confidenza: alta</sub>

### 127 → **E**

Le tre presse insieme hanno tasso combinato 1/4 di lavoro all'ora; S e T insieme hanno tasso 1/5. Il tasso di R da solo è 1/4 − 1/5 = 5/20 − 4/20 = 1/20 di lavoro all'ora, quindi R impiega 20 ore. Risposta E.

<sub>confidenza: alta</sub>

### 128 → **E**

La domanda riguarda IBM e AT&T: per il principio di inclusione-esclusione chi possiede azioni di almeno una delle due è 48 + 30 − 15 = 63. Su 200 intervistati, chi non ne possiede di nessuna delle due è 200 − 63 = 137. Risposta E.

<sub>confidenza: alta</sub>

### 129 → **D**

Gli interi con −26 < k < 24 vanno da −25 a 23 inclusi. I termini da −23 a 23 si cancellano a coppie dando 0, restano −25 e −24 la cui somma è −49 (confermato con python3: sum(range(-25,24)) = −49). Risposta D.

<sub>confidenza: alta</sub>

### 130 → **E**

Dal disegno R sta a sinistra dello 0, quindi la sua coordinata è negativa e vale −r (dato che |R| = r); S e T stanno a destra, con coordinate +s e +t. La media aritmetica è (−r + s + t)/3 = (s + t − r)/3. Risposta E.

<sub>confidenza: alta</sub>

### 131 → **A**

Mark ha venduto n − 10 e Ann n − 2. La condizione 'almeno una scatola ciascuno' impone n − 10 ≥ 1, cioè n ≥ 11; la condizione 'insieme meno di n' dà (n−10) + (n−2) < n, cioè 2n − 12 < n, ovvero n < 12. L'unico intero è n = 11 (verifica: Mark 1, Ann 9, totale 10 < 11). Risposta A.

<sub>confidenza: alta</sub>

### 132 → **A**

Dalle unità: 5 + R termina in 4, quindi R = 9 con riporto 1. Dalle centinaia: 3 + 4 + riporto = 8, quindi il riporto dalle decine è 1, cioè P + Q + 1 = S + 10; con Q = 2P si ha 3P + 1 = S + 10, cioè S = 3P − 9. Le cifre ammesse (Q = 2P ≤ 9 e S ≥ 0) danno P = 3 → S = 0 e P = 4 → S = 3; fra le opzioni compare solo 3, verificato con 345 + 489 = 834. Risposta A.

<sub>confidenza: alta</sub>

### 133 → **E**

Gli studenti che seguono almeno una fra musica e arte sono x + y − z (inclusione-esclusione, poiché gli z che fanno entrambe sono contati due volte in x + y). Quindi chi non segue nessuna delle due è 5.000 − (x + y − z) = 5.000 − x − y + z. Risposta E.

<sub>confidenza: alta</sub>

### 134 → **D**

Poiché ogni partecipante è azionista, dipendente o entrambi, la somma 62% + 47% = 109% eccede il 100% esattamente della sovrapposizione: entrambi = 9%. Gli azionisti NON dipendenti sono quindi 62% − 9% = 53%. Risposta D.

<sub>confidenza: alta</sub>

### 135 → **A**

Scomponendo: 90 = 2·3², 196 = 2²·7², 300 = 2²·3·5², quindi M = 2²·3²·5²·7² = 44.100 (verificato con python3). 600 = 2³·3·5² richiede 2³ mentre M contiene solo 2², perciò 600 non divide M; le altre opzioni sì (44.100 diviso 700, 900, 2.100, 4.900 dà resto 0). Risposta A.

<sub>confidenza: alta</sub>

### 136 → **D**

Dai dati del grafico (20, 12, 18, 10, 16, 8) le variazioni percentuali sono: 1→2 = −40%, 2→3 = +50%, 3→4 = −44,4%, 4→5 = +60%, 5→6 = −50% (calcolate con python3). La maggiore in valore assoluto è il +60% da Day 4 a Day 5. Risposta D.

<sub>confidenza: alta</sub>

### 137 → **C**

20! è divisibile per ogni intero da 1 a 20, quindi per 15, 17 e 19. Perciò 20! + 17 è divisibile per 17 (entrambi gli addendi lo sono), mentre per 15 e per 19 il primo addendo è divisibile ma 17 no, quindi la somma non lo è. Vale solo II: risposta C.

<sub>confidenza: alta</sub>

### 138 → **D**

Costo d'acquisto: 480 marchi / 1,6 marchi per dollaro = 300 dollari. Ricavo: 2.385 franchi / 5,3 franchi per dollaro = 450 dollari. Il profitto lordo è 450 − 300 = 150 dollari. Risposta D.

<sub>confidenza: alta</sub>

### 139 → **D**

Sia g il numero maggiore (meno negativo) e l = 2g − 4 il minore; da l·g = 160 si ottiene 2g² − 4g − 160 = 0, cioè g² − 2g − 80 = 0, ovvero (g − 10)(g + 8) = 0. Poiché entrambi i numeri devono essere negativi, si scarta g = 10 e resta g = −8, con l = 2(−8) − 4 = −20; verifica: (−8)(−20) = 160 e −20 < −8. Risposta D.

<sub>confidenza: alta</sub>

### 140 → **B**

N(t) = −20(t − 5)² + 500 è una parabola con concavità verso il basso e vertice in t = 5, valore massimo 500 cm; t = 5 rientra nel dominio 0 ≤ t ≤ 10. Poiché t è misurato in ore dopo le 2:00 del mattino, il massimo si ha alle 2:00 + 5 ore = 7:00. Risposta B.

<sub>confidenza: alta</sub>

### 141 → **A**

A 8 minuti/miglio, in 50 minuti Bob percorre 50/8 = 6,25 miglia in totale. Se corre altre d miglia verso sud, deve poi tornare indietro 3,25 + d miglia. Quindi d + (3,25 + d) = 6,25, da cui 2d = 3 e d = 1,5 miglia.

<sub>confidenza: alta</sub>

### 142 → **D**

Dopo un anno il primo deposito vale 1,08x; si aggiunge x, quindi il saldo è 1,08x + x. Al termine del secondo anno tutto cresce di un altro 8%: w = (1,08x + x)(1,08) = (1,08)^2 x + 1,08x. Raccogliendo x: x = w / (1,08 + (1,08)^2), cioè l'opzione D (il libro usa W maiuscola nelle opzioni, refuso di notazione).

<sub>confidenza: alta</sub>

### 143 → **A**

M è la somma di 100 termini 1/n con n da 201 a 300. Ogni termine è minore di 1/200 e maggiore di 1/300, quindi 100·(1/300) < M < 100·(1/200), cioè 1/3 < M < 1/2. (Il valore reale è circa 0,4046.)

<sub>confidenza: alta</sub>

### 144 → **E**

Tasso congiunto = 800/x chiodi all'ora; tasso di A = 800/y. Tasso di B = 800/x − 800/y = 800(y − x)/(xy). Il tempo di B da solo è 800 diviso il suo tasso, cioè xy/(y − x). Il denominatore è y − x perché y > x (A da sola impiega più tempo delle due insieme).

<sub>confidenza: alta</sub>

### 145 → **E**

Cesto 1: 4 mele su 6; cesto 2: 3 mele su 8. P(mela dal 1 e arancia dal 2) = (4/6)(5/8) = 20/48; P(arancia dal 1 e mela dal 2) = (2/6)(3/8) = 6/48. Somma = 26/48 = 13/24.

<sub>confidenza: alta</sub>

### 146 → **E**

Numero totale di paia = 403 × 98 × 2.488. Con python3: 403*98*2488 = 98.261.072, cioè circa 9,8×10^7, molto più vicino a 10^8 (differenza ~2 milioni) che a 10^7 (differenza ~88 milioni).

<sub>confidenza: alta</sub>

### 147 → **C**

Le cifre di n = 1k2,k24 sono 1, k, 2, k, 2, 4, con somma 9 + 2k. Perché n sia divisibile per 3 serve che 2k sia divisibile per 3, e poiché 2 e 3 sono coprimi serve k multiplo di 3: k = 0, 3, 6, 9. Quattro valori possibili.

<sub>confidenza: alta</sub>

### 148 → **B**

Sacchetto P: 10,8% di 37 = 4 biglie blu; sacchetto R: 50% di 32 = 16; sacchetto Q: 66,7% di x = (2/3)x. La condizione è 4 + (2/3)x + 16 = (1/3)(37 + x + 32). Moltiplicando per 3: 12 + 2x + 48 = 69 + x, quindi x = 9. Verifica: blu = 4 + 6 + 16 = 26 e totale 78, con 26 = 78/3.

<sub>confidenza: alta</sub>

### 149 → **A**

Con 161 dipendenti la mediana è l'81° valore ordinato per età. Cumulate: meno di 20 → 29 dipendenti; fino a 29 anni → 29 + 58 = 87. Poiché 81 cade fra il 30° e l'87° elemento, l'81° sta nella fascia 20–29, quindi 20 ≤ m ≤ 29.

<sub>confidenza: alta</sub>

### 150 → **E**

Si scrive k! = k·(k−1)!, quindi k! + (n−k)·(k−1)! = (k−1)!·[k + (n−k)] = (k−1)!·n = n·(k−1)!.

<sub>confidenza: alta</sub>

### 151 → **E**

Barbara = 65; Ron = Barbara − 1 = 64; Amy = Ron − 4 = 60. Ordinate: 60, 64, 65: la mediana è 64.

<sub>confidenza: alta</sub>

### 152 → **E**

Da x + y = 1 segue 100x + 200y = 100(x + y) + 100y = 100 + 100y. Con 0 < y < 1 l'espressione varia strettamente fra 100 e 200. Quindi 80 (I) è impossibile, mentre 140 (y = 0,4) e 199 (y = 0,99) sono raggiungibili: II e III.

<sub>confidenza: alta</sub>

### 153 → **D**

0,1X con X cifra non nulla vale al massimo 0,19; 0,02Y con Y cifra non nulla vale al minimo 0,021. Il rapporto massimo è 0,19/0,021 = 9,048 (calcolato con python3), il cui valore più vicino fra le opzioni è 9.

<sub>confidenza: alta</sub>

### 154 → **C**

Ogni coppia di squadre gioca esattamente una partita: il numero di partite è C(12,2) = 12·11/2 = 66.

<sub>confidenza: alta</sub>

### 155 → **E**

Servono due condizioni: 2 − √x ≥ 0 → x ≤ 4, e 1 − √(2 − √x) ≥ 0 → 2 − √x ≤ 1 → x ≥ 1. L'espressione è dunque reale solo per 1 ≤ x ≤ 4; per x = 5 si ha 2 − √5 < 0 e la radice interna non è definita.

<sub>confidenza: alta</sub>

### 156 → **D**

(L'enunciato del libro ha le parole fuori ordine: 'when What is the remainder 3^19 is divided by 10'; si legge come resto di 3^19 diviso 10.) Le ultime cifre di 3^n hanno ciclo 3, 9, 7, 1 di periodo 4. Poiché 19 = 4·4 + 3, la terza posizione del ciclo dà 7.

<sub>confidenza: alta</sub>

### 157 → **E**

Su 200: 160 hanno il cellulare, 90 il cercapersone, e tutti ne hanno almeno uno, quindi chi ha entrambi è 160 + 90 − 200 = 50. L'evento 'non ha il cellulare oppure non ha il cercapersone' è il complementare di 'ha entrambi': 200 − 50 = 150, cioè il 75%.

<sub>confidenza: alta</sub>

### 158 → **B**

Detto P il prezzo a inizio anno, alla fine del primo trimestre vale 1,2P e alla fine del secondo 1,5P. La variazione percentuale è (1,5P − 1,2P)/1,2P = 0,3/1,2 = 0,25, cioè 25%.

<sub>confidenza: alta</sub>

### 159 → **D**

Il termine n-esimo è (1/2)^n, quindi il decimo è 1/1024 = 0,0009765625 (verificato con python3). Questo valore sta fra 0,0001 e 0,001.

<sub>confidenza: alta</sub>

### 160 → **E**

Espandendo il secondo membro: xy + z = xy + xz, da cui z = xz, cioè z(1 − x) = 0. Quindi deve valere z = 0 oppure x = 1: l'unica affermazione necessariamente vera è l'opzione E.

<sub>confidenza: alta</sub>

### 161 → **E**

Siano r e 1,5r i tassi (piscine all'ora). Insieme: r + 1,5r = 2,5r = 1/4, quindi r = 1/10 e il tasso della pompa veloce è 1,5/10 = 3/20. Il tempo da sola è 20/3 ore (circa 6,67).

<sub>confidenza: alta</sub>

### 162 → **A**

Per 0 < x < 1 vale x^3 < x^2 < x < √x < 1 < 1/x (per esempio con x = 0,25: 0,0156; 0,0625; 0,25; 0,5; 4). Ordinando i cinque valori, il terzo, cioè la mediana, è x.

<sub>confidenza: alta</sub>

### 163 → **C**

Poniamo Kaye = 5k e Alberto = 3k. Dopo il regalo: (5k − 10)/(3k + 10) = 7/5 → 25k − 50 = 21k + 70 → 4k = 120 → k = 30. Quindi Kaye ha 150 − 10 = 140 e Alberto 90 + 10 = 100: la differenza è 40.

<sub>confidenza: alta</sub>

### 164 → **E**

1,5 deviazioni standard = 1,5 × 0,3 = 0,45, quindi l'intervallo è 8,1 ± 0,45 = [7,65; 8,55]. Dei 12 valori elencati solo 7,51 cade fuori (tutti gli altri, da 7,73 a 8,53, sono compresi): conteggio verificato con python3 = 11.

<sub>confidenza: alta</sub>

### 170 → **E**

"X percento maggiore di" significa moltiplicare per (1 + X/100). Il 1993 era 400% maggiore del 1992: 1993 = N + 4N = 5N. Il 1994 era 300% maggiore del 1993: 1994 = 5N + 3(5N) = 4·5N = 20N. Quindi il totale del 1994 è 20N.

<sub>confidenza: alta</sub>

### 171 → **D**

Da x/|y| = -1 segue x = -|y|, con y ≠ 0 e x < 0. Elevando al quadrato: x² = |y|² = y², quindi D è sempre vera. Le altre cadono con controesempi: con y = -3 si ha x = -3, e allora A (x = -y = 3) è falsa; con y = 3, x = -3, quindi B è falsa; C è impossibile perché x è negativo e y² positivo; E dà x³ = -27 e y³ = ±27, non sempre uguali (con y = 3 fallisce).

<sub>confidenza: alta</sub>

### 172 → **A**

La colonna centrale è completamente nota: 1·√6·6 = 6√6, quindi il prodotto comune è P = 6√6. Riga 1: A·1·2√3 = 6√6 → A = 3√2. Riga 3: √3·6·D = 6√6 → D = √2. Colonna 1: A·B·√3 = 3√2·B·√3 = 3√6·B = 6√6 → B = 2. Colonna 3: 2√3·C·√2 = 2√6·C = 6√6 → C = 3. Quindi ABCD = 3√2·2·3·√2 = 36 (verificato numericamente: tutte le righe e colonne danno 14.6969 = 6√6).

<sub>confidenza: alta</sub>

### 173 → **A**

Sia T il reddito totale di maggio: Mrs. Lee guadagna 0,60T e il resto della famiglia 0,40T. A giugno lei guadagna il 20% in più: 1,2·0,60T = 0,72T, mentre il resto resta 0,40T, per un totale di 1,12T. Il rapporto è 0,72/1,12 = 0,6428… ≈ 64%.

<sub>confidenza: alta</sub>

### 174 → **B**

Sia v la velocità effettiva e t il tempo effettivo; la distanza d = vt è la stessa. Con velocità v+15 il tempo sarebbe (2/3)t (ridotto di 1/3), quindi vt = (v+15)·(2/3)t. Semplificando t: v = (2/3)(v+15) → 3v = 2v + 30 → v = 30 miglia orarie.

<sub>confidenza: alta</sub>

### 175 → **E**

Si valuta ciascun insieme soluzione: A) x⁴≥1 → |x|≥1, due semirette; B) x³≤27 → x≤3, semiretta infinita; C) x²≥16 → x≤-4 o x≥4, due semirette; D) 2≤|x|≤5 → due segmenti separati [-5,-2] e [2,5]; E) 2≤3x+4≤6 → -2≤3x≤2 → -2/3≤x≤2/3, un unico segmento di lunghezza finita. Quindi E.

<sub>confidenza: alta</sub>

### 176 → **B**

Il nuovo grafico è quello dato traslato verso l'alto di 2. Derivata di f(x)=(x+1)(x-1)²: f'(x)=(x-1)(3x+1), quindi massimo locale in x=-1/3 con f=32/27≈1,185 e minimo locale in x=1 con f=0. Dopo la traslazione il massimo locale vale ≈3,185 e il minimo locale vale 2: entrambi positivi, quindi il ramo di destra non tocca mai l'asse x. Poiché per x→-∞ la funzione tende a -∞, c'è una sola intersezione, a sinistra di -1. Risposta: One.

<sub>confidenza: alta</sub>

### 177 → **E**

Con 10 persone il costo pro capite è x/10; con 16 persone è x/16. La differenza è x/10 - x/16 = (8x - 5x)/80 = 3x/80. Quindi con 10 persone ciascuno paga 3x/80 dollari in più.

<sub>confidenza: alta</sub>

### 178 → **D**

L'ordine conta (i libri sono elencati nell'ordine in cui vengono scelti), quindi si tratta di disposizioni semplici di 10 oggetti presi 4 a 4: 10·9·8·7 = 5.040.

<sub>confidenza: alta</sub>

### 179 → **D**

990 = 2·3²·5·11. Perché n! sia divisibile per 990 serve il fattore primo 11, quindi n ≥ 11. Con n = 11 il fattoriale contiene 11, 5, 2 e 9 = 3², quindi 11! è divisibile per 990. Il minimo è n = 11.

<sub>confidenza: alta</sub>

### 180 → **C**

P(M) = 1 - 0,8 = 0,2 e P(R) = 1 - 0,6 = 0,4. Poiché M e R sono mutuamente esclusivi, P(M o R) = P(M) + P(R) = 0,2 + 0,4 = 0,6 = 3/5.

<sub>confidenza: alta</sub>

### 181 → **C**

Costo totale = 10.000 + 3·20.000 = 70.000 dollari; ricavo = 8·20.000 = 160.000 dollari; profitto lordo = 90.000 dollari. Diviso per 20.000 utensili dà 4,50 dollari per utensile. (Il testo del libro ha un refuso: manca lo spazio in "\$8.The".)

<sub>confidenza: alta</sub>

### 182 → **A**

Con Q dispari, Q interi consecutivi hanno la mediana coincidente con il termine centrale, cioè 120, e ci sono (Q-1)/2 termini sopra di essa, ciascuno maggiore di 1 rispetto al precedente. Quindi il massimo è 120 + (Q-1)/2. Verifica con Q=5: interi 118,119,120,121,122, massimo 122 = 120 + 2 = 120 + (5-1)/2. Risposta A.

<sub>confidenza: alta</sub>

### 183 → **A**

(t/1000)⁴ = t⁴/10¹². Se t⁴ ha d cifre, la prima cifra non nulla occupa la posizione decimale 12-d+1, quindi il numero di zeri fra la virgola e la prima cifra non nulla è 12-d. Per t=3: t⁴=81, d=2, 10 zeri; t=5: 625, d=3, 9 zeri; t=9: 6561, d=4, 8 zeri. Servirebbero meno di 8 zeri, cioè d ≥ 5, cioè t⁴ ≥ 10.000, cioè t ≥ 10: nessuno dei tre valori funziona, quindi "None".

<sub>confidenza: alta</sub>

### 184 → **B**

Prima cifra: 8 scelte (da 2 a 9); seconda: 2 scelte (0 o 1); terza: 10 scelte. Totale senza vincolo = 8·2·10 = 160. Vanno tolti i codici con seconda e terza cifra entrambe 0: 8·1·1 = 8. Quindi 160 - 8 = 152 (confermato da enumerazione in python3).

<sub>confidenza: alta</sub>

### 185 → **E**

Sia x il volume di soluzione al 2% e 60-x quello al 12%: 0,02x + 0,12(60-x) = 0,05·60 = 3. Da cui 7,2 - 0,10x = 3 → x = 4,2/0,10 = 42 litri. (Coerente con la regola della leva: la distanza 12-5=7 sta a 5-2=3, quindi il 2% pesa 7/10 di 60 = 42.)

<sub>confidenza: alta</sub>

### 186 → **E**

Sia J il peso di Jake e S quello della sorella: J - 8 = 2S e J + S = 278. Sostituendo S = 278 - J: J - 8 = 2(278 - J) = 556 - 2J → 3J = 564 → J = 188 (e S = 90; verifica: 188-8 = 180 = 2·90).

<sub>confidenza: alta</sub>

### 187 → **B**

Una trasformazione lineare y = ax + b sposta la media di b ma moltiplica la deviazione standard per |a|; l'addizione della costante 20 non cambia la dispersione. Quindi la nuova deviazione standard è 0,8·20 = 16.

<sub>confidenza: alta</sub>

### 188 → **B**

Principio di inclusione-esclusione: |E∪F∪I| = 26+26+32 - |E∩F| - |E∩I| - |F∩I| + |E∩F∩I|. Poiché nessuno ha visitato sia Inghilterra sia Francia, |E∩F| = 0 e quindi anche l'intersezione tripla è 0. Risultato: 84 - 0 - 6 - 11 + 0 = 67.

<sub>confidenza: alta</sub>

### 189 → **C**

Aumento = 385 - 320 = 65 milioni. Variazione percentuale = 65/320 = 0,203125, cioè circa il 20%.

<sub>confidenza: alta</sub>

### 190 → **B**

Se x = qy + 9 con q intero, allora x/y = q + 9/y; dato x/y = 96,12 si ha q = 96 e la parte frazionaria 0,12 = 9/y, quindi y = 9/0,12 = 75. Verifica: x = 96,12·75 = 7.209 e 7.209 = 96·75 + 9, con resto 9 < 75.

<sub>confidenza: alta</sub>

### 191 → **B**

La prima equazione x(2x+1)=0 dà x=0 oppure x=-1/2. La seconda (x+1/2)(2x-3)=0 dà x=-1/2 oppure x=3/2. Poiché entrambe devono valere simultaneamente, l'unica soluzione comune è x=-1/2.

<sub>confidenza: alta</sub>

### 192 → **A**

Le classi totali sono 32x2=64 e gli insegnanti 37. Siano a, b, c il numero di docenti con 1, 2, 3 classi: a+b+c=37 e a+2b+3c=64. Sottraendo: b+2c=27. Con c=n: n=0 dà b=27, a=10 (valido); n massimo richiede b>=0, quindi 2n<=27 cioè n<=13, e n=13 dà b=1, a=23 (valido). Dunque minimo 0 e massimo 13.

<sub>confidenza: alta</sub>

### 193 → **B**

I cinque numeri in ordine crescente sono n, n+1, n+2, n+4, n+8, quindi la mediana è il terzo valore, n+2. La media è (5n+15)/5 = n+3. La differenza media meno mediana è (n+3)-(n+2)=1, indipendente da n.

<sub>confidenza: alta</sub>

### 194 → **E**

Sia t il numero attuale di insegnanti, quindi gli studenti sono 30t. Dopo le variazioni: (30t+50)/(t+5)=25, da cui 30t+50=25t+125, 5t=75, t=15. Verifica: 450 studenti e 15 docenti; poi 500/20=25.

<sub>confidenza: alta</sub>

### 195 → **B**

25^n = (5^2)^n = 5^(2n). La disuguaglianza 5^(2n) > 5^12 con base 5>1 equivale a 2n>12, cioè n>6. Il minimo intero è n=7 (con n=6 si avrebbe uguaglianza, non maggiore).

<sub>confidenza: alta</sub>

### 196 → **C**

La probabilità di scegliere una donna è 0,60 e, condizionatamente, la probabilità che sia avvocato è 0,45. Il prodotto 0,60 x 0,45 = 0,27 è la probabilità di selezionare una donna avvocato.

<sub>confidenza: alta</sub>

### 197 → **D**

Ogni anno il numero di alberi si moltiplica per 1+1/4=5/4, quindi dopo 4 anni x(5/4)^4=6250. Da python3: 6250*(4/5)^4 = 2560. Verifica: 2560 -> 3200 -> 4000 -> 5000 -> 6250.

<sub>confidenza: alta</sub>

### 198 → **C**

Gli anni 1990-2000 sono 11, quindi la mediana è il 6° valore in ordine crescente. Dal grafico (e dalla didascalia: crescita da ~190.000 nel 1990 fino a ~380.000 nel 1998, poi calo a ~260.000 nel 2000) circa 7-8 anni superano i 300.000 mentre i primi 4-5 anni sono sotto i 300.000; il 6° valore cade quindi poco sopra 300.000, cioè intorno a 300-310 mila. Il disegno ASCII è impreciso (mostra solo 10 barre invece di 11), ma la scelta più vicina è 310.000.

<sub>confidenza: **media**</sub>

### 199 → **B**

72 = 8 x 9 = 2^3 x 3^2. Quindi 2^3 divide 72 mentre 2^4 = 16 non lo divide (72/16 = 4,5). Per la definizione data, k = 3.

<sub>confidenza: alta</sub>

### 200 → **D**

La distribuzione è simmetrica rispetto a m, quindi il 50% sta sotto m. Il 68% cade tra m-d e m+d e, per simmetria, metà di questo (34%) sta tra m e m+d. Perciò la porzione minore di m+d è 50%+34% = 84%.

<sub>confidenza: alta</sub>

### 201 → **E**

I primi tre panini sono divisi tra m studenti, quindi ogni pezzo vale 1/m e tre pezzi valgono 3/m. Il quarto è diviso tra m-4 studenti, quindi un pezzo vale 1/(m-4). Totale: 3/m + 1/(m-4) = [3(m-4)+m]/[m(m-4)] = (4m-12)/[m(m-4)].

<sub>confidenza: alta</sub>

### 202 → **D**

Se x = 1+sqrt(2), allora x-1 = sqrt(2); elevando al quadrato x^2-2x+1 = 2, cioè x^2-2x-1 = 0. Corrisponde all'opzione D (le cui radici sono 1±sqrt(2)).

<sub>confidenza: alta</sub>

### 203 → **B**

Prendo 100 lavoratori nel 1992: disoccupati 16. Nel 1996 i lavoratori sono 120 e i disoccupati 0,09x120 = 10,8. Variazione percentuale: (10,8-16)/16 = -0,325, cioè un calo del 32,5%, approssimativamente il 30% di diminuzione.

<sub>confidenza: alta</sub>

### 204 → **C**

I non difettosi sono 9 su 12. Probabilità che entrambe le penne siano buone: C(9,2)/C(12,2) = 36/66 = 6/11 (verificato con python3: 0,5454...). Equivalente a (9/12)x(8/11).

<sub>confidenza: alta</sub>

### 205 → **E**

Con 10 frutti a media 56 centesimi il totale è 560; da 40a+60o=560 e a+o=10 si ottiene o=8 mele=2. Rimettendo indietro x arance: (560-60x)/(10-x) = 52 => 560-60x = 520-52x => 8x = 40 => x = 5. Verifica: restano 2 mele e 3 arance, totale 80+180=260 su 5 frutti = 52.

<sub>confidenza: alta</sub>

### 206 → **C**

Primo rapporto royalties/vendite: 3/20 = 0,15. Secondo: 9/108 = 0,08333. Diminuzione percentuale = (0,15-0,08333)/0,15 = 0,4444, cioè circa il 44,4%, che si arrotonda al 45%.

<sub>confidenza: alta</sub>

### 207 → **B**

La luce resta accesa 15 minuti dopo ogni apertura. Simulando minuto per minuto con python3 l'unione degli intervalli [t, t+15) per tutti i 16 orari, entro la finestra 8:00-10:00 risultano 25 minuti spenti. I tre buchi sono: 8:46-8:54 (8 min, dopo l'apertura delle 8:31), 9:26-9:29 (3 min, dopo le 9:11) e 9:46-10:00 (14 min, dopo le 9:31); 8+3+14 = 25.

<sub>confidenza: alta</sub>

### 208 → **C**

p = 30!. L'esponente di 3 si calcola con la formula di Legendre: floor(30/3)+floor(30/9)+floor(30/27) = 10+3+1 = 14. Quindi il massimo k è 14.

<sub>confidenza: alta</sub>

### 209 → **C**

n = 3^8 - 2^8 = 6561 - 256 = 6305. La fattorizzazione (python3) è 5 x 13 x 97. Quindi 5, 13, 97 e 65=5x13 sono divisori, mentre 35 = 5x7 non lo è perché 7 non compare tra i fattori primi.

<sub>confidenza: alta</sub>

### 210 → **E**

Se un tavolo ha 3 membri e gli altri 4 ciascuno, allora n-3 è multiplo di 4; analogamente con tavoli da 5, n-3 è multiplo di 5. Quindi n-3 è multiplo di 20 e, con 10<n<40, l'unico valore è n-3=20 cioè n=23. Dividendo 23 in tavoli da 6: 23 = 6x3 + 5, quindi il tavolo incompleto ha 5 membri. (Nel testo manca uno spazio dopo 'other tables,' — refuso del libro.)

<sub>confidenza: alta</sub>

### 211 → **B**

Sia D il numero totale di giorni previsti: le pagine totali sono 90D. Nei primi (D-6) giorni ha letto 75 pagine al giorno, e restano 690 pagine per gli ultimi 6 giorni, quindi 75(D-6) + 690 = 90D. Sviluppando: 75D - 450 + 690 = 90D, cioe' 240 = 15D e D = 16. Verifica: totale 90*16 = 1440 pagine; 75*10 = 750 nei primi 10 giorni, 1440 - 750 = 690, coerente.

<sub>confidenza: alta</sub>

### 212 → **D**

Da sqrt(r/s) = s, elevando al quadrato entrambi i membri (leciti perche' s > 0), si ottiene r/s = s^2. Moltiplicando per s: r = s^3. Corrisponde all'opzione D.

<sub>confidenza: alta</sub>

### 213 → **B**

Serve x/3 = p^2 con p primo, cioe' x = 3p^2. La condizione 3 < x < 100 diventa 1 < p^2 < 33.3, quindi p puo' essere 2, 3 o 5 (7 darebbe 3*49 = 147 > 100). I valori di x sono 12, 27 e 75: tre valori.

<sub>confidenza: alta</sub>

### 214 → **B**

Con n lettere i codici disponibili sono n singole lettere piu' C(n,2) coppie distinte in ordine alfabetico, cioe' n + n(n-1)/2. Per n = 4 si ottiene 4 + 6 = 10 < 12; per n = 5 si ottiene 5 + 10 = 15 >= 12. Il numero minimo e' quindi 5.

<sub>confidenza: alta</sub>

### 215 → **B**

h = -16(t-3)^2 + 150 e' una parabola con vertice in t = 3, quindi l'altezza massima (150 ft) si raggiunge a t = 3 s. Due secondi dopo, t = 5: h = -16(5-3)^2 + 150 = -16*4 + 150 = -64 + 150 = 86 piedi.

<sub>confidenza: alta</sub>

### 216 → **D**

Dalla prima disuguaglianza x + 6 > 10 segue x > 4 (stretta); dalla seconda x - 3 <= 5 segue x <= 8. L'intersezione e' 4 < x <= 8, cioe' l'opzione D.

<sub>confidenza: alta</sub>

### 217 → **C**

David ha d libri; d e' 3 volte quelli di Jeff, quindi Jeff = d/3; d e' la meta' di quelli di Paula, quindi Paula = 2d. Il totale e' d + d/3 + 2d = (3d + d + 6d)/3 = 10d/3.

<sub>confidenza: alta</sub>

### 218 → **C**

Ogni partita e' una coppia non ordinata di squadre distinte fra le 8, quindi il numero di partite e' C(8,2) = 8*7/2 = 28.

<sub>confidenza: alta</sub>

### 219 → **B**

Sia r la tariffa oraria regolare e t le ore stimate: rt = 336. Il lavoro ha richiesto t+4 ore con guadagno orario r-2, sempre per 336 dollari: (r-2)(t+4) = 336. Sottraendo: 4r - 2t - 8 = 0, cioe' t = 2r - 4; sostituendo in rt = 336 si ha 2r^2 - 4r - 336 = 0, r^2 - 2r - 168 = 0, r = 14 e t = 24. Verifica: 14*24 = 336 e 12*28 = 336.

<sub>confidenza: alta</sub>

### 220 → **E**

Con p, q interi positivi, p/q < 1 equivale a p < q. Allora q/p > 1 sempre (opzione E). Le altre non sono garantite: con p=1, q=2 si ha sqrt(1/2) < 1, p/q^2 = 1/4 < 1, p/2q = 1/4 < 1; e q/p^2 puo' essere <= 1, ad esempio p=3, q=4 da' 4/9 < 1.

<sub>confidenza: alta</sub>

### 221 → **A**

Separatamente: il pacco da 3 lb costa x + 2y e quello da 5 lb costa x + 4y, totale 2x + 6y. Combinati in un unico pacco da 8 lb: x + 7y. La differenza (2x + 6y) - (x + 7y) = x - y, positiva perche' x > y, quindi conviene combinare risparmiando x - y centesimi.

<sub>confidenza: alta</sub>

### 222 → **A**

Con r = 8, il tempo di raddoppio approssimato e' 70/8 = 8.75 anni. In 18 anni si hanno 18/8.75 circa 2.06 raddoppi, quindi approssimativamente 2 raddoppi: 5.000 -> 10.000 -> 20.000 dollari. Il calcolo esatto 5000*2^(18/8.75) da' circa 20.808, coerente con l'approssimazione di 20.000.

<sub>confidenza: alta</sub>

### 223 → **D**

La distanza arrotondata a 290 (decina piu' vicina) implica distanza reale in [285, 295); il carburante arrotondato a 12 galloni implica consumo reale in [11.5, 12.5). Il minimo di miglia/gallone si ottiene con distanza minima e carburante massimo: 285/12.5; il massimo con distanza massima e carburante minimo: 295/11.5. Numericamente l'intervallo e' circa 22.8-25.65, cioe' l'opzione D.

<sub>confidenza: alta</sub>

### 224 → **E**

Il segmento ombreggiato va da -5 a 3 (estremi inclusi): il centro e' (-5+3)/2 = -1 e il raggio (3-(-5))/2 = 4. La disuguaglianza e' quindi |x - (-1)| <= 4, cioe' |x + 1| <= 4, che restituisce -5 <= x <= 3.

<sub>confidenza: alta</sub>

### 225 → **D**

Ricavo totale su 10 giorni = 400*10 = 4.000 dollari. Primi 6 giorni: 360*6 = 2.160. Restano 4.000 - 2.160 = 1.840 per gli ultimi 4 giorni, media 1.840/4 = 460 dollari.

<sub>confidenza: alta</sub>

### 226 → **E**

Fattorizzando 3.150 = 2 * 3^2 * 5^2 * 7: gli esponenti dispari sono quelli di 2 e di 7, quindi il minimo y che rende il prodotto un quadrato e' 2*7 = 14. Verifica in Python: 3150*14 = 44.100 = 210^2, e nessun y < 14 funziona.

<sub>confidenza: alta</sub>

### 227 → **A**

La parte intera inferiore: [-1.6] = -2 (il piu' grande intero <= -1.6, non -1), [3.4] = 3, [2.7] = 2. Somma: -2 + 3 + 2 = 3.

<sub>confidenza: alta</sub>

### 228 → **C**

I risparmi settimanali sono 1, 2, 3, ..., 52 dollari. La somma e' 52*53/2 = 1.378 dollari (verificato con Python: sum(range(1,53)) = 1378).

<sub>confidenza: alta</sub>

### 229 → **C**

Applicando x_n = 2x_(n-1) - (1/2)x_(n-2): x_2 = 2*2 - 0.5*3 = 4 - 1.5 = 2.5; x_3 = 2*2.5 - 0.5*2 = 5 - 1 = 4. Il valore di x_3 e' quindi 4.

<sub>confidenza: alta</sub>

### 230 → **E**

Su distanza totale D, il tempo e' (xD/100)/40 + ((100-x)D/100)/60 = D[x/4000 + (100-x)/6000] = D(3x + 200 - 2x)/12000 = D(x+200)/12000. La velocita' media e' D diviso il tempo, cioe' 12.000/(x+200). Controllo numerico con x = 50 e D = 1200: tempo = 15 + 10 = 25 h, media 48 mph, e 12000/250 = 48.

<sub>confidenza: alta</sub>

### 231 → **A**

La cifra delle unità di 33^43 dipende solo da 3^43: il ciclo di 3 è 3,9,7,1 con periodo 4, e 43 mod 4 = 3, quindi unità 7. Per 43^33 conta 3^33: 33 mod 4 = 1, quindi unità 3. Somma 7+3 = 10, cifra delle unità 0. Verificato con python3: (33**43+43**33)%10 = 0.

<sub>confidenza: alta</sub>

### 232 → **D**

Le posizioni maschili sono fissate (1ª, 3ª, 5ª) e quelle femminili (2ª, 4ª, 6ª). I 3 maschi si dispongono nelle 3 posizioni maschili in 3! = 6 modi e le 3 femmine in 3! = 6 modi. Totale 6 × 6 = 36.

<sub>confidenza: alta</sub>

### 233 → **B**

d = 1/(2^3·5^7) = 1/(8·78125) = 1/625000. Moltiplicando numeratore e denominatore per 2^4 si ottiene 16/10^7 = 0,0000016. Le cifre non nulle sono 1 e 6, quindi due. Verificato con Decimal in python3: 0.0000016.

<sub>confidenza: alta</sub>

### 234 → **B**

I pari strettamente tra 99 e 301 vanno da 100 a 300. La somma è 2(50+51+...+150) = 2[(150·151/2) − (49·50/2)] = 2(11325 − 1225) = 2·10100 = 20200. Verificato con sum(range(100,301,2)) = 20200.

<sub>confidenza: alta</sub>

### 235 → **A**

Da 16 nov 2001 a 16 nov 2014 passano 13 anni; tre di essi (2004, 2008, 2012) hanno 366 giorni, gli altri 365. Giorni totali = 13·365 + 3 = 4748. 4748 mod 7 = 2 (7·678 = 4746). Venerdì + 2 giorni = domenica.

<sub>confidenza: alta</sub>

### 236 → **D**

Fattorizzo 7150 = 715·10 = (5·143)·(2·5) = 2·5^2·11·13. I fattori primi distinti sono 2, 5, 11 e 13, tutti compresi tra 1 e 100: quattro. Confermato in python3 elencando i primi ≤100 che dividono 7150: [2, 5, 11, 13].

<sub>confidenza: alta</sub>

### 237 → **D**

Per n ≥ 3 vale a_n = a_1·a_2·…·a_{n−1}, quindi a_{n+1} = (a_1·…·a_{n−1})·a_n = a_n·a_n = a_n^2. Con a_n = t si ha a_{n+1} = t^2 e a_{n+2} = (t^2)^2 = t^4. Controllo numerico: a_1=3, a_2=5, a_3=15, a_4=225 = 15^2, a_5 = 225^2 = 15^4.

<sub>confidenza: alta</sub>

### 238 → **D**

Il nuovo rapporto è P(1+k/100)/[E(1+m/100)] = (P/E)·(100+k)/(100+m). L'aumento percentuale è [(100+k)/(100+m) − 1]·100 = 100(k−m)/(100+m). Poiché k > m il risultato è positivo, coerente con un aumento.

<sub>confidenza: alta</sub>

### 239 → **D**

Su 300 soggetti: 120 palme sudate, 90 vomito, 225 vertigini, per un totale di 435 'occorrenze'. Detti a = esattamente uno, b = esattamente due = 0,35·300 = 105, c = esattamente tre: a+b+c = 300 e a+2b+3c = 435. Dalla prima a+c = 195; dalla seconda a+3c = 225, quindi 2c = 30, c = 15 e a = 180.

<sub>confidenza: alta</sub>

### 240 → **D**

m^{-1} = 1/m = −1/3 implica m = −3. Allora m^{-2} = 1/m^2 = 1/9 (positivo, perché il quadrato elimina il segno).

<sub>confidenza: alta</sub>

### 241 → **D**

Il prezzo 250 è un ricarico del 20% sul costo, quindi costo unitario = 250/1,2 ≈ 208,33 e costo totale 60·208,33 = 12.500. Ricavi: 54 vendute a 250 = 13.500, più rimborso su 6 pari a 6·(208,33·0,5) = 625, totale 14.125. Profitto = 1.625, cioè 1625/12500 = 13% di guadagno (verificato con python3).

<sub>confidenza: alta</sub>

### 242 → **D**

Somma delle 7 lunghezze = 7·68 = 476, mediana (4° valore) = 84, e a7 = 4a1 + 14. Per massimizzare a7 bisogna massimizzare a1, quindi minimizzare gli altri: a2 = a3 = a1 e a5 = a6 = 84. Allora 3a1 + 84 + 168 + (4a1+14) = 476 → 7a1 = 210 → a1 = 30 e a7 = 4·30+14 = 134 (verifica: 30+30+30+84+84+84+134 = 476).

<sub>confidenza: alta</sub>

### 243 → **E**

Con termine generale n + 2^{n−1}: sesto termine = 6 + 2^5 = 38, quinto termine = 5 + 2^4 = 21. Differenza = 38 − 21 = 17.

<sub>confidenza: alta</sub>

### 244 → **E**

Per rendere il prodotto minimo (più negativo possibile) servono modulo massimo e segno negativo: si sceglie 10 in valore assoluto per tutti i 20 fattori e un numero dispari di negativi. Prendendo 19 volte −10 e una volta +10 si ottiene (−10)^19·10 = −10^20, che è ammesso perché le ripetizioni sono consentite. Quindi il minimo è −(10)^20.

<sub>confidenza: alta</sub>

### 245 → **D**

Le stringhe distinte con D, G, I, I, T sono 5!/2! = 60. Quelle con le due I adiacenti si contano incollandole in un blocco: 4! = 24 disposizioni di {II, D, G, T}. Le I separate da almeno una lettera sono 60 − 24 = 36; verificato per enumerazione esaustiva in python3 (36 su 60).

<sub>confidenza: alta</sub>

### 246 → **D**

Osservo che 0,99999999 = 1 − 10^{-8} = (1 − 10^{-4})(1 + 10^{-4}), quindi il primo quoziente è 1 − 10^{-4} = 0,9999. Analogamente 0,99999991 = 1 − 9·10^{-8} = (1 − 3·10^{-4})(1 + 3·10^{-4}), quindi il secondo è 0,9997. La differenza è 0,0002 = 2·10^{-4}, confermata con Decimal ad alta precisione.

<sub>confidenza: alta</sub>

### 247 → **D**

Prendo 100 giornali venduti: p copie di A (ricavo p dollari) e 100 − p di B (ricavo 1,25(100−p) = 125 − 1,25p). Ricavo totale = 125 − 0,25p. Quindi r = 100·p/(125 − 0,25p); moltiplicando numeratore e denominatore per 4 si ottiene 400p/(500 − p).

<sub>confidenza: alta</sub>

### 248 → **E**

La produzione totale dei primi n giorni è 50n; aggiungendo 90 la media su n+1 giorni diventa 55: 50n + 90 = 55(n+1). Da cui 50n + 90 = 55n + 55, cioè 5n = 35 e n = 7.

<sub>confidenza: alta</sub>

### 249 → **A**

Sia il numero 10a + b; invertendo si ottiene 10b + a e la differenza è |9(a − b)| = 27, quindi |a − b| = 3. Esempio: 41 e 14 differiscono di 27 e le cifre differiscono di 3.

<sub>confidenza: alta</sub>

### 250 → **D**

Da 1/r = 1/x + 1/y = (y + x)/(xy) segue r = xy/(x + y), la classica formula delle resistenze in parallelo.

<sub>confidenza: alta</sub>

### 251 → **E**

Eventi indipendenti: serve Xavier SI, Yvonne SI, Zelda NO. P = (1/4)·(1/2)·(1 - 5/8) = (1/4)·(1/2)·(3/8) = 3/64. Verificato con Fraction in python3: 3/64.

<sub>confidenza: alta</sub>

### 252 → **C**

1/x - 1/(x+1) = [(x+1)-x]/[x(x+1)] = 1/(x²+x). Uguagliando a 1/(x+4) si ottiene x²+x = x+4, cioè x² = 4, quindi x = 2 oppure x = -2. Fra le opzioni compare solo -2; verifica: 1/(-2) - 1/(-1) = -0,5 + 1 = 0,5 = 1/(−2+4) = 1/2. Corretto.

<sub>confidenza: alta</sub>

### 253 → **B**

Esponenti negativi invertono le frazioni: (1/2)^-3 = 2³ = 8, (1/4)^-2 = 4² = 16, (1/16)^-1 = 16. Prodotto = 8·16·16 = 2048 = 2^11 = (1/2)^-11. Nota il refuso del libro: le opzioni A... in realtà C ed E sono identiche ((1/2)^-6), ma la risposta corretta è comunque B.

<sub>confidenza: alta</sub>

### 254 → **B**

10 decimali hanno cifra dei decimi pari e vengono arrotondati per eccesso (guadagno 1-f, con f parte frazionaria: sta strettamente fra 0,1 e 1), 20 hanno cifra dispari e vengono arrotondati per difetto (perdita f, fra 0,1 incluso e 1). Quindi E-S = somma guadagni (in (1,10)) meno somma perdite (in [2,20)), cioè E-S ∈ (-19, 8): 10 è impossibile. -16 si realizza p.es. con 20 numeri a f=0,95 (perdita 19) e 10 numeri di guadagno complessivo 3 (nove con f=0,68 e uno con f=0,88): 3-19=-16. 6 si realizza con 20 numeri a f=0,1 (perdita 2) e 10 numeri con f=0,2 (guadagno 0,8 ciascuno, totale 8): 8-2=6. Quindi solo I e II.

<sub>confidenza: alta</sub>

### 255 → **C**

Moltiplicando per x (x≠0): 5x - 6 = x², cioè x² - 5x + 6 = 0, che fattorizza in (x-2)(x-3)=0. Radici x=2 e x=3, entrambe diverse da 0 e quindi accettabili: due valori possibili.

<sub>confidenza: alta</sub>

### 256 → **B**

Sia x la frazione in peso della miscela X. Il loietto (ryegrass) totale: 0,40x + 0,25(1-x) = 0,30 → 0,15x = 0,05 → x = 1/3, cioè 33 1/3%. (La bluegrass e la fescue non servono al conto.)

<sub>confidenza: alta</sub>

### 257 → **D**

Punti critici: x=-3, x=-2 (zeri) e x=2 (escluso, denominatore nullo). Segno: x<-3 negativo; -3≤x<-2 non negativo (numeratore ≤0, denominatore <0); -2<x<2 negativo; x>2 positivo. Interi <5 che soddisfano: -3, -2, 3, 4 → 4 interi. Controllo in python3 su range(-20,5): [-3,-2,3,4].

<sub>confidenza: alta</sub>

### 258 → **D**

Su 150 case: AC=90, veranda=75, piscina=45, somma delle tre categorie = 210. Case con almeno una dotazione = 150 - 5 = 145. Con a = esattamente una, b = esattamente due, c = 3 = 5: a+b+5 = 145 → a+b = 140; a+2b+3·5 = 210 → a+2b = 195. Sottraendo: b = 55.

<sub>confidenza: alta</sub>

### 259 → **C**

Raccolgo 2^-17: 2^-14+2^-15+2^-16+2^-17 = 2^-17(8+4+2+1) = 15·2^-17. Diviso 5 dà 3·2^-17, quindi è 3 volte 2^-17. Verifica numerica in python3: rapporto = 3.0.

<sub>confidenza: alta</sub>

### 260 → **E**

Un decimale è finito se il denominatore ridotto ha solo fattori 2 e 5. 189=3³·7, 196=2²·7², 225=3²·5², 144=2⁴·3² contengono fattori 3 o 7 (e le frazioni sono già ridotte o restano con quei fattori). 128 = 2⁷ e 39 è dispari e non divisibile per 2: 39/128 = 0,3046875, decimale finito.

<sub>confidenza: alta</sub>

### 261 → **D**

Primo membro: (1/5)^m·(1/4)^18 = 1/(5^m·2^36). Secondo membro: 1/(2·10^35) = 1/(2·2^35·5^35) = 1/(2^36·5^35). Uguagliando gli esponenti di 5: m = 35 (quelli di 2 coincidono già, 36=36).

<sub>confidenza: alta</sub>

### 262 → **D**

Casi totali: C(8,4) = 70. Casi favorevoli: Andrew incluso, Karen esclusa, quindi si scelgono i restanti 3 posti fra gli altri 6 volontari: C(6,3) = 20. Probabilità = 20/70 = 2/7 (verificato con math.comb).

<sub>confidenza: alta</sub>

### 263 → **C**

Prezzo di acquisto 100·(6+1/18) = 605,56 $; con la commissione del 2% l'esborso è 605,56·1,02 = 617,67 $. Vendita 100·24 = 2400 $, al netto del 2% incassa 2400·0,98 = 2352 $. Guadagno percentuale = (2352-617,67)/617,67 = 280,8% → 280%. Nota: '6 1/18' è quasi certamente un refuso del libro per 6 1/8, ma anche con 6,125 il risultato è 276,5%, sempre più vicino a 280%.

<sub>confidenza: alta</sub>

### 264 → **D**

x = 150!. L'esponente di 5 in 150! si calcola con Legendre: floor(150/5) + floor(150/25) + floor(150/125) = 30 + 6 + 1 = 37. Quindi il massimo y con 5^y divisore è 37.

<sub>confidenza: alta</sub>

### 265 → **D**

Somma dei primi cinque = 9+7+10+4+6 = 36. Con 3: somma 39, media 6,5; ordinati 3,4,6,7,9,10 → mediana (6+7)/2 = 6,5 → uguali. Con 7: somma 43, media ≈7,17; ordinati 4,6,7,7,9,10 → mediana 7 → diverse. Con 12: somma 48, media 8; ordinati 4,6,7,9,10,12 → mediana (7+9)/2 = 8 → uguali. Quindi I e III.

<sub>confidenza: alta</sub>

### 266 → **E**

Il ricarico è il 40% del PREZZO DI VENDITA, non del costo: S = 150 + 0,4S → 0,6S = 150 → S = 250. Profitto lordo = 250 - 150 = 100 $.

<sub>confidenza: alta</sub>

### 267 → **C**

Un quadrato è dispari se la base è dispari. Servono n dispari con 10 < n² < 1000: n=5 (25) fino a n=31 (961), perché 3²=9<10 e 33²=1089>1000. I dispari da 5 a 31 sono (31-5)/2+1 = 14. Conteggio verificato in python3: 14.

<sub>confidenza: alta</sub>

### 268 → **A**

Bilancio del grasso: 0,01x + 0,02y + 0,03z = 0,015(x+y+z). Moltiplicando per 1000: 10x + 20y + 30z = 15x + 15y + 15z → 5y + 15z = 5x → x = y + 3z.

<sub>confidenza: alta</sub>

### 269 → **D**

Selezioni totali di 4 libri su 8: C(8,4) = 70. Selezioni senza alcun tascabile (solo fra i 6 rilegati): C(6,4) = 15. Con almeno un tascabile: 70 - 15 = 55.

<sub>confidenza: alta</sub>

### 270 → **E**

√4 = 2 esatto; ⁴√4 = √2 ≈ 1,4142; ∛4 ≈ 1,5874. Somma ≈ 5,0016, quindi maggiore di 4. Già solo 2 + 1,4142 + 1,5 > 4 basta a concludere.

<sub>confidenza: alta</sub>

### 271 → **D**

Altezza al termine dell'anno n: 4 + nd. La condizione 'a fine 6° anno era 1/5 più alto che a fine 4° anno' dà 4+6d = (6/5)(4+4d) → 20+30d = 24+24d → 6d = 4 → d = 2/3 piedi l'anno. Verifica: 4+4(2/3)=6,667 e 4+6(2/3)=8 = 6,667·1,2.

<sub>confidenza: alta</sub>

### 272 → **A**

Con 13 note ci sono 12 intervalli di rapporto costante r, e r^12 = 2 (la più alta è doppia della più bassa), quindi r = 2^(1/12). La settima nota è la prima moltiplicata per r^6: 440·2^(6/12) = 440·√2 ≈ 622,25. (L'opzione D, 440·2^(7/12), corrisponderebbe all'ottava nota.)

<sub>confidenza: alta</sub>
