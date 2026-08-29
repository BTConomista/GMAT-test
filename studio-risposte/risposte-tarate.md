# Risposte ragionate — prova tarata

> ⚠️ **Materiale di studio, non una fonte.** Le risposte ufficiali stanno in
> [`book/ch04.md`](../book/ch04.md) §4.3. Dove le due si contraddicono, ha ragione `ch04.md`.
> Vedi [README.md](README.md).

## Come è stato prodotto

Stesso compito di `risposte-ragionate.md`, procedimento diverso.

**Fase 1 — taratura.** Un agente ha risolto le domande **1–29 da solo**, fissato le sue
lettere, e *solo dopo* ha aperto la chiave ufficiale in §4.3 per confrontarsi. Punteggio:
**29/29**.

**Fase 2 — risoluzione.** Le restanti 238 domande sono state risolte da dodici agenti che
avevano in mano le **28 lezioni operative** ricavate dalla fase 1.

Poiché la taratura non ha prodotto errori, le lezioni non sono correzioni ma **le accortezze
che hanno evitato i distrattori** — cioè le trappole viste da vicino e disinnescate, scritte
in forma applicabile.

Il confronto con la prova cieca è in [`divergenze.md`](divergenze.md).

---

## Le 28 lezioni ricavate dalla taratura

Sono la parte di questo file che vale indipendentemente dalle risposte: descrivono i
**distrattori tipici** del GMAT quantitativo e come non caderci.


1. Nelle probabilita' con eventi complementari ('meno di 25 anni'), calcolare prima la quantita' esplicitamente data (la percentuale dei 25+ pesata: 0.48*0.40 + 0.52*0.20 = 0.296) e poi sottrarre da 1: e' meno soggetto a errori che sommare direttamente i complementi ramo per ramo, e impedisce di rispondere 0.30 (che e' il complemento sbagliato, cioe' proprio il valore intermedio 0.296 arrotondato).

2. Nei problemi di estrazione senza reimmissione con condizione gia' verificata ('le prime 2 carte NON sono X'), aggiornare SOLO il denominatore quando le carte estratte non erano del tipo cercato: 8/46, non 6/46. Prima di calcolare, chiedersi esplicitamente: il numeratore cambia o no?

3. Nei problemi di media, convertire subito la media in TOTALE (media x numero di elementi) e lavorare sui totali: 80x4 = 320, poi 320 - 233 = 87. Non manipolare le medie direttamente.

4. Nelle commissioni/tariffe a scaglioni, applicare la percentuale alta SOLO all'eccedenza: 20% di (1300-500) = 160, non 20% di 1300. Il distrattore e' quasi sempre il calcolo che applica l'aliquota alta all'intero importo.

5. Nelle domande con elenchi I/II/III testare ogni caso separatamente fino in fondo, ricalcolando SIA la media SIA la mediana da zero per ogni valore: la mediana va sempre ricavata riordinando la lista aggiornata, non riusando l'ordinamento precedente.

6. Per liste di interi consecutivi (pari, dispari o qualsiasi), la media e' il termine centrale: per n dispari termini a passo 2 partendo da a, media = a + (n-1). Per 10 dispari: a+9; per 5 pari: b+4. Cosi' la differenza si ottiene simbolicamente senza scrivere le liste.

7. Mediana = valore centrale della lista ORDINATA, mai il valore centrale della tabella nell'ordine in cui e' presentata. Riordinare sempre prima di leggere. Il distrattore A in questi item e' tipicamente la media, non la mediana.

8. In somme telescopiche verificare la cancellazione a coppie e tenere solo primo e ultimo termine (1/2 - 1/6 = 1/3), invece di sommare tutte le frazioni.

9. Nei problemi su retta numerata, dedurre dal disegno l'ORDINE delle grandezze assolute: se q sta piu' vicino a -1 di r, allora |q| > |r|. Poi confrontare i prodotti per segno prima e per modulo dopo: i prodotti negativi si scartano subito, tra i positivi vince quello con i moduli maggiori.

10. Nelle ripartizioni proporzionali, impostare l'unita' base come incognita e contare quante unita' totali (2 proprietari x 3 + 10 dipendenti x 1 = 16 unita'), poi moltiplicare per il numero di unita' della persona richiesta. Rileggere se chiede la quota di UNO o di TUTTI (qui: ciascun proprietario = 3x = 9.000, non 18.000).

11. Nei cambi valuta a due passaggi, seguire la catena di unita' passo per passo (500 $ -> 400 euro -> resta 1/4 = 100 euro -> 120 $) e non moltiplicare i due tassi tra loro: la frazione spesa nel mezzo rompe la moltiplicazione diretta.

12. Nei conteggi da figura, contare per etichetta e trascrivere i conteggi separati (x=5, y=3, v=2, w=2, totale 12) e verificare che la somma dia il totale dichiarato PRIMA di formare il rapporto: e' il controllo che intercetta un conteggio saltato.

13. Nei sistemi simmetrici a tre equazioni a coppie (x+y, y+z, x+z), sommare tutte e tre e dividere per 2 per ottenere x+y+z, poi sottrarre l'equazione che non contiene l'incognita cercata. Attenzione a quale lettera e' chiesta: 'verdi in R' = z, non x.

14. 'Massimo numero di gruppi identici usando TUTTO' = MCD delle quantita', non la somma ne' il rapporto. MCD(15,85)=5.

15. Quando si confrontano cinque rapporti, calcolarli tutti numericamente con la calcolatrice invece di stimarli: qui B (5,45) e D (5,21) sono vicini e a occhio si scambiano, mentre il minimo vero e' C (3,95).

16. Nelle 'tariffe orarie effettive', il numeratore e' la paga effettiva e il denominatore il tempo TOTALE indicato dal problema, inclusi i tempi non pagati: 90 / 7,5 = 12.

17. Nelle conversioni di unita' composte, dividere le due grandezze per hour: (32 miglia/h)/(24 gal/h) = 4/3 miglia per gallone. Il reciproco (3/4) e' sempre tra le opzioni: controllare quale unita' e' al numeratore nella domanda.

18. Quando l'enunciato sottolinea l'unita' di misura (es. 'quanti SECONDI'), fare la conversione come ultimo passo e riscriverla: 1/30 di ora = 120 secondi. Le opzioni contengono di norma sia il valore in ore sia quello in secondi.

19. In 'increased/decreased by a factor of 1/n' interpretare come variazione relativa: aumento -> x(1+1/n), diminuzione -> x(1-1/n). Poi impostare l'equazione all'indietro dal valore noto finale, invece di riapplicare in avanti.

20. Nei problemi di lavoro congiunto 'per lo stesso tempo', calcolare le due velocita' in unita' comuni (R = 10.000/9, S = 5.000/3 = 15.000/9) e fare la quota come rate/(somma rate): il tempo si semplifica e non serve conoscerlo.

21. Nei problemi di monete/miscele, usare la sostituzione 'tutto del tipo economico': 16 x 10 = 160 centesimi, differenza 235-160 = 75, divisa per la differenza unitaria 15 = 5 pezzi da 25. Piu' veloce e meno soggetto a errori del sistema a due incognite.

22. Nei problemi di profitto, portare acquisto e vendita alla STESSA quantita' fisica prima di sottrarre (5 dozzine = 60 uova; costo 5x2,80 = 14; ricavo 20x0,90 = 18; profitto 4). Le opzioni includono sempre il ricavo lordo e il costo come distrattori.

23. 'Divisibile sia per 2 SIA per 3' significa divisibile per 6 (non l'unione dei multipli di 2 e di 3). Poi applicare inclusione-esclusione e verificare l'intersezione con l'altro insieme (mcm 6 e 7 = 42 > 24, quindi nessuna sovrapposizione).

24. Nei confronti tra piani retributivi, uguagliare le due espressioni complete e risolvere per l'incognita richiesta, controllando che la percentuale sia applicata alla base giusta (0,20S, non 0,20 dello stipendio).

25. Per confrontare espressioni algebriche con vincoli d'ordine (1<x<y<z), fare le differenze a coppie e semplificare invece di sostituire numeri: E-B = z(x-1)>0, E-D = x(z-y)>0, E-C = y(z-x)>0. La sostituzione numerica va usata solo come verifica, perche' un solo esempio non prova il 'must'.

26. Nei problemi su insiemi ottenuti per traslazione, contare la CARDINALITA' dell'unione tenendo conto delle sovrapposizioni: con 8 interi consecutivi, X+4 e X-4 si sovrappongono e l'unione va da min-4 a max+4, cioe' 16 elementi (non 8+8=16 per caso: verificare sempre l'unione elencando gli estremi). E rispondere alla differenza chiesta (16-8=8), non alla cardinalita' di Y.

27. Nelle approssimazioni, non arrotondare i fattori prima di dividere se le opzioni sono vicine (12 vs 13): calcolare 1,03 x 4,86 = 5,0058 e poi dividere.

28. Nei problemi con tre categorie legate a catena, esprimere TUTTO in funzione della categoria richiesta (h) prima di sommare: h + (h+20) + 2(h+20) = 140. Cosi' si risolve direttamente l'incognita chiesta e non se ne ricava un'altra da riconvertire.


## Tipologie di domanda risultate insidiose

- Probabilita' con complemento richiesto ('meno di X'): il valore intermedio calcolato compare tra le opzioni come distrattore (dom. 1)

- Probabilita' condizionata senza reimmissione: rischio di aggiornare anche il numeratore quando non serve (dom. 2)

- Tariffe e commissioni a scaglioni: rischio di applicare l'aliquota alta all'intero importo (dom. 4)

- Media contro mediana su liste piccole: rischio di leggere il valore centrale della tabella invece che della lista ordinata, o di rispondere con la media (dom. 5, 7)

- Formulazioni ambigue 'increased/decreased by a factor of 1/n': l'interpretazione moltiplicativa alternativa (x1/4) porterebbe a un risultato diverso; qui l'ambiguita' e' del libro (dom. 20)

- Conversioni di unita' composte e reciproci (miglia/gallone contro galloni/miglio, ore contro secondi): il reciproco e il valore non convertito sono sempre tra le opzioni (dom. 18, 19)

- Confronto di piu' rapporti numericamente vicini in tabella: B (5,45) e D (5,21) si confondono a stima (dom. 15)

- Confronto algebrico di espressioni con vincoli d'ordine: verificare con un solo esempio numerico non prova il 'must be' (dom. 26)

- Domande che chiedono una quantita' derivata (differenza, quota individuale, complemento) e non quella appena calcolata (dom. 10, 27)

- Approssimazioni con opzioni adiacenti (12 vs 13): l'arrotondamento anticipato dei fattori puo' far cadere nell'opzione sbagliata (dom. 28)

- Lettura di conteggi da figure ASCII: rischio di saltare una casella se non si verifica che i conteggi sommino al totale dichiarato (dom. 12)

- Linguaggio di divisibilita' 'divisibile sia per 2 sia per 3' da tradurre in 'divisibile per 6', piu' inclusione-esclusione (dom. 24)


---

## Legenda

**Fase**: `taratura` = risolta nella fase 1 e confrontata con la chiave ufficiale;
`tarata` = risolta nella fase 2, con le lezioni già in mano.

**Confidenza** dichiarata da chi ha risolto: **alta** (calcolo verificato, coincide con
un'opzione), **media** (ragionamento solido ma enunciato ambiguo), **bassa** (non convinto).

---

### 1 → **B**

Probabilita' di avere 25 anni o piu': 0,48 x 0,40 = 0,192 per chi si identifica come maschio e 0,52 x 0,20 = 0,104 per chi si identifica come femmina, totale 0,296. La domanda chiede il complemento, cioe' meno di 25 anni: 1 - 0,296 = 0,704, circa 0,70. Nota: 0,30 e' il distrattore che corrisponde ai 25+ arrotondati.

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 2 → **E**

Le prime 2 carte estratte non rappresentano azioni, quindi restano 46 carte di cui ancora tutte e 8 le carte-azione. La probabilita' che la terza sia un'azione e' 8/46 = 4/23.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 3 → **D**

Media 80 su 4 persone significa un totale di 4 x 80 = 320 miglia. Carmen, Juan e Maria hanno percorso 72 + 78 + 83 = 233 miglia. Quindi Rafael ha percorso 320 - 233 = 87 miglia.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 4 → **C**

Commissione a scaglioni: 15% sui primi 500 $ = 75 $; l'eccedenza e' 1.300 - 500 = 800 $, su cui il 20% = 160 $. Totale 75 + 160 = 235 $. Il distrattore D (260 $) corrisponde a 20% di 1.300.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 5 → **D**

I primi quattro lotti sommano 2+4+3+5 = 14. Con 1: totale 15, media 3; lista ordinata 1,2,3,4,5, mediana 3 -> uguali. Con 2: totale 16, media 3,2; lista 2,2,3,4,5, mediana 3 -> diversi. Con 6: totale 20, media 4; lista 2,3,4,5,6, mediana 4 -> uguali. Quindi I e III.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 6 → **D**

Sia a il minimo di S (10 dispari consecutivi): la media e' il valore centrale = a + 9. Sia b il minimo di T (5 pari consecutivi): media = b + 4. Dato a = b + 7, la differenza delle medie e' (b+7+9) - (b+4) = 12.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 7 → **E**

I valori sono 5, 4, 3, 4, 2; ordinati: 2, 3, 4, 4, 5. Con 5 valori la mediana e' il terzo, cioe' 4. (La media sarebbe 18/5 = 3,6, che e' il distrattore D.)

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 8 → **C**

La somma e' telescopica: tutti i termini intermedi (-1/3 con +1/3, -1/4 con +1/4, -1/5 con +1/5) si cancellano, restano 1/2 - 1/6 = 3/6 - 1/6 = 2/6 = 1/3.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 9 → **A**

Dalla figura: p < -1, poi -1 < q < r < 0, poi 0 < s < 1. Quindi q e r sono negativi con |q| > |r| (q e' piu' vicino a -1), e |p| > 1. I prodotti qs e rs sono negativi (scartati). Tra i positivi: pq = |p||q|, pr = |p||r|, qr = |q||r|. Poiche' |q| > |r| si ha pq > pr, e poiche' |p| > 1 > |q| si ha pq > qr. Il massimo e' pq.

<sub>confidenza: alta · fase: taratura · ufficiale: **A** · ✅ corretta</sub>

### 10 → **B**

Sia x la quota di ciascun dipendente; ogni proprietario riceve 3x. Totale: 2(3x) + 10x = 16x = 48.000, quindi x = 3.000 e ciascun proprietario riceve 3x = 9.000 $. La domanda chiede quanto riceve CIASCUN proprietario, non i due insieme (18.000).

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 11 → **D**

500 $ x 0,80 = 400 euro ricevuti. Ne spende 3/4, quindi le restano 400/4 = 100 euro. Ricambiati a 1,20 $ per euro danno 100 x 1,20 = 120 $.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 12 → **E**

Conteggio dalla figura: x compare 3 volte in alto e 2 in basso = 5; y 2 in alto e 1 in basso = 3; v 1 in alto e 1 in basso = 2; w 2 in basso = 2. Verifica: 5+3+2+2 = 12, coerente col totale. Quindi (x o y) : (v o w) = 8 : 4 = 2:1.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 13 → **D**

Dalle righe della tabella: x + y = 80, y + z = 120, x + z = 160. Sommando: 2(x+y+z) = 360, quindi x+y+z = 180. Le verdi in R sono z = 180 - (x+y) = 180 - 80 = 100.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 14 → **B**

Tutti i bouquet devono avere lo stesso rapporto bianchi:rossi e usare tutti i fiori, quindi il numero di bouquet deve dividere sia 15 sia 85. Il massimo e' MCD(15,85) = 5 (3 bianchi e 17 rossi per bouquet).

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 15 → **C**

Calcolo il rapporto smaltito/riciclato per ciascuna contea: A = 142.800/16.700 = 8,55; B = 48.000/8.800 = 5,45; C = 51.400/13.000 = 3,95; D = 20.300/3.900 = 5,21; E = 16.200/3.300 = 4,91. Il minimo e' C.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 16 → **E**

125% = 1,25; 1,25 x 5 = 6,25. Il distrattore A (5,125) nasce dal leggere '125%' come '+0,125'.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 17 → **E**

Paga giornaliera: 6 ore x 15 $ = 90 $. Tempo totale considerato: 6 ore di lavoro + 1,5 ore di viaggio = 7,5 ore. Tariffa effettiva = 90/7,5 = 12 $ l'ora.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 18 → **D**

Miglia per gallone = (32 miglia/ora) / (24 galloni/ora) = 32/24 = 4/3. Il distrattore B (3/4) e' il reciproco, cioe' galloni per miglio.

<sub>confidenza: alta · fase: taratura · ufficiale: **D** · ✅ corretta</sub>

### 19 → **E**

A 30 mm all'ora, 1 mm richiede 1/30 di ora. Convertendo: (1/30) x 3.600 = 120 secondi. L'enunciato sottolinea 'seconds', quindi la conversione e' il passaggio decisivo.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 20 → **B**

Interpreto 'increased by a factor of 1/4' come aumento di 1/4, cioe' moltiplicazione per 5/4, e 'decreased by a factor of 1/3' come moltiplicazione per 2/3. Detto N il numero nel 2000: N x (5/4) x (2/3) = 100, cioe' N x (5/6) = 100, da cui N = 120.

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 21 → **C**

Velocita' di R = 10.000/9 scatole all'ora; velocita' di S = 5.000/3 = 15.000/9 scatole all'ora. Lavorando per lo stesso tempo, la quota di R e' 10.000/(10.000+15.000) = 10.000/25.000 = 40%. Il tempo si semplifica e non serve conoscerlo.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 22 → **B**

Se tutte e 16 le monete fossero da 10 centesimi il totale sarebbe 160 centesimi; il totale reale e' 235. La differenza 75 centesimi, divisa per la differenza unitaria 25-10 = 15, da' 5 monete da 25 centesimi. Verifica: 5 x 25 + 11 x 10 = 125 + 110 = 235.

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 23 → **C**

Costo: 5 dozzine x 2,80 = 14,00 $. Ricavo: 5 dozzine = 60 uova, vendute a 3 per 0,90 $, cioe' 20 gruppi x 0,90 = 18,00 $. Profitto lordo = 18,00 - 14,00 = 4,00 $. Il distrattore E (12,00) e' il ricavo per dozzina mal calcolato, D (11,30) e' un altro errore di unita'.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 24 → **C**

Divisibili sia per 2 sia per 3 significa divisibili per 6: 6, 12, 18, 24 -> 4 carte. Divisibili per 7: 7, 14, 21 -> 3 carte. L'intersezione richiederebbe multipli di 42, che non esistono entro 24, quindi nessuna sovrapposizione: 4 + 3 = 7 carte su 24, cioe' 7/24.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 25 → **C**

Uguaglio i due piani: 35.000 = 10.000 + 0,20 x S. Quindi 0,20 S = 25.000 e S = 125.000 $.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 26 → **E**

Con 1 < x < y < z confronto per differenze: E - B = (zx + zy) - (zy + z) = z(x - 1) > 0, quindi E > B, e B > A perche' y > x. E - D = (zx + zy) - (yx + yz) = x(z - y) > 0, quindi E > D. E - C = (zx + zy) - (xy + xz) = y(z - x) > 0, quindi E > C. Percio' z(x + y) e' il maggiore.

<sub>confidenza: alta · fase: taratura · ufficiale: **E** · ✅ corretta</sub>

### 27 → **C**

Prendo X = {1,...,8}. Allora X+4 = {5,...,12} e X-4 = {-3,...,4}; l'unione Y va da -3 a 12, cioe' 16 interi distinti (gli intervalli si toccano senza lasciare buchi). La domanda chiede QUANTI IN PIU', cioe' 16 - 8 = 8.

<sub>confidenza: alta · fase: taratura · ufficiale: **C** · ✅ corretta</sub>

### 28 → **B**

1,03 x 4,86 = 5,0058; 60,2 / 5,0058 = 12,03. L'opzione piu' vicina e' 12. Con arrotondamenti grossolani (60/5 = 12) si conferma, ma il calcolo esatto serve perche' 12 e 13 sono opzioni adiacenti.

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 29 → **B**

Sia h il numero di libri cartonati di saggistica. I tascabili di saggistica sono h + 20 e i tascabili di narrativa sono 2(h + 20). Totale: h + (h + 20) + 2(h + 20) = 4h + 60 = 140, quindi h = 20. Verifica: 20 + 40 + 80 = 140.

<sub>confidenza: alta · fase: taratura · ufficiale: **B** · ✅ corretta</sub>

### 30 → **B**

Somma prima gli addendi: 1,4 + 1/5 = 1,4 + 0,2 = 1,6. Poi applica la percentuale: 0,35 x 1,6 = 0,56. Verificato con python (0,56). Il distrattore A (0,42) e' 35% di 1,2 e D/E derivano dal sommare senza convertire 1/5 in 0,2.

<sub>confidenza: alta · fase: tarata</sub>

### 31 → **A**

Porto al denominatore comune 50: x/50 + x/25 = x/50 + 2x/50 = 3x/50. Il rapporto con x e' 3/50 = 0,06, cioe' il 6%. La x si semplifica, quindi il risultato non dipende dal valore (purche' x>0). Confermato con frazioni esatte in python: 3/50.

<sub>confidenza: alta · fase: tarata</sub>

### 32 → **E**

Domanda di conversione di unita' composte (categoria insidiosa): tengo separate le due grandezze rispetto al tempo. Consumo = 5 gal / 2 h = 2,5 gal/h, quindi 3,75 gal corrispondono a 3,75/2,5 = 1,5 ore = 90 minuti. Velocita' = 1 miglio/minuto, quindi in 90 minuti percorre 90 miglia. I distrattori (36, 40, 80) nascono da usare ore al posto di minuti o dal reciproco del consumo.

<sub>confidenza: alta · fase: tarata</sub>

### 33 → **A**

Il termine 1/999 e' circa 0,001, del tutto trascurabile rispetto a 100: il denominatore vale ~100,001. Quindi 999/100,001 = 9,9899, che tra le opzioni (10, 1, 0,1, 0,01, 0,001, distanziate per ordini di grandezza) e' chiaramente vicinissimo a 10. Calcolo verificato in python: 9,9899.

<sub>confidenza: alta · fase: tarata</sub>

### 34 → **B**

Pongo Y = 100, quindi X = 50 (X e' il 50% di Y). Il totale X+Y = 150 e la quota richiesta e' 50/150 = 1/3 = 33 1/3%. Attenzione al distrattore D (50%), che e' il dato di partenza e non la quantita' richiesta (rapporto sul TOTALE, non su Y). Verificato con frazioni: 1/2 diviso 3/2 = 1/3.

<sub>confidenza: alta · fase: tarata</sub>

### 35 → **E**

Ci sono due scenari. Se i 450 dollari sono il prezzo di vendita della bici costata 250, il profitto su quella e' 200 e l'altro sarebbe 250-200 = 50, che non compare tra le opzioni. Se invece i 450 sono la vendita della bici costata 375, il profitto e' 75 e l'altro profitto e' 250-75 = 175, presente come opzione E. La domanda chiede cosa PUO' essere, quindi basta uno scenario coerente: 175. Nota: 75 (opzione A) e' il profitto sulla bici venduta, non su 'the other', tipico distrattore della quantita' derivata.

<sub>confidenza: alta · fase: tarata</sub>

### 36 → **E**

Da k^2 = m^2 segue k^2 - m^2 = 0, cioe' (k-m)(k+m) = 0, quindi k = m oppure k = -m: nessuna delle due singolarmente e' obbligata (con k=2, m=-2 fallisce A e C; con k=2, m=2 fallisce B e D). L'unica affermazione sempre vera e' |k| = |m|, che equivale esattamente a k^2 = m^2. Ho verificato le controprove con coppie numeriche invece di fidarmi di un solo esempio, come richiesto dalle domande 'must be true'.

<sub>confidenza: alta · fase: tarata</sub>

### 37 → **D**

Ripartizione proporzionale: unita' totali = 15 + 20 + 30 = 65 ore. Il valore dell'ora e' 780/65 = 12 dollari. Makoto ha lavorato 15 ore, quindi riceve 15 x 12 = 180 dollari (opzione D). Ho controllato che la domanda chieda la quota di UNO solo (Makoto) e non il totale; verifica di coerenza: 180 + 240 + 360 = 780.

<sub>confidenza: alta · fase: tarata</sub>

### 38 → **B**

Con x intero positivo, y = 4^x - 3 assume i valori: x=1 -> 1, x=2 -> 13, x=3 -> 61, x=4 -> 253. Quindi A, C, D, E sono tutti raggiungibili. Per y = 7 servirebbe 4^x = 10, che non e' una potenza di 4 (x non intero), quindi 7 e' l'unico valore impossibile. Elenco generato con python: [1, 13, 61, 253, 1021].

<sub>confidenza: alta · fase: tarata</sub>

### 39 → **D**

Prezzo scontato per lattina: 0,40 x (1 - 0,15) = 0,34 dollari. 72 lattine = 3 confezioni da 24, quindi tutto e' scontato: 72 x 0,34 = 24,48 dollari. Distrattori: 28,80 e' il prezzo pieno di 72 lattine, 16,32 e' il prezzo scontato di 48 lattine. Calcolo verificato in python.

<sub>confidenza: alta · fase: tarata</sub>

### 40 → **C**

Imposto n / (2/3) = 9/2, cioe' n x (3/2) = 9/2, quindi n = (9/2) x (2/3) = 3. Verifica diretta: 3 diviso 2/3 = 3 x 3/2 = 9/2, corretto. Il distrattore E (27/4) e' il risultato di moltiplicare invece di dividere per 2/3 in senso inverso (9/2 x 3/2).

<sub>confidenza: alta · fase: tarata</sub>

### 41 → **D**

Prima ricavo la quantita' fisica costante: 26,40 / 1,65 = 16 galloni. Questa settimana gli stessi 16 galloni costano 16 x 1,82 = 29,12 dollari. La domanda chiede QUANTO IN PIU' (quantita' derivata): 29,12 - 26,40 = 2,72 dollari. Il distrattore C (2,64) e' il 10% della spesa vecchia e A (1,70) e' vicino alla sola differenza di prezzo unitario x 10.

<sub>confidenza: alta · fase: tarata</sub>

### 42 → **B**

Percentuali in sequenza su basi diverse: affitto = 25% di 2.200 = 550, quindi il RESTO e' 2.200 - 550 = 1.650. Il cibo e' il 30% del resto: 0,30 x 1.650 = 495 dollari. Il distrattore D (660) e' il 30% applicato erroneamente all'intero stipendio, C (550) e' l'affitto. Applicata l'accortezza sull'aliquota da riferire alla base giusta.

<sub>confidenza: alta · fase: tarata</sub>

### 43 → **B**

Sistema simmetrico: sommo le due equazioni membro a membro: (2x+y) + (x+2y) = 7 + 5, cioe' 3x + 3y = 12, quindi x + y = 4. La domanda chiede (x+y)/3 = 4/3 (opzione B). Il distrattore E (4) e' proprio x+y, cioe' la quantita' intermedia e non quella richiesta: attenzione alla quantita' derivata.

<sub>confidenza: alta · fase: tarata</sub>

### 44 → **E**

Pongo Z = 1; allora Y = 2Z = 2 e X = 4Y = 8. Il rapporto X:Z = 8:1 (opzione E). Attenzione all'ordine chiesto (X rispetto a Z, non Z rispetto a X): il reciproco 1:8 e' l'opzione A ed e' il distrattore classico.

<sub>confidenza: alta · fase: tarata</sub>

### 45 → **B**

Lettura di conteggi da tabella: trascrivo e sommo tutte le categorie (mutuamente esclusive) 78 + 9.209 + 35.509 + 27.909 + 2.372 = 75.077, controllo che il totale includa ogni riga. Poi 9.209 / 75.077 = 0,1227, cioe' circa 12,3%, quindi 12% (opzione B). Il distrattore A (9%) nasce dal leggere 9.209 come '9 mila su 100 mila' arrotondando male il denominatore.

<sub>confidenza: alta · fase: tarata</sub>

### 46 → **E**

Sommo esplicitamente i dieci termini con python: 1 + 1/4 + 1/9 + ... + 1/100 = 1,5498. Quindi S < 2 (opzione E). Controllo di plausibilita': gia' dopo i primi tre termini si e' a 1,36 e i termini successivi sono minuscoli, con maggiorazione classica S < 1 + somma di 1/(k(k-1)) = 1 + (1 - 1/10) = 1,9 < 2. Attenzione: C (2<S<3) e' il distrattore che sopravvaluta la coda della serie.

<sub>confidenza: alta · fase: tarata</sub>

### 47 → **D**

Numero di pezzi difettosi su 20.000: da 0,3% = 60 a 0,5% = 100 unita'. Rimborso pieno a 2.500 dollari l'una: da 60 x 2.500 = 150.000 a 100 x 2.500 = 250.000 dollari (opzione D). Il distrattore C (60.000-100.000) e' il conteggio delle unita' moltiplicato per 1.000 anziche' per 2.500, cioe' si ferma al valore intermedio.

<sub>confidenza: alta · fase: tarata</sub>

### 48 → **A**

REFUSO DEL LIBRO: cosi' come scritta, con la radice solo sul numeratore, l'espressione vale sqrt(4,2 x 1590)/15,7 = 81,72/15,7 = 5,20, che non e' vicino a nessuna delle opzioni (20, 40, 60, 80, 100). Con la radice su tutta la frazione, invece, il calcolo e' pulito e coerente con l'arrotondamento tipico del GMAT: sqrt(4 x 1600 / 16) = sqrt(400) = 20, e il valore esatto e' sqrt(4,2x1590/15,7) = 20,62. Scelgo quindi A, essendo l'unica lettura che produce una delle opzioni; segnalo l'errore di composizione della formula.

<sub>confidenza: **media** · fase: tarata</sub>

### 49 → **B**

sqrt(17) sta tra 4 e 4,25 (4,123) e sqrt(47) tra 6,8 e 6,9 (6,856); la somma e' 10,979, che arrotondata all'intero piu' vicino da' 11 (opzione B). Nota: non si puo' sommare sotto radice (sqrt(64) = 8 e' esattamente il distrattore A, e 32 = 17+47-32 il distrattore E). Somma verificata numericamente in python.

<sub>confidenza: alta · fase: tarata</sub>

### 50 → **D**

Retribuzione a scaglioni: 48 ore = 40 ore alla tariffa x piu' 8 ore di straordinario a 22 dollari. Lo straordinario vale 8 x 22 = 176 dollari, quindi 40x = 816 - 176 = 640 e x = 16 (opzione D). Applicata l'accortezza sugli scaglioni: la tariffa maggiorata vale SOLO sull'eccedenza oltre le 40 ore; il distrattore E (17) verrebbe da 816/48 = 17, cioe' dalla tariffa media indistinta.

<sub>confidenza: alta · fase: tarata</sub>

### 51 → **A**

Calcolo esatto con frazioni: 7/8 + 1/9 = 63/72 + 8/72 = 71/72; dividere per 1/2 equivale a moltiplicare per 2, quindi il valore e' 71/36 = 1,9722. Il valore piu' vicino tra le opzioni e' 2 (distanza 0,028) contro 3/2 (distanza 0,47). Verificato con python3 (Fraction): 71/36 = 1.97222.

<sub>confidenza: alta · fase: tarata</sub>

### 52 → **D**

Scrivo x = 10a + b e y = 10b + a con a,b cifre non nulle; la somma e' x + y = 11a + 11b = 11(a+b). Quindi 11 divide sempre x+y qualunque siano le cifre. Le altre opzioni dipendono da (a+b): p.es. 12 e 21 danno 33, non divisibile per 6, 9, 10 o 14. Risposta 11.

<sub>confidenza: alta · fase: tarata</sub>

### 53 → **C**

La successione parte da -5 con passo +1 e ha 8 termini: -5, -4, -3, -2, -1, 0, 1, 2. Lo zero non e' positivo, quindi i positivi sono soltanto 1 e 2, cioe' due. Risposta: Two.

<sub>confidenza: alta · fase: tarata</sub>

### 54 → **E**

Il numero totale di scatole necessarie e' s/r (divisione esatta, nessuna arancia avanza). Se n scatole sono gia' state riempite, restano s/r - n scatole da riempire. Attenzione al distrattore A (s - nr), che e' il numero di arance rimaste, non di scatole: la domanda chiede scatole, quindi si divide prima per r.

<sub>confidenza: alta · fase: tarata</sub>

### 55 → **B**

Domanda con elenco I/II/III: valuto ciascuna separatamente. I: 2a > b + c e' falsa perche' a e' il minore, quindi 2a < b + c (es. a=1,b=2,c=3: 2 < 5). II: c - a > b - a equivale, sommando a a entrambi i membri, a c > b, vera per ipotesi. III: c/a < b/a equivale, moltiplicando per a > 0, a c < b, falsa. Quindi solo II.

<sub>confidenza: alta · fase: tarata</sub>

### 56 → **B**

Calcolo la deviazione standard di popolazione per ciascuna riga con python3: A (media 50) = 3,54; B (media 20) = 10,00; C (media 30) = 2,45; D (media 40) = 1,58; E (media 60) = 7,07. La B ha valori 10,30,30,10, cioe' scarti di 10 da tutte le parti, ed e' quindi la piu' dispersa nonostante i numeri piccoli: la deviazione standard misura la dispersione assoluta, non relativa alla media (E ha numeri piu' grandi ma scarti minori).

<sub>confidenza: alta · fase: tarata</sub>

### 57 → **A**

Il costo variabile per unita' e' 40% di 2 dollari = 0,80 dollari; il margine di contribuzione per unita' e' 2,00 - 0,80 = 1,20 dollari. Il pareggio richiede 1,20n = 5.040, quindi n = 4.200 unita'. Verificato: ricavo 8.400 = costi 3.360 + 5.040.

<sub>confidenza: alta · fase: tarata</sub>

### 58 → **D**

Margine per unita' = 1,20 - 0,65 = 0,55 dollari. Il pareggio con l'investimento iniziale si ha quando 0,55n = 9.900, cioe' n = 18.000 unita'. Verifica: ricavo 21.600 = 9.900 + 0,65 x 18.000 = 9.900 + 11.700 = 21.600.

<sub>confidenza: alta · fase: tarata</sub>

### 59 → **D**

Percentuale 'greater than' si calcola sulla base del confronto (State D): (181 - 79)/79 = 102/79 = 1,2911, cioe' circa 129% in piu'. L'opzione approssimata piu' vicina e' 125%. Attenzione al distrattore E (155%), che corrisponde al rapporto 181/79 = 229% mal interpretato, e a C (100%), che sarebbe il semplice raddoppio.

<sub>confidenza: alta · fase: tarata</sub>

### 60 → **D**

L'aggiunta di n litri copre la differenza di riempimento: 7/9 - 1/3 = 7/9 - 3/9 = 4/9 della capacita'. Quindi n = (4/9)C, da cui C = (9/4)n. Verifica dimensionale: con n = 4 la capacita' e' 9, il serbatoio passa da 3 a 7 litri, cioe' da 1/3 a 7/9.

<sub>confidenza: alta · fase: tarata</sub>

### 61 → **B**

Variazione netta di quota: -280 + 350 - 620 + 100 - 400 = -850 metri. Partendo da 850 metri sopra Town X, l'arrivo e' a 850 - 850 = 0, cioe' alla stessa quota di Town X. Il distrattore A (850 sotto) nasce dall'applicare la variazione netta senza partire dai 850 iniziali.

<sub>confidenza: alta · fase: tarata</sub>

### 62 → **A**

Gli x alberi producono 10x bushel su un raccolto totale di 350. La frazione richiesta e' 10x/350 = x/35. Il distrattore B e' la frazione complementare (il resto del raccolto), C ed E sono quantita' assolute e non frazioni: la domanda chiede la quota di quei x alberi, quindi x/35.

<sub>confidenza: alta · fase: tarata</sub>

### 63 → **D**

Sia n il numeratore: n/(n+16) = 0,8 da cui n = 0,8n + 12,8, cioe' 0,2n = 12,8 e n = 64. Il denominatore e' 64 + 16 = 80. Verifica: 64/80 = 0,8. Attenzione: la domanda chiede il DENOMINATORE, non il numeratore (64 e' il distrattore B).

<sub>confidenza: alta · fase: tarata</sub>

### 64 → **D**

La quota mensile di Jonathan e' 525 - 250 (deposito una tantum) = 275 dollari. Poiche' i tre pagano quote uguali, l'affitto mensile totale e' 3 x 275 = 825 dollari. Il distrattore A (1.575) e' 3 x 525, cioe' il calcolo che dimentica di togliere prima il deposito.

<sub>confidenza: alta · fase: tarata</sub>

### 65 → **A**

Da F/J = 3/2 segue F = 1,5J. La seconda condizione da' (F + 40)/J = 5/3, cioe' 1,5J + 40 = (5/3)J. Quindi 40 = (5/3 - 3/2)J = (10/6 - 9/6)J = J/6, da cui J = 240 dollari. Verifica: F = 360, (360 + 40)/240 = 400/240 = 5/3.

<sub>confidenza: alta · fase: tarata</sub>

### 66 → **B**

Sia t il numero di ore trascorse dalle 11:00 (partenza di Al); Ben viaggia da 3 ore in piu', cioe' t + 3 ore. Distanza combinata: 40t + 20(t + 3) = 240, quindi 60t + 60 = 240 e t = 3. L'orario e' 11:00 + 3 ore = 14:00. Verifica: Al 40 x 3 = 120 miglia, Ben 20 x 6 = 120 miglia, totale 240. La trappola qui e' usare lo stesso tempo per entrambi (darebbe 4 ore, cioe' le 15:00, opzione C).

<sub>confidenza: alta · fase: tarata</sub>

### 67 → **B**

Con s = 2.000 si ha s/1.000 = 2 e (s/1.000)^2 = 4. Dunque f = 3r x 4 = 12r, da cui r = f/12. Il distrattore C (f/36) nasce dal quadrare anche il 3, il distrattore A dal dimenticare il quadrato.

<sub>confidenza: alta · fase: tarata</sub>

### 68 → **D**

La popolazione parte da 3 e raddoppia a ogni fine mese: dopo k mesi vale 3 x 2^k. Per k = 10 si ottiene 3(2^10) = 3.072. Il distrattore C, 2(3^10), inverte base ed esponente rispetto alla popolazione iniziale.

<sub>confidenza: alta · fase: tarata</sub>

### 69 → **C**

REFUSO DEL LIBRO: la formula e' stampata come F = 9/(5C) + 32, ma la relazione corretta (e l'unica che da' un'opzione sensata) e' F = (9/5)C + 32. Invertendo: C = (F - 32) x 5/9 = (85 - 32) x 5/9 = 53 x 5/9 = 29,44, che arrotondato al grado piu' vicino da' 29 gradi Celsius. Il distrattore A (18) corrisponde a (85-32)/3 circa, e D/E a interpretazioni errate della formula.

<sub>confidenza: alta · fase: tarata</sub>

### 70 → **E**

Pongo y = 5k con k intero positivo: 3x = 200 - 20k, quindi serve 200 - 20k divisibile per 3; modulo 3 si ha 2 - 2k = 0, cioe' k = 1 (mod 3). Enumerando con python3 le soluzioni con x, y positivi: (y=5, x=60), (y=20, x=40), (y=35, x=20). Tutti e tre i valori di x sono multipli di 10 (mentre 3, 6, 7, 8 non dividono, ad esempio, 20), quindi la risposta e' 10.

<sub>confidenza: alta · fase: tarata</sub>

### 71 → **E**

Valuto le tre espressioni una per una. I: (√82+√82)² = (2√82)² = 4·82 = 328, intero. II: 82·√82 ≈ 742,54, non intero perché 82 non è un quadrato perfetto. III: (√82)(√82)/82 = 82/82 = 1, intero. Quindi sono interi I e III, cioè l'opzione E.

<sub>confidenza: alta · fase: tarata</sub>

### 72 → **C**

Sviluppo i due quadrati: (x+2)² = x²+4x+4 e (x-2)² = x²-4x+4. La somma è 2x²+8 (i termini in 4x si cancellano) e la media è (2x²+8)/2 = x²+4. Risposta C. Il distrattore A (x²) si ottiene dimenticando il +4 costante.

<sub>confidenza: alta · fase: tarata</sub>

### 73 → **C**

x²-2<0 equivale a x² < 2, cioè |x| < √2, quindi -√2 < x < √2. Attenzione: la disuguaglianza su x² include i valori negativi, quindi l'intervallo è simmetrico attorno a 0 e non 0 < x < √2 (distrattore B, che dimentica i negativi). La radice va estratta correttamente: il limite è √2 ≈ 1,414 e non 2 (distrattore E). Risposta C.

<sub>confidenza: alta · fase: tarata</sub>

### 74 → **B**

Poiché non inizia mai il libro successivo nello stesso giorno in cui finisce il precedente, ogni libro occupa ceil(pagine/50) giorni interi. Giorni per libro: 253→6, 110→3, 117→3, 170→4, 155→4, 50→1, 205→5, 70→2. I giorni cumulativi di fine sono 6, 9, 12, 16, 20, 21, 26, 28: l'ottavo libro finisce esattamente il 28° giorno, mentre il nono richiederebbe fino al giorno 32. Alla fine del 28° giorno ha terminato 8 libri, risposta B.

<sub>confidenza: alta · fase: tarata</sub>

### 75 → **D**

Il mercato totale è x unità in entrambi gli anni, quindi i produttori dell'Europa occidentale hanno prodotto e venduto 0,42x nel 1990 e 0,33x nel 1993. La diminuzione è 0,42x - 0,33x = 0,09x, cioè il 9% di x. Risposta D. Nota: essendo il totale x uguale nei due anni, la differenza delle quote percentuali si applica direttamente a x; i distrattori con x/100 nascono dal confondere 'percento' con una divisione ulteriore, e 14% è la variazione relativa (9/42 ≈ 21%) male approssimata.

<sub>confidenza: alta · fase: tarata</sub>

### 76 → **A**

Fattorizzo: (k+2)(k³-k) = (k+2)·k·(k²-1) = (k-1)k(k+1)(k+2), cioè il prodotto di quattro interi consecutivi. Tra quattro consecutivi c'è sempre almeno un multiplo di 3 e almeno due pari, quindi il prodotto è divisibile per 6 (anzi per 24). Il resto della divisione per 6 è quindi sempre 0. Verificato con python per k da 1 a 9: resto 0 in ogni caso. Risposta A.

<sub>confidenza: alta · fase: tarata</sub>

### 77 → **D**

Calcolo esattamente la distanza da 1/2 con le frazioni (non a stima, per la lezione sui rapporti numericamente vicini): 4/7-1/2 = 1/14 ≈ 0,0714; 5/9-1/2 = 1/18 ≈ 0,0556; 6/11-1/2 = 1/22 ≈ 0,0455; 7/13-1/2 = 1/26 ≈ 0,0385; 9/16-1/2 = 1/16 = 0,0625. Tutte le frazioni sono maggiori di 1/2 e la differenza minima è 1/26. Risposta D.

<sub>confidenza: alta · fase: tarata</sub>

### 78 → **D**

Moltiplico entrambi i membri per p (lecito perché p ≠ 0): p·p - (1-p²) = r, cioè p² - 1 + p² = r. Il segno meno davanti alla frazione va distribuito su entrambi i termini di (1-p²), passaggio dove nasce il distrattore. Quindi r = 2p² - 1, risposta D.

<sub>confidenza: alta · fase: tarata</sub>

### 79 → **C**

Da |z|/w = 1 segue |z| = w, quindi w è positivo e z può valere w oppure -w: né A né B sono obbligate. Elevando al quadrato, z² = |z|² = w², che vale in entrambi i casi: C è sempre vera. D ed E falliscono per esempio con z = -1, w = 1 (z² = 1 ma w³ = 1 con z = -1 dà z³ = -1 ≠ 1). Risposta C.

<sub>confidenza: alta · fase: tarata</sub>

### 80 → **E**

Sia n il numero: n = (2/3)n + 108. Portando a sinistra, n - (2/3)n = (1/3)n = 108, quindi n = 324. Verifica: due terzi di 324 sono 216 e 216 + 108 = 324. Risposta E. Il distrattore D (216) è proprio i due terzi, cioè la quantità intermedia e non quella richiesta.

<sub>confidenza: alta · fase: tarata</sub>

### 81 → **D**

Questa è una tariffa a scaglioni: la lezione dice di applicare la tariffa alta SOLO all'eccedenza, quindi alle (x-50) ore oltre le prime 50. Ogni ora eccedente contiene due intervalli da 30 minuti, quindi costa 2 × 0,40 = 0,80 dollari. La spesa totale è c + 0,80(x-50). Risposta D. Il distrattore C dimentica il raddoppio da mezz'ora a ora, B applica la tariffa a tutte le x ore.

<sub>confidenza: alta · fase: tarata</sub>

### 82 → **B**

La riduzione di velocità è 100 - 47 = 53 km/h. Convertendo, 53 × 0,625 = 33,125 miglia orarie, cioè circa 33. Risposta B. Attenzione alla lezione sulle conversioni: bisogna convertire la differenza, non le due velocità separatamente prima di sottrarre (il risultato coincide, ma il distrattore C = 53 è la riduzione non convertita, e D = 63 è 100×0,625 arrotondato).

<sub>confidenza: alta · fase: tarata</sub>

### 83 → **B**

Da 5x - 8 = 12 ottengo 5x = 20, quindi x = 4. Da x = y + 3 segue y = x - 3 = 4 - 3 = 1. Risposta B. Il distrattore D (4) è il valore di x, cioè la quantità intermedia e non quella richiesta.

<sub>confidenza: alta · fase: tarata</sub>

### 84 → **E**

Le ore registrate totali sono 4 (martedì) + 2 (giovedì) = 6. Le ore viste sono comprese tra 1+2 = 3 e 2+3 = 5. Le ore non ancora viste sono h = 6 - (ore viste), quindi h varia da 6-5 = 1 a 6-3 = 3. Controllo la fattibilità: mercoledì sono disponibili 4 ore registrate (basta per 1-2 ore di visione) e venerdì restano almeno 6-2 = 4 ore (basta per 2-3 ore), quindi entrambi gli estremi sono realizzabili. Risposta E.

<sub>confidenza: alta · fase: tarata</sub>

### 85 → **E**

Uso la sostituzione 'tutto del tipo economico' (lezione sulle miscele): se tutti i 50 costumi costassero 80 dollari si spenderebbero 4.000; la differenza 4.270 - 4.000 = 270 divisa per la differenza unitaria 90-80 = 10 dà 27 costumi del gruppo B. Il costo totale dei costumi del gruppo B è quindi 27 × 90 = 2.430 dollari. Risposta E. Attenzione: la domanda chiede il costo totale del gruppo B, non il numero di dancer né il costo del gruppo A (23 × 80 = 1.840, distrattore A).

<sub>confidenza: alta · fase: tarata</sub>

### 86 → **D**

Il dosaggio tipico per 120 libbre è 120/15 = 8 unità da 2 cc, cioè 16 cc. Il dosaggio prescritto è 18 cc. L'aumento percentuale rispetto al tipico è (18-16)/16 = 2/16 = 0,125, cioè 12,5%. Risposta D. Il distrattore C (11%) corrisponde a calcolare 2/18, cioè usare la base sbagliata al denominatore.

<sub>confidenza: alta · fase: tarata</sub>

### 87 → **D**

Da u = f(t) = √t - 10 ricavo √t = u + 10 e quindi, elevando al quadrato entrambi i membri, t = (u + 10)². Risposta D. I distrattori invertono l'ordine delle operazioni (radice prima dell'addizione) o applicano la radice a u.

<sub>confidenza: alta · fase: tarata</sub>

### 88 → **D**

Sia n il numero originale: 0,35n - 15 = 0,25n. Portando i termini in n a sinistra, 0,10n = 15, quindi n = 150. Verifica: 35% di 150 = 52,5; 52,5 - 15 = 37,5 = 25% di 150. Risposta D.

<sub>confidenza: alta · fase: tarata</sub>

### 89 → **D**

Sia r il numero di rose rosse e w quelle bianche: le probabilità sono proporzionali ai conteggi, quindi w = 2r e w + r = 30, da cui 3r = 30, r = 10 e w = 20. Verifica: P(bianca) = 20/30 = 2/3 è esattamente il doppio di P(rossa) = 10/30 = 1/3. Risposta D. Il distrattore B (10) è il numero di rose rosse, non quello richiesto.

<sub>confidenza: alta · fase: tarata</sub>

### 90 → **C**

Lavoro all'indietro lungo la catena percentuale: 3 persone sono il 20% di quelle intervistate al telefono, quindi gli intervistati telefonici sono 3/0,20 = 15. Questi 15 sono il 60% di chi ha risposto all'annuncio, quindi il totale è 15/0,60 = 25. Verifica in avanti: 60% di 25 = 15 e 20% di 15 = 3. Risposta C. Il distrattore E (64) nasce dall'applicare i tassi nel verso sbagliato.

<sub>confidenza: alta · fase: tarata</sub>

### 91 → **D**

Esponente negativo: (-3)^(-2) = 1/(-3)^2. La base negativa elevata a esponente PARI da' segno positivo: (-3)^2 = 9, quindi il risultato e' 1/9. I distrattori A e C nascono dall'errore di applicare il segno meno fuori dalla potenza (come se fosse -(3^2)), E dall'ignorare il segno negativo dell'esponente. Verificato con Python: 0.1111... = 1/9.

<sub>confidenza: alta · fase: tarata</sub>

### 92 → **C**

I 6 prezzi formano una progressione aritmetica di ragione 0,25 partendo dal piu' piccolo a. Somma = 6a + 0,25*(0+1+2+3+4+5) = 6a + 3,75 = 8,25, quindi 6a = 4,50 e a = 0,75. Il vaso piu' grande e' a + 5*0,25 = 0,75 + 1,25 = 2,00. Controllo: 0,75+1,00+1,25+1,50+1,75+2,00 = 8,25.

<sub>confidenza: alta · fase: tarata</sub>

### 93 → **A**

Con r = s + 6 riscrivo tutto in funzione di s: A = 2r = 2s+12; B = 2s; C = r+s = 2s+6; D = 2r-s = s+12; E = 2s-r = s-6. A supera B di 12, C di 6, E di s+18 (positivo) e D di (2s+12)-(s+12) = s > 0 perche' s e' un intero positivo. Quindi A e' sempre il maggiore, indipendentemente dal valore di s (verificato numericamente per s = 1, 5, 20).

<sub>confidenza: alta · fase: tarata</sub>

### 94 → **C**

Caso 'tariffe a scaglioni' (accortezza n.4): l'aliquota alta va applicata SOLO al primo scaglione e quella bassa all'eccedenza. Commissione sul primo scaglione: 15% di 50.000 = 7.500. Restano 24.000 - 7.500 = 16.500 dovuti al 10% sull'eccedenza, quindi eccedenza = 16.500/0,10 = 165.000. Prezzo di vendita = 50.000 + 165.000 = 215.000. Il distrattore B (160.000) corrisponde a dimenticare il primo scaglione nell'eccedenza; D (240.000) a fare 24.000/0,10.

<sub>confidenza: alta · fase: tarata</sub>

### 95 → **B**

Sia E il numero di English majors: E = 2H e E = 3M, quindi H = E/2 e M = E/3. Il rapporto H:M = (E/2):(E/3) = (1/2):(1/3) = 3:2. Verifica con E = 6: H = 3, M = 2, rapporto 3 a 2. Attenzione all'ordine richiesto (storia : matematica): il rapporto inverso 2 a 3 e' il distrattore C.

<sub>confidenza: alta · fase: tarata</sub>

### 96 → **E**

Sostituisco d = 800 e y = 8 nella formula d*(y+1)/24: 800*(8+1)/24 = 800*9/24 = 7200/24 = 300 mg. Il distrattore comune (266,7 o 275) nasce dall'usare y invece di y+1; qui il calcolo esatto da' 300, che coincide con l'opzione E.

<sub>confidenza: alta · fase: tarata</sub>

### 97 → **A**

Enumerati i 36 esiti equiprobabili, quelli con somma > 9 (cioe' 10, 11 o 12) sono: 10 -> (4,6),(5,5),(6,4) = 3; 11 -> (5,6),(6,5) = 2; 12 -> (6,6) = 1, totale 6 casi. Probabilita' = 6/36 = 1/6. Conteggio confermato con enumerazione in Python. Il distrattore D (5/18 = 10/36) corrisponde a includere anche la somma 9.

<sub>confidenza: alta · fase: tarata</sub>

### 98 → **B**

La vacanza inizia sabato; i giorni sono sabato, domenica, lunedi'. Torna a casa alla fine di lunedi' se e solo se NON piove sabato, NON piove domenica e piove lunedi'. Probabilita' = 0,8 * 0,8 * 0,2 = 0,128. I distrattori: 0,008 = 0,2^3 (piove tutti e tre i giorni), 0,512 = 0,8^3 (mai pioggia), 0,488 = 1 - 0,512.

<sub>confidenza: alta · fase: tarata</sub>

### 99 → **E**

Sia x il numero di chi ama entrambi; chi non ama nessuno dei due e' 2x. Inclusione-esclusione sui 200 intervistati: (60 - x) + (80 - x) + x + 2x = 200, cioe' 140 + x = 200, quindi x = 60 e 'nessuno dei due' = 2x = 120. Verifica: chi ama almeno uno = 60 + 80 - 60 = 80, e 200 - 80 = 120 = 2*60. Coerente (tutti gli sciatori amano anche il pattinaggio, ammissibile). Il distrattore A (20) e' il valore di x che si otterrebbe sbagliando l'equazione.

<sub>confidenza: alta · fase: tarata</sub>

### 100 → **E**

Applico la tabella data passo per passo, dall'interno verso l'esterno. Primo: m (+) p = n. Secondo: n (+) q = q (terza relazione). Terzo: q (+) p = r (quinta relazione). Quindi [(m+p)+q]+p = r. Nota: l'operazione non e' commutativa (p(+)q = p mentre q(+)p = r), percio' l'ordine degli argomenti nell'ultimo passaggio e' decisivo; usare p(+)q darebbe erroneamente p (distrattore C).

<sub>confidenza: alta · fase: tarata</sub>

### 101 → **A**

Le prime 24 ore costano x in blocco; le ore eccedenti sono 36 - 24 = 12, pagate y ciascuna, quindi 12y. Costo totale = x + 12y. Il distrattore B applica y a tutte le 36 ore ignorando che le prime 24 sono gia' incluse in x; C, D ed E moltiplicano x per un numero di ore, ma x e' una tariffa forfettaria, non oraria.

<sub>confidenza: alta · fase: tarata</sub>

### 102 → **D**

Conversione di unita' composte (categoria insidiosa: il fattore non convertito e' tra le opzioni). 1 metro cubo = 1.000.000 cm3, quindi la massa e' 7,3 g/cm3 * 1.000.000 cm3 = 7.300.000 grammi. Ultimo passaggio, la conversione richiesta in chilogrammi: 7.300.000 / 1.000 = 7.300 kg. L'opzione E (7.300.000) e' proprio il valore in grammi non convertito.

<sub>confidenza: alta · fase: tarata</sub>

### 103 → **C**

Moltiplico entrambi i membri per z (lecito perche' z diverso da 0): z*z + (1 - 2z^2) = w, cioe' z^2 + 1 - 2z^2 = w, da cui w = -z^2 + 1. Verifica numerica con z = 3: membro sinistro 3 + (1-18)/3 = -8/3, e w/z = (-9+1)/3 = -8/3. Coincidono. Il distrattore E (-2z^2+1) si ottiene dimenticando di moltiplicare il primo termine z per z.

<sub>confidenza: alta · fase: tarata</sub>

### 104 → **C**

Applico la definizione ad*+be+cf con (a,b,c) = (1,-2,3) e (d,e,f) = (1, 1/2, 1/3): 1*1 + (-2)*(1/2) + 3*(1/3) = 1 - 1 + 1 = 1. Verificato con frazioni esatte in Python. Il distrattore A (-1) nasce da un errore di segno sul secondo addendo.

<sub>confidenza: alta · fase: tarata</sub>

### 105 → **B**

Categoria insidiosa media/mediana su tabella (accortezze n.5 e n.7): la mediana va letta sulla lista ORDINATA dei dati, non dalla colonna centrale della tabella. Considero solo gli studenti con almeno 1 assenza: 3 + 10 + 3 + 5 + 3 = 24 studenti. La lista ordinata e' 1,1,1, poi dieci 2 (posizioni 4-13), poi 3,3,3 (14-16), poi 4 cinque volte, poi '5 o piu'' tre volte. Con 24 valori la mediana e' la media del 12esimo e del 13esimo, entrambi pari a 2, quindi 2. Nota: i valori '5 o piu'' non creano problemi perche' stanno tutti nella coda alta.

<sub>confidenza: alta · fase: tarata</sub>

### 106 → **C**

Da d/c = b/a segue, prendendo i reciproci, c/d = a/b; combinando con x/y = c/d ottengo la relazione base x/y = a/b, cioe' bx = ay. I. y/x = b/a e' semplicemente il reciproco di x/y = a/b: VERA. II. x/a = y/b equivale a bx = ay: VERA. III. y/a = x/b equivale a by = ax, che non discende da bx = ay (le lettere sono scambiate): FALSA. Controesempio: c=2, d=3, x=4, y=6, b=3, a=2 -> y/a = 3 ma x/b = 4/3. Quindi solo I e II. Elenco I/II/III valutato caso per caso e verificato numericamente su due esempi.

<sub>confidenza: alta · fase: tarata</sub>

### 107 → **B**

Attenzione: qui [x] e' il minimo intero MAGGIORE O UGUALE a x, cioe' il soffitto (ceiling), non il pavimento. ceil(x/2) = 0 significa -1 < x/2 <= 0, quindi -2 < x <= 0. Fra le opzioni solo -3/2 rientra in questo intervallo: -2 e' escluso (per x = -2 si ha x/2 = -1 e ceil(-1) = -1, non 0), mentre 1/2, 1 e 2 danno ceil positivo. Verificato in Python: ceil(-1,5/2) = ceil(-0,75) = 0.

<sub>confidenza: alta · fase: tarata</sub>

### 108 → **B**

L'equazione t(t+2) = 24 diventa t^2 + 2t - 24 = 0, cioe' (t+6)(t-4) = 0, con radici t = 4 e t = -6. Poiche' a e b soddisfano la stessa equazione e a e' diverso da b, l'insieme {a,b} = {4, -6} e quindi a + b = -2. Alternativa piu' rapida: per la somma delle radici (Vieta), a + b = -2/1 = -2. I distrattori 46 e 48 derivano dal trattare 24 come prodotto di fattori interi senza risolvere l'equazione.

<sub>confidenza: alta · fase: tarata</sub>

### 109 → **E**

I voti indipendenti sono 0,40N e da questi Ms. Robbins ha ricevuto un numero FISSO, 8.000 (non una percentuale). I voti dei registrati sono N - 0,40N = 0,60N, di cui lei ottiene il 10%, cioe' 0,10*0,60N = 0,06N. Totale = 0,06N + 8.000. Verifica con N = 100.000: indipendenti 40.000 (ne prende 8.000), registrati 60.000 (ne prende 6.000), totale 14.000 = 0,06*100.000 + 8.000. Il distrattore A sostituisce 8.000 con 3.200 = 8% applicato erroneamente.

<sub>confidenza: alta · fase: tarata</sub>

### 110 → **B**

P = I - C. Primi 4 mesi: C = I + 32.000, quindi P = -32.000 al mese, totale -128.000. Mesi successivi (3): I = C + 36.000, quindi P = +36.000 al mese, totale +108.000. Ultimi 5 mesi: I = C + 10.000, quindi P = +10.000 al mese, totale +50.000. Somma: -128.000 + 108.000 + 50.000 = 30.000 dollari. Il punto delicato e' il segno dei primi 4 mesi (i costi superano i ricavi): trattarli come positivi darebbe 286.000, e ignorarli darebbe 158.000.

<sub>confidenza: alta · fase: tarata</sub>

### 111 → **E**

Media ponderata: se le unità di P sono 1, quelle di Q sono 2 (il doppio). Ricavo totale = 1x20 + 2x17 = 20 + 34 = 54 dollari su 3 unità vendute. Media = 54/3 = 18,00 dollari. Applicata la lezione 3: convertire subito in TOTALI e dividere per il numero di elementi, invece di mediare 20 e 17 (che darebbe 18,50, il distrattore D, cioè la media non pesata).

<sub>confidenza: alta · fase: tarata</sub>

### 112 → **B**

17 viaggi x 4 giare = 68 giare trasportate. In cartoni da 7: 68 = 9x7 + 5, quindi l'ultimo cartone parzialmente pieno contiene 5 giare. La domanda chiede quante giare SERVONO per riempirlo, cioè 7 - 5 = 2. Attenzione al distrattore D (5), che è il contenuto attuale del cartone e non la quantità mancante: ho riletto la domanda per accertarmi che chiedesse la quantità derivata.

<sub>confidenza: alta · fase: tarata</sub>

### 113 → **E**

Sia D il numero di Democratici dell'anno scorso: Repubblicani = D + 20, totale T = 2D + 20. Quest'anno il totale è lo stesso e i Repubblicani sono 2 in meno: R' = D + 18. La condizione R' = (2/3)T dà D + 18 = (2/3)(2D + 20), cioè 3D + 54 = 4D + 40, quindi D = 14 e T = 2(14) + 20 = 48. Verifica: R' = 32 e 32/48 = 2/3.

<sub>confidenza: alta · fase: tarata</sub>

### 114 → **D**

I depositi da 1 a 50 dollari formano una serie aritmetica: somma = 50x51/2 = 1.275. Sommando al saldo iniziale: 800 + 1.275 = 2.075 dollari. Il distrattore C (1.675) corrisponde a dimenticare parte della serie e A (850) a sommare solo pochi depositi.

<sub>confidenza: alta · fase: tarata</sub>

### 115 → **B**

Domanda con conversione di unità (lezione 17-18): la differenza in libbre è 2,7 miliardi - 980 milioni = 2.700 - 980 = 1.720 milioni di libbre. Convertendo in galloni si DIVIDE per 8,6 (perché 1 gallone = 8,6 libbre): 1.720/8,6 = 200 milioni di galloni. Il distrattore E (14.800) è la moltiplicazione per 8,6 invece della divisione, e C (1.700) è il valore non convertito.

<sub>confidenza: alta · fase: tarata</sub>

### 116 → **B**

4 macchine producono x in 6 giorni, quindi la produzione totale è 24 macchina-giorni per x unità: rate di una macchina = x/24 unità al giorno. Per fare 3x in 4 giorni serve un rate complessivo di 3x/4 al giorno. Numero macchine = (3x/4)/(x/24) = 18. Controllo: 18 macchine x 4 giorni = 72 macchina-giorni = 3 volte i 24 macchina-giorni che producono x.

<sub>confidenza: alta · fase: tarata</sub>

### 117 → **C**

Domanda con elenco I/II/III: valuto ogni operazione separatamente (lezione 5). Il vincolo 6Δ3 ≤ 3 è soddisfatto solo da sottrazione (6-3=3) e divisione (6/3=2); addizione dà 9 e moltiplicazione 18, escluse. I: 2-2=0 ma 2/2=1, quindi non deve valere. II: 2/2=1 ma 2-2=0, quindi non deve valere. III: 4-2=2 e 4/2=2, vero in entrambi i casi rimasti, quindi è l'unica che DEVE essere vera.

<sub>confidenza: alta · fase: tarata</sub>

### 118 → **A**

0,25n = 0,375m (37½% = 0,375). Dividendo: n/m = 0,375/0,25 = 3/2. Quindi 12n/m = 12 x 3/2 = 18. Verifica numerica: m = 2, n = 3 dà 25% di 3 = 0,75 e 37,5% di 2 = 0,75, e 12x3/2 = 18. Il distrattore C (8) corrisponde a invertire il rapporto (m/n = 2/3).

<sub>confidenza: alta · fase: tarata</sub>

### 119 → **A**

Ho enumerato con Python tutte le permutazioni delle sei cifre 1,2,3,6,7,8 divise in due numeri di tre cifre, cercando la differenza positiva minima: il minimo è 29, ottenuto con 316 - 287. Logica sottostante: per minimizzare si accostano le centinaia (3 e 2), si mette la cifra più piccola nelle decine del maggiore e la più grande nelle decine del minore (316 e 287). L'enumerazione esaustiva conferma che nessuna combinazione fa meglio di 29.

<sub>confidenza: alta · fase: tarata</sub>

### 120 → **D**

La tabella è parziale (sei tecniche in totale, quattro elencate), ma la domanda restringe esplicitamente il denominatore a chi ha indicato UNA DELLE QUATTRO tecniche elencate. Somma dei quattro: 35 + 22 + 18 + 15 = 90. Coupon + espositori = 22 + 18 = 40. Frazione = 40/90 = 4/9. Il distrattore C (2/5 = 40/100) è l'errore di usare 100 come denominatore ignorando che la tabella è parziale.

<sub>confidenza: alta · fase: tarata</sub>

### 121 → **E**

Full-time = 65%, part-time = 35% (le due categorie esauriscono il totale). La differenza è 30% del totale = 5.100 dipendenti, quindi totale = 5.100/0,30 = 17.000. Verifica: 65% di 17.000 = 11.050 full-time e 5.950 part-time, differenza 5.100. Il distrattore C (11.050) è proprio il numero di full-time, non il totale richiesto.

<sub>confidenza: alta · fase: tarata</sub>

### 122 → **A**

C(90) = 100.000 x 90 / (100 - 90) = 9.000.000/10 = 900.000 dollari. C(80) = 100.000 x 80 / (100 - 80) = 8.000.000/20 = 400.000 dollari. Differenza = 900.000 - 400.000 = 500.000 dollari. La domanda chiede la differenza (quantità derivata), non uno dei due costi.

<sub>confidenza: alta · fase: tarata</sub>

### 123 → **E**

Elenco I/II/III valutato caso per caso. Ponendo u = xy, l'equazione x²y² - xy = 6 diventa u² - u - 6 = 0, cioè (u-3)(u+2) = 0, quindi xy = 3 oppure xy = -2. I: y = 1/(2x) dà xy = 1/2, non ammesso. II: y = -2/x dà xy = -2, ammesso. III: y = 3/x dà xy = 3, ammesso. Quindi solo II e III.

<sub>confidenza: alta · fase: tarata</sub>

### 124 → **E**

La deviazione standard misura la dispersione attorno alla media: aggiungendo la stessa costante 1 a tutti i valori, media e valori traslano insieme e ogni scarto (n+1) - (media+1) = n - media resta identico. Quindi la deviazione standard è invariata e vale d. I distrattori A e B applicano erroneamente la traslazione alla dispersione.

<sub>confidenza: alta · fase: tarata</sub>

### 125 → **D**

Su 100 studenti: 80 fanno calcolo; il 60% di questi fa anche fisica, cioè 48 fanno entrambe. 10 non fanno nessuna delle due, quindi 90 fanno almeno una. Inclusione-esclusione: 90 = 80 + P - 48, da cui P = 58%. Verifica: solo calcolo 32, entrambe 48, solo fisica 10, nessuna 10 -> totale 100. Il distrattore C (48%) è proprio l'intersezione, valore intermedio calcolato.

<sub>confidenza: alta · fase: tarata</sub>

### 126 → **B**

Provo i valori: k=1 dà 561,037 (cifra delle unità 1); k=2 dà 56,1037 (cifra delle unità 6, corretto); k=3 dà 5,61037 (unità 5). Quindi k = 2. Nota che k negativi moltiplicherebbero: k=-1 dà 56.103,7 (unità 3) e k=-2 dà 561.037 (unità 7), entrambi errati. Il divisore giusto è 10² = 100.

<sub>confidenza: alta · fase: tarata</sub>

### 127 → **E**

Lavoro con i rate (lavoro/ora): R + S + T = 1/4, mentre S + T = 1/5. Sottraendo: R = 1/4 - 1/5 = 5/20 - 4/20 = 1/20 lavoro all'ora. Il tempo di R da sola è il reciproco: 20 ore. Il distrattore B (10) e C (12) nascono da sottrarre i tempi (5 e 4) invece dei rate.

<sub>confidenza: alta · fase: tarata</sub>

### 128 → **E**

La domanda riguarda solo IBM e AT&T (le altre righe della tabella sono distrattori). Inclusione-esclusione: chi possiede almeno una delle due = 48 + 30 - 15 = 63. Chi non possiede nessuna delle due = 200 - 63 = 137. Il distrattore A (63) è proprio il valore intermedio, cioè l'unione anziché il complemento richiesto: applicata la lezione 1, calcolare l'unione e poi sottrarre dal totale.

<sub>confidenza: alta · fase: tarata</sub>

### 129 → **D**

Gli interi k con -26 < k < 24 vanno da -25 a 23 inclusi (estremi esclusi). I termini da -23 a 23 si cancellano a coppie, restano -25 e -24, la cui somma è -49. Verificato con Python: sum(range(-25,24)) = -49. Il distrattore E (-51) corrisponde a includere erroneamente -26.

<sub>confidenza: alta · fase: tarata</sub>

### 130 → **E**

Dal disegno R è a sinistra dello zero, quindi la sua coordinata è negativa: essendo |R| = r, la coordinata di R è -r. S e T sono a destra dello zero, quindi le loro coordinate sono +s e +t. La media aritmetica delle tre coordinate è (-r + s + t)/3 = (s + t - r)/3. Il distrattore D somma i valori assoluti ignorando il segno di R, e B dimentica la divisione per 3.

<sub>confidenza: alta · fase: tarata</sub>

### 131 → **A**

Mark ha venduto n-10 e Ann n-2. La condizione 'ciascuno almeno una scatola' impone n-10 >= 1, cioe' n >= 11. La condizione 'insieme meno di n' impone (n-10)+(n-2) < n, cioe' 2n-12 < n, cioe' n < 12. L'unico intero che soddisfa 11 <= n < 12 e' n = 11 (verificato con ciclo in Python su n da 5 a 30: unica soluzione 11). Controllo: Mark 1, Ann 9, totale 10 < 11.

<sub>confidenza: alta · fase: tarata</sub>

### 132 → **A**

Da 3P5 + 4QR = 8S4: unita' 5+R termina in 4 quindi R=9 con riporto 1; centinaia 3+4+riporto=8 quindi il riporto dalle decine vale 1. Decine: P+Q+1 = S+10, con Q=2P da' 3P+1 = S+10, ossia S = 3P-9, con P<=4 (perche' Q=2P deve restare cifra) e P>=3 (per avere il riporto). P=3 da' S=0, P=4 da' S=3. Ricerca esaustiva in Python conferma solo (P,Q,R,S) = (3,6,9,0) e (4,8,9,3): tra le opzioni compare solo 3, e infatti 345+489=834.

<sub>confidenza: alta · fase: tarata</sub>

### 133 → **E**

Per inclusione-esclusione chi fa musica o arte e' x + y - z (z e' contato due volte in x e y e va tolto una volta). Chi non fa ne' l'una ne' l'altra e' 5.000 - (x + y - z) = 5.000 - x - y + z. Il distrattore D (5.000 - x - y - z) e' l'errore di sottrarre invece di riaggiungere l'intersezione.

<sub>confidenza: alta · fase: tarata</sub>

### 134 → **D**

Poiche' ogni presente e' azionista, dipendente o entrambi, l'unione vale 100%. Per inclusione-esclusione l'intersezione e' 62 + 47 - 100 = 9%. Gli azionisti NON dipendenti sono quindi 62 - 9 = 53%. Il distrattore E (62%) e' il totale azionisti senza togliere la sovrapposizione, il distrattore B (38%) e' il complemento dei dipendenti.

<sub>confidenza: alta · fase: tarata</sub>

### 135 → **A**

Fattorizzo: 90 = 2·3^2·5, 196 = 2^2·7^2, 300 = 2^2·3·5^2, quindi M = 2^2·3^2·5^2·7^2 = 44.100 (verificato in Python con gcd/lcm). Testando i divisori: 44.100/700 = 63, /900 = 49, /2.100 = 21, /4.900 = 9 sono interi, mentre 44.100/600 = 73,5 non lo e' perche' 600 = 2^3·3·5^2 richiede 2^3 mentre M ha solo 2^2. Quindi 600 non e' un fattore.

<sub>confidenza: alta · fase: tarata</sub>

### 136 → **D**

Dalla didascalia del grafico ASCII i valori sono 20, 12, 18, 10, 16, 8 (ho verificato che le sei etichette corrispondano alle sei barre, secondo l'accortezza sui conteggi da figura). Variazioni percentuali calcolate in Python: 1->2 = -40%, 2->3 = +50%, 3->4 = -44,4%, 4->5 = +60%, 5->6 = -50%. La massima in modulo e' +60% da Day 4 a Day 5. Nota: la domanda chiede la magnitudine, quindi si confrontano i valori assoluti e non solo i cali.

<sub>confidenza: alta · fase: tarata</sub>

### 137 → **C**

Item con elenco I/II/III, valutato caso per caso. 20! contiene tutti i fattori da 1 a 20, quindi e' divisibile per 15, 17 e 19; percio' n = 20! + 17 ha lo stesso resto di 17 modulo ciascuno. 17 mod 15 = 2 (I no), 17 mod 17 = 0 (II si'), 17 mod 19 = 17 (III no). Calcolo diretto in Python su 20!+17: resti 2, 0, 17. Solo II.

<sub>confidenza: alta · fase: tarata</sub>

### 138 → **D**

Problema di cambio valuta a due passaggi: seguo la catena di unita' invece di moltiplicare i tassi. Costo: 480 marchi / 1,6 marchi per dollaro = 300 $. Ricavo: 2.385 franchi / 5,3 franchi per dollaro = 450 $. Profitto lordo = 450 - 300 = 150 $.

<sub>confidenza: alta · fase: tarata</sub>

### 139 → **D**

Sia g il maggiore (il meno negativo) e L il minore, con L = 2g - 4 e L·g = 160. Sostituendo: 2g^2 - 4g - 160 = 0, cioe' g^2 - 2g - 80 = 0, con radici g = 10 e g = -8. Poiche' entrambi i numeri devono essere negativi si scarta g = 10 (darebbe L = 16, positivi) e resta g = -8, con L = 2(-8) - 4 = -20; verifica: (-8)(-20) = 160 e -20 < -8. Il distrattore A (-20) e' il numero minore, non quello chiesto.

<sub>confidenza: alta · fase: tarata</sub>

### 140 → **B**

N(t) = -20(t-5)^2 + 500 e' una parabola con concavita' verso il basso e vertice in t = 5, dove il quadrato si annulla e N vale 500 (massimo), con t = 5 dentro l'intervallo ammesso 0 <= t <= 10. Poiche' t si conta a partire dalle 2:00 del mattino, il massimo cade alle 2:00 + 5 ore = 7:00. Applico l'accortezza sull'ultimo passaggio di conversione (ore -> orario), che qui e' proprio il punto della domanda: il distrattore A (5:30) e' il valore di t letto come orario.

<sub>confidenza: alta · fase: tarata</sub>

### 141 → **A**

A 8 minuti per miglio, in 50 minuti percorre 50/8 = 6,25 miglia in tutto. Se corre ancora d miglia verso sud, deve poi tornare indietro per 3,25 + d miglia, quindi d + (3,25 + d) = 6,25, da cui 2d = 3 e d = 1,5. Il distrattore C (3,0) e' il valore di 2d, il distrattore D (3,25) e' la distanza gia' percorsa.

<sub>confidenza: alta · fase: tarata</sub>

### 142 → **D**

Il primo deposito x resta due anni e diventa x(1,08)^2; il secondo deposito x, fatto dopo un anno, resta un anno e diventa x(1,08). Quindi w = x(1,08 + 1,08^2) e x = w / (1,08 + (1,08)^2). Verifica numerica: con x = 1 si ha w = 1,08 + 1,1664 = 2,2464 e w/(1,08+1,08^2) = 1. Refuso del libro: le opzioni scrivono W maiuscola mentre l'enunciato usa w minuscola, e l'opzione E ha una forma malformata; la sostanza non cambia.

<sub>confidenza: alta · fase: tarata</sub>

### 143 → **A**

M e' la somma di 100 termini 1/k con k da 201 a 300. Ciascun termine e' compreso fra 1/300 e 1/201, quindi 100·(1/300) < M < 100·(1/201), cioe' 1/3 < M < 0,4975 < 1/2. Il calcolo esatto con Fraction da' M = 0,40463, che sta effettivamente fra 1/3 = 0,333 e 1/2.

<sub>confidenza: alta · fase: tarata</sub>

### 144 → **E**

Lavoro con i ritmi: A e B insieme fanno 800 chiodi in x ore, quindi ritmo congiunto 800/x; A da solo 800/y. Il ritmo di B e' 800/x - 800/y = 800(y-x)/(xy), quindi il tempo di B e' 800 diviso quel ritmo, cioe' xy/(y-x). Il distrattore D (xy/(x-y)) e' il segno invertito: poiche' insieme sono piu' veloci di A da solo si ha x < y, quindi il denominatore corretto e' y-x, positivo.

<sub>confidenza: alta · fase: tarata</sub>

### 145 → **E**

Cesto 1: 4 mele su 6; cesto 2: 3 mele su 8. I due casi favorevoli sono (mela dal primo, arancia dal secondo) e (arancia dal primo, mela dal secondo): (4/6)(5/8) + (2/6)(3/8) = 20/48 + 6/48 = 26/48 = 13/24 (verificato con Fraction). L'errore tipico e' contare un solo ordine, che darebbe 5/12; il distrattore D (5/24) corrisponde a uno dei due addendi mal calcolato.

<sub>confidenza: alta · fase: tarata</sub>

### 146 → **E**

Domanda di approssimazione con opzioni distanti un ordine di grandezza, quindi non arrotondo prima di moltiplicare. Numero totale di rivenditori = 403 × 98 = 39.494; paia totali = 39.494 × 2.488 = 98.261.072, cioe' circa 9,83·10^7. Il rapporto con 10^8 e' 0,98, mentre con 10^7 sarebbe 9,8: il valore piu' vicino e' 10^8.

<sub>confidenza: alta · fase: tarata</sub>

### 147 → **C**

Le sei cifre di 1k2,k24 sono 1, k, 2, k, 2, 4, quindi la somma delle cifre e' 9 + 2k. Serve che 9 + 2k sia divisibile per 3: poiche' 9 lo e', occorre 2k divisibile per 3, cioe' k multiplo di 3. Le cifre ammesse sono k = 0, 3, 6, 9 (verificato con ciclo in Python), quindi quattro valori possibili di n. Il distrattore E (dieci) e' il numero di cifre senza il vincolo.

<sub>confidenza: alta · fase: tarata</sub>

### 148 → **B**

Blu nel sacchetto P: 10,8% di 37 = 3,996 cioe' 4; nel sacchetto R: 50% di 32 = 16; nel sacchetto Q: 66,7% di x, cioe' (2/3)x (le percentuali sono arrotondate al decimo, quindi le leggo come 4/37 e 2/3 esatti). Il totale delle biglie e' 69 + x e i blu devono essere un terzo del totale: 4 + 16 + (2/3)x = (69 + x)/3, cioe' 20 + 2x/3 = 23 + x/3, quindi x/3 = 3 e x = 9. Verifica: 4 + 6 + 16 = 26 blu su 78 biglie totali, esattamente un terzo.

<sub>confidenza: alta · fase: tarata</sub>

### 149 → **A**

Con 161 dipendenti la mediana e' il valore in posizione (161+1)/2 = 81 nella lista ordinata per eta'. Frequenze cumulate: meno di 20 anni = 29, fino a 29 anni = 29 + 58 = 87. L'81esimo cade quindi nella fascia 20-29, e la mediana m soddisfa necessariamente 20 <= m <= 29. Applico l'accortezza media-contro-mediana: la mediana si legge dalla lista ordinata (qui gia' ordinata per fascia di eta'), non dal centro della tabella; le fasce piu' ampie B, C, D non sono vincoli che m 'deve' soddisfare.

<sub>confidenza: alta · fase: tarata</sub>

### 150 → **E**

Riscrivo k! come k·(k-1)! e raccolgo (k-1)!: k·(k-1)! + (n-k)·(k-1)! = (k-1)!·[k + (n-k)] = n·(k-1)!. Verifica esaustiva in Python per k da 1 a 6 e n da k+1 a 8: l'identita' k! + (n-k)(k-1)! = n(k-1)! vale sempre (assert superato). Quindi l'espressione equivale a n·(k-1)!.

<sub>confidenza: alta · fase: tarata</sub>

### 151 → **E**

Barbara = Ron + 1 = 65, quindi Ron = 64; Ron = Amy + 4, quindi Amy = 60. Le tre altezze ordinate sono 60, 64, 65. Applico la lezione 7: la mediana e' il valore centrale della lista ORDINATA, cioe' 64 (la media sarebbe 63, che compare come distrattore D). Risposta 64.

<sub>confidenza: alta · fase: tarata</sub>

### 152 → **E**

Domanda con elenco I/II/III: valuto ogni caso separatamente. Con x + y = 1 scrivo 100x + 200y = 100(x+y) + 100y = 100 + 100y. Poiche' x e y sono entrambi positivi, 0 < y < 1, quindi il valore sta strettamente tra 100 e 200. I (80) e' fuori intervallo; II (140) si ottiene con y = 0,4 e x = 0,6; III (199) con y = 0,99 e x = 0,01. Quindi solo II e III.

<sub>confidenza: alta · fase: tarata</sub>

### 153 → **D**

0,1X e' il numero 0,1X con X cifra delle centesime: per massimizzare il rapporto prendo X = 9, cioe' 0,19. 0,02Y ha Y come cifra delle millesime: per massimizzare il rapporto minimizzo il denominatore con Y = 1 (le cifre devono essere non nulle), cioe' 0,021. Il rapporto e' 0,19/0,021 = 9,0476, il cui valore piu' vicino tra le opzioni e' 9. Attenzione al distrattore 10 (che si otterrebbe con 0,2/0,02, ma X e Y devono essere non nulli).

<sub>confidenza: alta · fase: tarata</sub>

### 154 → **C**

Ogni coppia di squadre gioca esattamente una partita, quindi il numero di partite e' il numero di coppie non ordinate: C(12,2) = 12x11/2 = 66. Verificato con python (comb(12,2) = 66). Il distrattore B (132) e' 12x11, cioe' il conteggio ordinato senza dividere per 2; A (144) e' 12^2.

<sub>confidenza: alta · fase: tarata</sub>

### 155 → **E**

Perche' l'espressione sia reale servono due condizioni annidate: (1) 2 - sqrt(x) >= 0, cioe' sqrt(x) <= 2, cioe' x <= 4; (2) 1 - sqrt(2 - sqrt(x)) >= 0, cioe' 2 - sqrt(x) <= 1, cioe' sqrt(x) >= 1, cioe' x >= 1. Quindi l'espressione e' definita esattamente per 1 <= x <= 4: i valori 1, 2, 3, 4 vanno bene, mentre x = 5 viola la prima condizione (2 - sqrt(5) < 0). La domanda chiede dove NON e' definita, quindi 5.

<sub>confidenza: alta · fase: tarata</sub>

### 156 → **D**

Refuso del libro: il testo e' 'when What is the remainder 3^19 is divided by 10?', con la parola 'when' fuori posto; la domanda e' evidentemente 'qual e' il resto di 3^19 diviso 10'. Le ultime cifre di 3^n hanno ciclo di periodo 4: 3, 9, 7, 1. Poiche' 19 = 4x4 + 3, il resto corrisponde al terzo elemento del ciclo, cioe' 7. Verificato con python: pow(3,19,10) = 7.

<sub>confidenza: alta · fase: tarata</sub>

### 157 → **E**

Con 200 persone: cellulare 80%, cercapersone 45%, unione 100% (tutti hanno almeno uno). Per inclusione-esclusione l'intersezione e' 80 + 45 - 100 = 25% che possiede entrambi. L'insieme richiesto 'non possiede il cellulare OPPURE non possiede il cercapersone' e' per De Morgan il complementare di 'possiede entrambi', quindi 100% - 25% = 75%. E' un caso di complemento richiesto (lezione 1): calcolo prima la quantita' esplicita (25% con entrambi) e poi sottraggo da 100, evitando il distrattore 25% o 55%.

<sub>confidenza: alta · fase: tarata</sub>

### 158 → **B**

Pongo il prezzo di inizio anno = 100. Fine primo trimestre: 120. Fine secondo trimestre: 150 (sempre rispetto a inizio anno, non composto sul trimestre precedente). L'aumento percentuale dal primo al secondo trimestre si calcola sulla base del primo trimestre: (150 - 120)/120 = 30/120 = 25%. Il distrattore 30% e' l'aumento assoluto in punti, non la variazione relativa.

<sub>confidenza: alta · fase: tarata</sub>

### 159 → **D**

La successione e' 1/2, 1/4, 1/8, ..., cioe' il termine n-esimo e' 1/2^n. Il decimo termine e' 1/2^10 = 1/1024 = 0,0009765625. Questo valore e' maggiore di 0,0001 e minore di 0,001, quindi soddisfa 0,0001 < x < 0,001. Verificato numericamente con python.

<sub>confidenza: alta · fase: tarata</sub>

### 160 → **E**

Sviluppo il secondo membro: x(y + z) = xy + xz. L'equazione xy + z = xy + xz si semplifica in z = xz, cioe' z - xz = 0, cioe' z(1 - x) = 0. Quindi necessariamente z = 0 oppure x = 1. Le opzioni A, B, C impongono condizioni piu' forti che non devono valere sempre (es. x = 2, z = 0, y qualsiasi soddisfa l'equazione senza che x = 0 o y = 1); D e' falsa perche' y = 0 non basta (con y = 0 resta z = xz). Quindi E.

<sub>confidenza: alta · fase: tarata</sub>

### 161 → **E**

Le due pompe insieme riempiono la piscina in 4 ore, quindi il tasso combinato e' 1/4 piscina/ora. Sia r il tasso della pompa lenta: r + 1,5r = 2,5r = 1/4, da cui r = 1/10. La pompa veloce ha tasso 1,5r = 0,15 = 3/20 piscina/ora, quindi impiega da sola 1/(3/20) = 20/3 ore (circa 6,67). Il distrattore D (6) sarebbe il caso di rapporto 1:2, e B (16/3) e' il tempo della pompa lenta invertito per errore.

<sub>confidenza: alta · fase: tarata</sub>

### 162 → **A**

Per 0 < x < 1 le potenze crescenti rimpiccioliscono e la radice ingrandisce: x^3 < x^2 < x < sqrt(x) < 1 < x^(-1). Verifica con x = 0,25: 0,0156 < 0,0625 < 0,25 < 0,5 < 4. La lista ordinata dei cinque valori e' quindi (x^3, x^2, x, sqrt(x), x^(-1)) e il terzo elemento, cioe' la mediana, e' x. Applico la lezione 7: la mediana si legge sulla lista riordinata, non sull'ordine in cui i valori sono elencati nel testo.

<sub>confidenza: alta · fase: tarata</sub>

### 163 → **C**

Pongo Kaye = 5t e Alberto = 3t. Dopo il regalo di 10 francobolli: (5t - 10)/(3t + 10) = 7/5, quindi 25t - 50 = 21t + 70, cioe' 4t = 120 e t = 30. Allora Kaye aveva 150 e Alberto 90; dopo il regalo Kaye ha 140 e Alberto 100. La domanda chiede la differenza DOPO il regalo (quantita' derivata, non i totali appena calcolati): 140 - 100 = 40. I distrattori D (60 = differenza iniziale) ed E (90) confermano il rischio di rispondere alla quantita' sbagliata.

<sub>confidenza: alta · fase: tarata</sub>

### 164 → **E**

1,5 deviazioni standard valgono 1,5 x 0,3 = 0,45, quindi l'intervallo 'entro 1,5 sd dalla media' e' [8,1 - 0,45; 8,1 + 0,45] = [7,65; 8,55]. Scorro i 12 valori elencati: 7,51 sta fuori (sotto 7,65); tutti gli altri (8,22; 7,86; 8,36; 8,09; 7,83; 8,30; 8,01; 7,73; 8,25; 7,96; 8,53) cadono dentro, incluso 8,53 che e' sotto 8,55. Conteggio verificato con python: 11 valori dentro, 1 fuori. Ho applicato la lezione 12 controllando che 11 + 1 = 12, il totale dichiarato.

<sub>confidenza: alta · fase: tarata</sub>

### 170 → **E**

Attenzione al linguaggio 'percent greater' (aumento percentuale, non 'percento di'): '300 percento maggiore' significa moltiplicare per 1+3 = 4, e '400 percento maggiore' significa moltiplicare per 1+4 = 5. Quindi 1993 = 5N e 1994 = 4 x 5N = 20N. Il distrattore classico e' D (12N), che nasce dal leggere '300 percento maggiore' come 'il 300% di', cioe' 3 x 4 = 12.

<sub>confidenza: alta · fase: tarata</sub>

### 171 → **D**

Da x/|y| = -1 segue x = -|y|, con y diverso da 0 e x negativo. Elevando al quadrato: x^2 = |y|^2 = y^2, quindi D e' sempre vera. Le altre cadono con un controesempio: y = -3 da' |y| = 3 e x = -3, ma -y = +3, quindi A e' falsa; B e' falsa perche' x = -3 e y = -3 la soddisferebbe ma con y = +3, x = -3 no; C darebbe x = 9 (positivo, impossibile) ed E darebbe x^3 = y^3 cioe' x = y, falsa per y = 3. Applicata la lezione 25: verificare il 'must be true' con differenze/algebra e non con un solo esempio.

<sub>confidenza: alta · fase: tarata</sub>

### 172 → **A**

La colonna centrale e' interamente nota: 1 x sqrt(6) x 6 = 6sqrt(6) = P, prodotto comune. Dalla riga 1: A x 1 x 2sqrt(3) = 6sqrt(6) -> A = 3sqrt(2). Dalla colonna 1: 3sqrt(2) x B x sqrt(3) = 6sqrt(6) -> B = 2. Dalla riga 2: 2 x sqrt(6) x C = 6sqrt(6) -> C = 3. Dalla riga 3: sqrt(3) x 6 x D = 6sqrt(6) -> D = sqrt(2). Verificate tutte righe e colonne numericamente (ognuna vale 14,6969 = 6sqrt(6)); ABCD = 3sqrt(2) x 2 x 3 x sqrt(2) = 36.

<sub>confidenza: alta · fase: tarata</sub>

### 173 → **A**

Pongo il totale di maggio T = 100: Mrs. Lee 60, resto della famiglia 40. A giugno lei guadagna il 20% in piu': 60 x 1,20 = 72; il resto resta 40, quindi il nuovo totale e' 112 (non 100 - il denominatore cambia, ed e' qui l'errore tipico che porta a rispondere 72%, opzione C). 72/112 = 0,6429, cioe' circa 64%.

<sub>confidenza: alta · fase: tarata</sub>

### 174 → **B**

Ridurre il tempo di 1/3 significa nuovo tempo = (2/3)t (lezione 19 sull'interpretazione relativa delle variazioni frazionarie). La distanza e' la stessa: v x t = (v+15) x (2/3)t; il tempo si semplifica dando v = (2/3)(v+15), cioe' 3v = 2v + 30 e v = 30. Verifica: a 30 mph con t = 1 h la distanza e' 30 miglia; a 45 mph servono 2/3 h, esattamente un terzo in meno.

<sub>confidenza: alta · fase: tarata</sub>

### 175 → **E**

Valuto una per una: A) x^4 >= 1 equivale a |x| >= 1, cioe' due semirette; B) x^3 <= 27 equivale a x <= 3, una semiretta infinita; C) x^2 >= 16 equivale a |x| >= 4, due semirette; D) 2 <= |x| <= 5 da' [-5,-2] unito [2,5], due segmenti distinti, non uno solo; E) 2 <= 3x+4 <= 6 da' -2 <= 3x <= 2, cioe' -2/3 <= x <= 2/3, un unico segmento di lunghezza finita 4/3. Il distrattore e' D, che e' limitato ma non connesso.

<sub>confidenza: alta · fase: tarata</sub>

### 176 → **B**

La nuova curva e' la stessa traslata verso l'alto di 2. I punti critici di f(x) = (x+1)(x-1)^2 si trovano da f'(x) = (x-1)(3x+1): massimo locale in x = -1/3 con f = 32/27 = 1,185 e minimo locale in x = 1 con f = 0. Sommando 2 il massimo locale diventa 3,185 e il minimo locale 2, entrambi strettamente positivi, quindi la curva non riattraversa l'asse nella zona centrale; resta solo l'attraversamento del ramo sinistro che scende a meno infinito. La scansione numerica su [-5,5] conferma un unico cambio di segno, vicino a x = -1,359.

<sub>confidenza: alta · fase: tarata</sub>

### 177 → **E**

Con 10 persone la quota e' x/10, con 16 e' x/16; con MENO persone la quota e' maggiore, quindi il costo in piu' per persona e' x/10 - x/16. Denominatore comune 80: (8x - 5x)/80 = 3x/80. Verificato numericamente: 1/10 - 1/16 = 0,0375 = 3/80. Il distrattore D (3x/40) nasce da un errore nel denominatore comune, e A (x/6) dal sottrarre i numeri di persone invece delle quote.

<sub>confidenza: alta · fase: tarata</sub>

### 178 → **D**

La frase 'li elenchera' nell'ordine in cui sono scelti' rende il conteggio ordinato: si tratta di permutazioni, non di combinazioni. P(10,4) = 10 x 9 x 8 x 7 = 5.040. Il distrattore C (210) e' C(10,4), cioe' il conteggio non ordinato, mentre E (151.200) e' P(10,5).

<sub>confidenza: alta · fase: tarata</sub>

### 179 → **D**

Fattorizzo 990 = 2 x 3^2 x 5 x 11. Perche' n! sia divisibile per 990 serve il fattore primo 11, che compare per la prima volta in 11!, quindi n >= 11. Verificato con Python: 10! mod 990 = 450 (non divisibile), 11! mod 990 = 0. Il fattore vincolante e' il primo piu' grande, 11.

<sub>confidenza: alta · fase: tarata</sub>

### 180 → **C**

Dai complementi: P(M) = 1 - 0,8 = 0,2 e P(R) = 1 - 0,6 = 0,4. Poiche' M e R non possono verificarsi entrambi, sono mutuamente esclusivi e P(M o R) = 0,2 + 0,4 = 0,6 = 3/5, senza sottrarre alcuna intersezione. E' un item della categoria 'probabilita' con complemento': ho calcolato prima esplicitamente le probabilita' dirette dai complementi dati e solo dopo sommato. Il distrattore E (12/25 = 0,48) e' il prodotto 0,8 x 0,6, cioe' il caso indipendente, qui escluso dall'ipotesi.

<sub>confidenza: alta · fase: tarata</sub>

### 181 → **C**

Costo totale = 10.000 + 3 x 20.000 = 70.000 dollari; ricavo = 8 x 20.000 = 160.000; profitto lordo = 90.000. Profitto per attrezzo = 90.000/20.000 = 4,50 dollari. Il distrattore D (5,00) e' il margine unitario 8 - 3 che ignora il costo fisso di 10.000, il quale spalmato su 20.000 pezzi vale 0,50 per pezzo.

<sub>confidenza: alta · fase: tarata</sub>

### 182 → **A**

Con Q dispari, la mediana di Q interi consecutivi coincide con il termine centrale, cioe' 120, e ci sono (Q-1)/2 termini sopra di essa, ciascuno a passo 1. Quindi il massimo e' 120 + (Q-1)/2. Verifica con Q = 5: la lista e' 118,119,120,121,122, massimo 122 = 120 + (5-1)/2. Applicata la lezione 6 sui termini centrali di liste consecutive; le opzioni con Q/2 non sono intere per Q dispari.

<sub>confidenza: alta · fase: tarata</sub>

### 183 → **A**

(t/1000)^4 = t^4 x 10^-12. Calcolando con Decimal in Python: t=3 da' 0,000000000081 (10 zeri), t=5 da' 0,000000000625 (9 zeri), t=9 da' 0,000000006561 (8 zeri). La condizione richiede MENO di 8 zeri, cioe' al piu' 7: nessuno dei tre valori la soddisfa (t=9 ne ha esattamente 8, che non e' 'fewer than 8'). Algebricamente serve t^4 x 10^-12 >= 10^-8, cioe' t^4 >= 10.000, cioe' t >= 10. Risposta A. Il caso limite III e' l'insidia: chi confonde 'non piu' di 8' con 'meno di 8' risponde D.

<sub>confidenza: alta · fase: tarata</sub>

### 184 → **B**

Conto per complemento sul vincolo congiunto. Senza il terzo vincolo: prima cifra 8 possibilita' (da 2 a 9, escluse 0 e 1), seconda cifra 2 possibilita' (0 o 1), terza cifra 10, totale 8 x 2 x 10 = 160. Sottraggo i codici proibiti, quelli con seconda e terza cifra entrambe 0: 8 x 1 x 1 = 8. 160 - 8 = 152. Il distrattore C (160) e' proprio il conteggio senza l'ultimo vincolo.

<sub>confidenza: alta · fase: tarata</sub>

### 185 → **E**

Sia a la quantita' di soluzione al 2% e 60 - a quella al 12%: 0,02a + 0,12(60 - a) = 0,05 x 60 = 3. Sviluppando: 7,2 - 0,10a = 3, quindi a = 42 litri (verificato numericamente: 42). Controllo con le distanze dalla media (regola della leva): 5 dista 3 dal 2% e 7 dal 12%, quindi il rapporto 2% : 12% e' 7 : 3, cioe' 42 e 18 litri. Il distrattore A (18) e' proprio la quantita' dell'altra soluzione: la domanda chiede quella al 2%.

<sub>confidenza: alta · fase: tarata</sub>

### 186 → **E**

Sia J il peso di Jake e S quello della sorella: J - 8 = 2S e J + S = 278. Sostituendo S = 278 - J: J - 8 = 556 - 2J, quindi 3J = 564 e J = 188. Verifica: sorella 90, Jake dopo il calo 180 = 2 x 90, somma attuale 188 + 90 = 278. La domanda chiede il peso ATTUALE, non quello dopo il calo (180 non e' tra le opzioni, ma il rischio di rispondere con la quantita' sbagliata e' quello segnalato dalla lezione 10).

<sub>confidenza: alta · fase: tarata</sub>

### 187 → **B**

Una trasformazione lineare y = ax + b scala la deviazione standard del fattore |a| e la traslazione b non la altera (sposta la media, non la dispersione). Quindi nuova SD = 0,8 x 20 = 16. Il distrattore E (40) verrebbe da chi somma anche il 20 della traslazione, e C (28) da 0,8x20+20 calcolato male; la costante additiva va ignorata.

<sub>confidenza: alta · fase: tarata</sub>

### 188 → **B**

Inclusione-esclusione a tre insiemi: |E u F u I| = 26 + 26 + 32 - |E∩F| - |E∩I| - |F∩I| + |E∩F∩I|. Poiche' nessuno ha viaggiato sia in Inghilterra sia in Francia, |E∩F| = 0 e di conseguenza anche l'intersezione tripla e' 0 (essendo contenuta in E∩F). Quindi 84 - 0 - 6 - 11 + 0 = 67. Il distrattore E (79) dimentica una delle sovrapposizioni.

<sub>confidenza: alta · fase: tarata</sub>

### 189 → **C**

Incremento percentuale = (385 - 320)/320 = 65/320 = 0,203125, cioe' circa 20%. Il denominatore e' il valore dell'anno scorso (base di partenza), non quello di quest'anno: usare 385 darebbe circa 17%, che e' esattamente il distrattore B. D (65%) e' la differenza assoluta in milioni scambiata per percentuale.

<sub>confidenza: alta · fase: tarata</sub>

### 190 → **B**

Se x = qy + r con quoziente intero 96 e resto 9, allora x/y = 96 + 9/y; confrontando con 96,12 si ha 9/y = 0,12, quindi y = 9/0,12 = 75. Verifica: x = 96,12 x 75 = 7.209 e 7209 diviso 75 da' quoziente 96 e resto 9. Il distrattore A (96) e' il quoziente, non il divisore.

<sub>confidenza: alta · fase: tarata</sub>

### 191 → **B**

La prima equazione x(2x+1)=0 ha soluzioni x=0 e x=-1/2. La seconda (x+1/2)(2x-3)=0 ha soluzioni x=-1/2 e x=3/2. Poiche' devono valere entrambe simultaneamente, x deve appartenere all'intersezione dei due insiemi di radici: l'unico valore comune e' x=-1/2. I distrattori C (0) e E (3/2) sono le radici che soddisfano una sola delle due equazioni.

<sub>confidenza: alta · fase: tarata</sub>

### 192 → **A**

Le classi totali sono 32 scuole x 2 = 64, con 37 insegnanti. Detti a, b, c il numero di insegnanti che tengono 1, 2, 3 classi: a+b+c=37 e a+2b+3c=64. Sottraendo si ottiene b+2c=27, con c=n. Il minimo e' n=0 (b=27, a=10, tutti non negativi); il massimo si ha rendendo b minimo: b=27-2c>=0 da' c<=13,5, quindi c=13 con b=1 e a=23 (23+1+13=37, 23+2+39=64). Verifica esaustiva con Python: n varia da 0 a 13.

<sub>confidenza: alta · fase: tarata</sub>

### 193 → **B**

Categoria insidiosa media-contro-mediana: ho ricavato la mediana riordinando esplicitamente la lista. I cinque numeri n, n+1, n+2, n+4, n+8 sono gia' in ordine crescente, quindi la mediana e' il terzo valore, n+2. La media e' (5n+15)/5 = n+3. La differenza media - mediana e' (n+3)-(n+2)=1, indipendente da n. Il distrattore A (0) corrisponderebbe a una lista simmetrica, che qui non lo e'.

<sub>confidenza: alta · fase: tarata</sub>

### 194 → **E**

Sia t il numero attuale di insegnanti; gli studenti sono 30t. Dopo le variazioni: (30t+50)/(t+5)=25, cioe' 30t+50=25t+125, da cui 5t=75 e t=15. Verifica: 450 studenti e 15 insegnanti danno 30:1; poi 500 studenti e 20 insegnanti danno 25:1. La domanda chiede il numero di insegnanti (15), non quello di studenti, quindi ho controllato di rispondere alla grandezza richiesta.

<sub>confidenza: alta · fase: tarata</sub>

### 195 → **B**

Riscrivo la base comune: 25^n = (5^2)^n = 5^(2n). La disuguaglianza 5^(2n) > 5^12 con base 5 > 1 equivale a 2n > 12, cioe' n > 6. Il piu' piccolo intero strettamente maggiore di 6 e' 7. Il distrattore A (6) e' il caso di uguaglianza 25^6 = 5^12, che non soddisfa la disuguaglianza stretta.

<sub>confidenza: alta · fase: tarata</sub>

### 196 → **C**

Probabilita' composta su due rami: P(donna) = 0,60 e P(avvocato | donna) = 0,45. La probabilita' di selezionare una donna avvocato e' il prodotto 0,60 x 0,45 = 0,27. Non serve il complemento qui: la domanda chiede proprio la quantita' calcolata direttamente. Il distrattore E (0,45) e' la probabilita' condizionata non pesata.

<sub>confidenza: alta · fase: tarata</sub>

### 197 → **D**

Un aumento di 1/4 rispetto all'anno precedente moltiplica il numero per 5/4 ogni anno (lezione sulle variazioni relative: x(1+1/4), non x/4). Dopo 4 anni: x(5/4)^4 = 6.250, quindi x = 6.250 x (4/5)^4 = 6.250 x 256/625 = 2.560. Verifica con Python: 6250*(0.8)^4 = 2560. Il distrattore A (1.250) sarebbe 6.250/5, cioe' un'unica divisione.

<sub>confidenza: alta · fase: tarata</sub>

### 198 → **C**

Sono 11 anni (1990-2000), quindi la mediana e' il 6o valore della lista ORDINATA, non il valore dell'anno centrale del grafico (lezione 7: riordinare sempre). Dalla didascalia la serie sale da circa 190.000 nel 1990 fino al picco di circa 380.000 nel 1998 e poi scende a circa 260.000 nel 2000. Ordinando i valori (circa 171k, 188k, 211k, 254k, 304k, 340k, 348k, 354k, 363k, 373k, con 250k del 2000 inserito nella parte bassa), il 6o valore piu' piccolo sta attorno a 300-310 mila, quindi l'opzione piu' vicina e' 310.000. Il disegno ASCII e' reso in modo impreciso (le barre visibili sono meno degli 11 anni), quindi mi sono basato sulla didascalia numerica; da qui la confidenza non massima.

<sub>confidenza: **media** · fase: tarata</sub>

### 199 → **B**

Scompongo 72 = 8 x 9 = 2^3 x 3^2. La notazione 2^k || 72 richiede che 2^k divida 72 ma 2^(k+1) no: 2^3 = 8 divide 72 (72/8 = 9), mentre 2^4 = 16 non divide 72 (72/16 = 4,5). Quindi k = 3. I distrattori D (8) ed E (18) sono rispettivamente 2^3 e 72/4, cioe' valori che confondono la potenza con il suo valore.

<sub>confidenza: alta · fase: tarata</sub>

### 200 → **D**

La distribuzione e' simmetrica attorno a m e il 68% cade nell'intervallo (m-d, m+d). Per simmetria meta' di quel 68%, cioe' 34%, sta tra m e m+d. La porzione minore di m e' il 50%. Quindi la percentuale minore di m+d e' 50% + 34% = 84%. Il distrattore A (16%) e' il complemento, cioe' la porzione maggiore di m+d: ho controllato esplicitamente il verso della disuguaglianza richiesta. Nota: nel testo del libro manca uno spazio ('mean $m$.If'), refuso tipografico senza effetto sul contenuto.

<sub>confidenza: alta · fase: tarata</sub>

### 201 → **E**

Ciascuno dei primi tre panini e' diviso fra m studenti, quindi ogni pezzo vale 1/m di panino; Carol ne mangia uno per panino, cioe' 3/m. Il quarto panino e' diviso fra m-4 studenti, quindi il suo pezzo vale 1/(m-4). Totale: 3/m + 1/(m-4) = [3(m-4) + m] / [m(m-4)] = (3m-12+m)/[m(m-4)] = (4m-12)/[m(m-4)]. Verifica numerica con m=6: 3/6 + 1/2 = 1, e (24-12)/(6x2) = 12/12 = 1. Il distrattore C (4m-4) deriva dal dimenticare il -12 nella somma dei numeratori.

<sub>confidenza: alta · fase: tarata</sub>

### 202 → **D**

Se x = 1 + radice(2), allora x - 1 = radice(2); elevando al quadrato: x^2 - 2x + 1 = 2, cioe' x^2 - 2x - 1 = 0. Verifica diretta sostituendo x = 1+radice(2) approssimato a 2,41421: 2,41421^2 - 2(2,41421) - 1 = 5,82843 - 4,82843 - 1 = 0. L'opzione B (x^2-2x+1) e' il quadrato prima di portare il 2 a sinistra ed e' il distrattore principale.

<sub>confidenza: alta · fase: tarata</sub>

### 203 → **B**

Uso una base comoda: 100 lavoratori edili nel 1992, di cui il 16% disoccupati = 16 persone. Nel 1996 i lavoratori sono il 20% in piu', cioe' 120, e i disoccupati sono il 9% di 120 = 10,8. La variazione percentuale del NUMERO di disoccupati e' (10,8 - 16)/16 = -0,325, cioe' un calo del 32,5%, approssimabile a una diminuzione del 30%. Attenzione al tranello: la variazione dei tassi (16 -> 9) suggerirebbe -43,75%, ma la domanda chiede la variazione del numero, non del tasso.

<sub>confidenza: alta · fase: tarata</sub>

### 204 → **C**

Estrazione senza reimmissione: su 12 penne, 9 non sono difettose. P(entrambe non difettose) = C(9,2)/C(12,2) = 36/66 = 6/11. Equivalentemente, passo per passo: (9/12) x (8/11) = 72/132 = 6/11 — qui il numeratore SI aggiorna (9 -> 8) perche' la prima penna estratta era proprio del tipo cercato, a differenza del caso della lezione 2. Il distrattore E (3/4) e' 9/12, cioe' la sola prima estrazione.

<sub>confidenza: alta · fase: tarata</sub>

### 205 → **E**

Converto subito la media in totale (lezione 3): 10 frutti a 56 centesimi = 560 centesimi. Con a mele a 40 e o arance a 60 e a+o=10: 400 + 20o = 560, quindi o = 8 arance e a = 2 mele. Rimettendo indietro x arance: (560 - 60x)/(10 - x) = 52, da cui 560 - 60x = 520 - 52x, quindi 40 = 8x e x = 5. Verifica: restano 2 mele e 3 arance, totale 80+180 = 260 su 5 frutti = 52 centesimi esatti.

<sub>confidenza: alta · fase: tarata</sub>

### 206 → **C**

Primo rapporto royalties/vendite = 3/20 = 0,15; secondo rapporto = 9/108 = 0,08333. La diminuzione percentuale si calcola sulla base iniziale: (0,15 - 0,08333)/0,15 = 0,4444, cioe' circa 44,4%, che si arrotonda a 45%. La domanda chiede la variazione percentuale del RAPPORTO, non la differenza fra i rapporti (che sarebbe circa 6,7 punti, distrattore A = 8%); ho verificato di rispondere alla grandezza derivata richiesta.

<sub>confidenza: alta · fase: tarata</sub>

### 207 → **B**

Simulo il timer con Python: ogni apertura porta lo spegnimento a ora+15 min, e la luce e' spenta negli intervalli tra la scadenza e l'apertura successiva. Catena: 8:00...8:31 (con reset a catena) porta la luce accesa fino alle 8:46, poi buio fino alle 8:54 = 8 minuti. Da 8:54 i reset (8:57, 9:05, 9:11) portano fino alle 9:26, poi buio fino alle 9:29 = 3 minuti. L'ultimo reset alle 9:31 tiene accesa fino alle 9:46, poi buio fino alle 10:00 = 14 minuti. Totale 8+3+14 = 25 minuti.

<sub>confidenza: alta · fase: tarata</sub>

### 208 → **C**

p = 30!, quindi applico la formula di Legendre per l'esponente del primo 3: floor(30/3) + floor(30/9) + floor(30/27) = 10 + 3 + 1 = 14 (i termini successivi sono nulli perche' 81 > 30). Il distrattore A (10) e' il solo primo addendo, cioe' il conteggio dei multipli di 3 senza tener conto dei multipli di 9 e 27 che contribuiscono fattori 3 extra. Verifica con Python: somma = 14.

<sub>confidenza: alta · fase: tarata</sub>

### 209 → **C**

n = 3^8 - 2^8 = 6.561 - 256 = 6.305. Scompongo: 6.305 = 5 x 1.261 = 5 x 13 x 97. Verifica dei resti con Python: 6305 e' divisibile per 97, 65 (=5x13), 13 e 5, mentre 6305/35 lascia resto 5. Il 35 richiederebbe il fattore 7, assente nella fattorizzazione, quindi NON e' un divisore. Attenzione: la domanda chiede quale NON e' fattore, quindi la risposta e' l'unica opzione che fallisce il test.

<sub>confidenza: alta · fase: tarata</sub>

### 210 → **E**

Condizione 1: un tavolo da 3 e gli altri da 4 implica N-3 divisibile per 4; condizione 2: un tavolo da 3 e gli altri da 5 implica N-3 divisibile per 5. Quindi N-3 e' multiplo del mcm(4,5)=20, cioe' N = 23, 43, ...; l'unico valore con 10 < N < 40 e' N = 23 (ricerca esaustiva verificata con Python). Con tavoli da 6: 23 = 3x6 + 5, quindi al tavolo incompleto siedono 5 membri (e 5 < 6, come richiesto). Nota: il testo del libro ha un refuso di spaziatura ('table,and'), ininfluente.

<sub>confidenza: alta · fase: tarata</sub>

### 211 → **B**

Sia D il numero totale di giorni previsti: il totale di pagine e' 90D. Nei primi D-6 giorni ha letto 75 pagine al giorno, e restano 690 pagine per gli ultimi 6 giorni, quindi 90D - 75(D-6) = 690. Sviluppando: 90D - 75D + 450 = 690, cioe' 15D = 240 e D = 16. Verifica: totale 1440 pagine, primi 10 giorni a 75 = 750, restano 690 per 6 giorni (115/giorno). La domanda chiede i GIORNI TOTALI, non i giorni iniziali (10, distrattore implicito), quindi 16.

<sub>confidenza: alta · fase: tarata</sub>

### 212 → **D**

Da sqrt(r/s) = s, elevando al quadrato entrambi i membri si ottiene r/s = s^2, quindi r = s^3. L'elevamento al quadrato e' lecito senza ambiguita' di segno perche' s > 0 (la radice e' non negativa e s pure). Verifica numerica con s = 2: r = 8, sqrt(8/2) = sqrt(4) = 2 = s. Corretto.

<sub>confidenza: alta · fase: tarata</sub>

### 213 → **B**

Serve x/3 = p^2 con p primo, cioe' x = 3p^2, e insieme 3 < x < 100. Da 3p^2 < 100 segue p^2 < 33,33, quindi p puo' valere 2, 3, 5 (p = 7 da' 49 > 33,33). I corrispondenti x sono 12, 27, 75, tutti nell'intervallo aperto (3, 100). Sono tre valori: risposta 'Three'. (Attenzione al distrattore E = Nine, che conta i quadrati generici anziche' i quadrati di primi.)

<sub>confidenza: alta · fase: tarata</sub>

### 214 → **B**

Con n lettere i codici disponibili sono n singole lettere piu' C(n,2) coppie distinte (l'ordine alfabetico impone un unico ordinamento per coppia, quindi si contano combinazioni, non permutazioni). Servono almeno 12 codici: n + C(n,2) da' 10 per n = 4 (insufficiente) e 15 per n = 5 (sufficiente). Il minimo numero di lettere e' quindi 5.

<sub>confidenza: alta · fase: tarata</sub>

### 215 → **B**

La parabola h = -16(t-3)^2 + 150 ha vertice (massimo) in t = 3 con h = 150. Due secondi DOPO il massimo significa t = 5, non t = 2: h = -16(5-3)^2 + 150 = -64 + 150 = 86. Il distrattore D (150) e' l'altezza massima stessa; il distrattore C (134) corrisponde a t = 4, cioe' un solo secondo dopo. Risposta 86.

<sub>confidenza: alta · fase: tarata</sub>

### 216 → **D**

Prima disuguaglianza: x + 6 > 10 da' x > 4 (stretta). Seconda: x - 3 <= 5 da' x <= 8 (debole). L'intersezione e' 4 < x <= 8. Il controllo decisivo qui e' il verso stretto/debole degli estremi: solo l'opzione D ha estremo sinistro aperto ed estremo destro chiuso con i valori 4 e 8.

<sub>confidenza: alta · fase: tarata</sub>

### 217 → **C**

David ha d libri; 'd e' 3 volte quelli di Jeff' significa d = 3J, quindi J = d/3. 'd e' 1/2 di quelli di Paula' significa d = P/2, quindi P = 2d. Totale = d + d/3 + 2d = (3d + d + 6d)/3 = 10d/3. Il rischio qui e' invertire le relazioni (J = 3d o P = d/2), che produrrebbe le opzioni A o B: ho ricontrollato che Jeff ha MENO libri e Paula il DOPPIO.

<sub>confidenza: alta · fase: tarata</sub>

### 218 → **C**

Ogni partita e' una coppia non ordinata di squadre distinte, quindi il numero di partite e' C(8,2) = 8*7/2 = 28. Il distrattore D (56) e' 8*7, cioe' il conteggio ordinato che contarebbe due volte ogni incontro; E (64) e' 8^2.

<sub>confidenza: alta · fase: tarata</sub>

### 219 → **B**

Sia h il tempo stimato e r la tariffa oraria regolare: h*r = 336. Il lavoro e' durato h+4 ore e la paga effettiva per ora e' stata r-2, con lo stesso compenso totale: (h+4)(r-2) = 336. Sottraendo: -2h + 4r - 8 = 0, cioe' h = 2r - 4; sostituendo, 2r^2 - 4r - 336 = 0, r^2 - 2r - 168 = 0, r = 14 (radice positiva) e h = 24. Verifica: 336/24 = 14 $/h stimati, 336/28 = 12 = 14-2. Il tempo STIMATO e' 24 (28 e' quello effettivo, distrattore A).

<sub>confidenza: alta · fase: tarata</sub>

### 220 → **E**

Da p/q < 1 con p, q interi positivi segue p < q, quindi q/p > 1 sempre: E e' l'unica che 'deve' essere maggiore di 1. Le altre falliscono con controesempi: A sqrt(p/q) < 1 perche' radice di un numero minore di 1; B p/q^2 = (p/q)/q < 1; C p/(2q) < 1/2; D q/p^2 con p = 2, q = 3 da' 3/4 < 1. Come da lezione 25, ho verificato il 'must' per via algebrica generale, usando i numeri solo per escludere.

<sub>confidenza: alta · fase: tarata</sub>

### 221 → **A**

Separatamente: pacco da 3 libbre costa x + 2y, pacco da 5 libbre costa x + 4y, totale 2x + 6y. Combinati in un unico pacco da 8 libbre: x + 7y. Differenza (separati meno combinato) = (2x + 6y) - (x + 7y) = x - y, positiva perche' x > y: conviene combinare risparmiando x - y centesimi. Il distrattore B ha il segno invertito, D inverte il metodo.

<sub>confidenza: alta · fase: tarata</sub>

### 222 → **A**

Il tempo di raddoppio approssimato e' 70/r = 70/8 = 8,75 anni. In 18 anni ci stanno circa due raddoppi (17,5 anni), quindi 5.000 -> 10.000 -> 20.000 dollari. Verifica esatta: 5.000 * 1,08^18 = 19.980, coerente con 20.000. Il distrattore D (10.000) corrisponde a un solo raddoppio: la domanda chiede il totale dopo 18 anni, cioe' due periodi di raddoppio.

<sub>confidenza: alta · fase: tarata</sub>

### 223 → **D**

290 arrotondato alla decina piu' vicina implica miglia reali in [285, 295); 12 arrotondato all'unita' implica galloni reali in [11,5, 12,5). Il rapporto miglia/gallone e' minimo con numeratore minimo e denominatore massimo, 285/12,5 = 22,8; massimo con 295/11,5 = 25,65. Questo e' un item di tipo 'unita' composte e limiti di arrotondamento': l'accortezza applicata e' accoppiare gli estremi in modo opposto (min/max e max/min), non min/min come in C o B.

<sub>confidenza: alta · fase: tarata</sub>

### 224 → **E**

Il segmento ombreggiato va da -5 a 3 estremi inclusi. Il centro e' (-5 + 3)/2 = -1 e il raggio (3 - (-5))/2 = 4, quindi la condizione e' |x - (-1)| <= 4, cioe' |x + 1| <= 4. Verifica degli estremi: x = -5 da' |-4| = 4 (incluso), x = 3 da' |4| = 4 (incluso). Il distrattore D (|x - 1| <= 4) ha il segno del centro invertito e descrive [-3, 5].

<sub>confidenza: alta · fase: tarata</sub>

### 225 → **D**

Applico la lezione 3: converto subito le medie in totali. Ricavo totale sui 10 giorni = 400 * 10 = 4.000; ricavo dei primi 6 giorni = 360 * 6 = 2.160; restano 4.000 - 2.160 = 1.840 per gli ultimi 4 giorni, cioe' una media di 1.840/4 = 460 dollari al giorno. Il distrattore B (440) e' il risultato di manipolare le medie direttamente (400 + 40).

<sub>confidenza: alta · fase: tarata</sub>

### 226 → **E**

Fattorizzo 3.150 = 2 * 3^2 * 5^2 * 7. Perche' il prodotto sia un quadrato perfetto ogni esponente deve essere pari: 3 e 5 sono gia' a esponente 2, mentre 2 e 7 compaiono con esponente 1, quindi il minimo y e' 2 * 7 = 14. Verifica: 3.150 * 14 = 44.100 = 210^2. Le opzioni A (2) e D (7) sono i fattori presi singolarmente.

<sub>confidenza: alta · fase: tarata</sub>

### 227 → **A**

La funzione parte intera inferiore (floor) del numero negativo va arrotondata verso il basso: [-1,6] = -2, non -1. Poi [3,4] = 3 e [2,7] = 2. Somma: -2 + 3 + 2 = 3. Il distrattore B (4) nasce proprio dall'usare -1 al posto di -2 per il termine negativo.

<sub>confidenza: alta · fase: tarata</sub>

### 228 → **C**

I risparmi settimanali formano la sequenza 1, 2, 3, ..., 52 (settimana 1 = 1 dollaro, poi ogni settimana 1 in piu' per altre 51 settimane, quindi l'ultimo termine e' 52). La somma e' 52*53/2 = 1.378. Il distrattore D (2.652) e' 52*53 senza dividere per 2; A (1.326) e' la somma fino a 51.

<sub>confidenza: alta · fase: tarata</sub>

### 229 → **C**

Applico la ricorrenza due volte. x2 = 2*x1 - (1/2)*x0 = 2*2 - 1,5 = 2,5. x3 = 2*x2 - (1/2)*x1 = 2*2,5 - 1 = 4. L'opzione A (2,5) e' proprio x2, cioe' il valore intermedio: la domanda chiede x3, quindi bisogna fare il secondo passo (categoria 'quantita' derivata, non quella appena calcolata').

<sub>confidenza: alta · fase: tarata</sub>

### 230 → **E**

Con distanza totale D, la porzione xD/100 e' percorsa a 40 mph e la porzione (100-x)D/100 a 60 mph. Il tempo totale e' D[x/4000 + (100-x)/6000] = D(3x + 200 - 2x)/12.000 = D(x + 200)/12.000. La velocita' media e' distanza/tempo = 12.000/(x + 200): D si semplifica. Verifica numerica: x = 0 da' 60, x = 100 da' 40, x = 50 da' 48 (media armonica corretta, non 50), tutti coincidenti con l'opzione E. L'errore tipico sarebbe mediare le velocita' pesandole sulla distanza anziche' sul tempo.

<sub>confidenza: alta · fase: tarata</sub>

### 231 → **A**

La cifra delle unità di 33^43 dipende solo da 3^43: il ciclo di 3 è 3,9,7,1 con periodo 4, e 43 mod 4 = 3, quindi la terza cifra del ciclo è 7. La cifra delle unità di 43^33 dipende da 3^33: 33 mod 4 = 1, quindi è 3. Somma 7 + 3 = 10, cifra delle unità 0. Verificato con python3 calcolando (33**43 + 43**33) % 10 = 0.

<sub>confidenza: alta · fase: tarata</sub>

### 232 → **D**

Le posizioni maschili sono fisse (1ª, 3ª, 5ª) e quelle femminili pure (2ª, 4ª, 6ª); lo schema M,F,M,F,M,F è imposto. Quindi i 3 maschi si permutano fra loro in 3! = 6 modi e le 3 femmine in 3! = 6 modi. Totale 6 x 6 = 36. Il distrattore E (720 = 6!) corrisponde a ignorare il vincolo di alternanza.

<sub>confidenza: alta · fase: tarata</sub>

### 233 → **B**

Per ottenere una potenza di 10 al denominatore moltiplico numeratore e denominatore per 2^4: d = 2^4 / (2^7 x 5^7) = 16 / 10^7 = 0,0000016. Le cifre non nulle sono 1 e 6, quindi due. Verificato con python3: 1/(2**3*5**7) = 1,6 x 10^-6.

<sub>confidenza: alta · fase: tarata</sub>

### 234 → **B**

Gli interi pari strettamente compresi tra 99 e 301 vanno da 100 a 300, cioè 101 termini. Somma = 2(50 + 51 + ... + 150) = 2[(150·151/2) - (49·50/2)] = 2(11325 - 1225) = 20200; equivalentemente 101 x media 200 = 20200. Verificato con python3 sommando la lista: 20200. Il distrattore E (45150) è la somma di TUTTI gli interi da 100 a 300.

<sub>confidenza: alta · fase: tarata</sub>

### 235 → **A**

Dal 16 novembre 2001 al 16 novembre 2014 passano 13 intervalli annuali: 13 x 365 = 4745 giorni, più 3 giorni bisestili (29 febbraio 2004, 2008, 2012, tutti interni all'intervallo) = 4748 giorni. 4748 mod 7 = 2 (7 x 678 = 4746), quindi si avanza di 2 giorni rispetto a venerdì: domenica. Doppia verifica con datetime di python3: 16/11/2001 venerdì, 16/11/2014 domenica, differenza 4748 giorni.

<sub>confidenza: alta · fase: tarata</sub>

### 236 → **D**

Fattorizzo 7150 = 715 x 10 = (5 x 143) x (2 x 5) = 2 x 5^2 x 11 x 13. I fattori primi distinti sono 2, 5, 11, 13: quattro, tutti compresi tra 1 e 100. Verificato con python3 (fattorizzazione per divisioni successive: {2:1, 5:2, 11:1, 13:1}). Attenzione a contare i primi DISTINTI, non le molteplicità (che darebbero 5, cioè il distrattore E).

<sub>confidenza: alta · fase: tarata</sub>

### 237 → **D**

Se a_n = t con n > 2, allora t è già il prodotto di tutti i termini precedenti, quindi il prodotto dei primi n termini vale t x t = t^2, da cui a_{n+1} = t^2. Il prodotto dei primi n+1 termini è allora t^2 x t^2 = t^4, quindi a_{n+2} = t^4. Verifica numerica con python3 sulla successione 3, 5, 15, 225, 50625, ...: per n = 3, t = 15 e a_5 = 50625 = 15^4; per n = 4, t = 225 e a_6 = 2562890625 = 225^4.

<sub>confidenza: alta · fase: tarata</sub>

### 238 → **D**

Il rapporto passa da P/E a [P(1 + k/100)] / [E(1 + m/100)], quindi il fattore di variazione è (100 + k)/(100 + m) e l'aumento percentuale è 100[(100 + k)/(100 + m) − 1] = 100(k − m)/(100 + m). Controllo numerico con k = 30, m = 10: aumento reale = 100(130/110 − 1) = 200/11 ≈ 18,18%; l'opzione D dà 100(20)/110 = 200/11, mentre C dà 200/13, B dà 20 e A dà 3. Il distrattore B (k − m) è l'errore classico di sottrarre le percentuali senza rapportarle alla base cresciuta.

<sub>confidenza: alta · fase: tarata</sub>

### 239 → **D**

Su 300 soggetti: 120 palmi sudati, 90 vomito, 225 vertigini, somma 435. Detti x1, x2, x3 quanti hanno esattamente uno, due, tre effetti: x1 + x2 + x3 = 300 (tutti hanno almeno un effetto) e x1 + 2x2 + 3x3 = 435 (ogni soggetto è contato tante volte quanti effetti ha). Con x2 = 35% di 300 = 105, sottraendo le due equazioni: x2 + 2x3 = 135, quindi x3 = 15 e x1 = 300 − 105 − 15 = 180. Il distrattore A (105) è proprio il valore intermedio già dato dal testo.

<sub>confidenza: alta · fase: tarata</sub>

### 240 → **D**

Da m^-1 = 1/m = -1/3 segue m = -3. Allora m^-2 = 1/m^2 = 1/(-3)^2 = 1/9, positivo perché l'esponente pari elimina il segno. I distrattori A (-9) e C (-1/9) nascono dal conservare erroneamente il segno negativo, E (9) dal confondere m^-2 con m^2.

<sub>confidenza: alta · fase: tarata</sub>

### 241 → **D**

Il prezzo di 250 $ è un ricarico del 20% sul costo, quindi costo unitario = 250/1,20 = 208,33 $ e costo totale dei 60 pezzi = 12.500 $. Ricavi: 54 macchine vendute a 250 = 13.500 $, più il rimborso delle 6 invendute pari al 50% del costo = 6 x 104,17 = 625 $, totale 14.125 $. Profitto = 14.125 − 12.500 = 1.625 $, cioè 1.625/12.500 = 13% del costo iniziale. Accortezza sul markup: 250 è il 120% del costo, non il costo maggiorato applicando il 20% a 250.

<sub>confidenza: alta · fase: tarata</sub>

### 242 → **D**

Ordino i sette pezzi a1 ≤ ... ≤ a7: la media 68 dà somma 476 e la mediana è a4 = 84, con a7 = 4a1 + 14. Per massimizzare a7 devo massimizzare a1, quindi minimizzo tutto il resto: a2 = a3 = a1 (non possono scendere sotto a1) e a5 = a6 = 84 (non possono scendere sotto la mediana). Allora 3a1 + 84 + 168 + (4a1 + 14) = 476, cioè 7a1 = 210 e a1 = 30, da cui a7 = 4(30) + 14 = 134. Controllo di coerenza dell'ordinamento: 30, 30, 30, 84, 84, 84, 134 ha somma 476, mediana 84, ed è ordinata.

<sub>confidenza: alta · fase: tarata</sub>

### 243 → **E**

Con la formula data, il sesto termine è 6 + 2^5 = 6 + 32 = 38 e il quinto è 5 + 2^4 = 5 + 16 = 21. La differenza è 38 − 21 = 17. (Controllo della formula sui primi termini: n=1 dà 1+1=2, n=2 dà 2+2=4, n=3 dà 3+4=7, coerente con 2, 4, 7 dell'enunciato.) La domanda chiede la differenza, non il termine: il distrattore D (16) è il salto della sola parte esponenziale 2^5 − 2^4.

<sub>confidenza: alta · fase: tarata</sub>

### 244 → **E**

Per rendere il prodotto minimo serve il valore più negativo possibile: modulo massimo (tutti i fattori di modulo 10) e segno negativo (numero dispari di fattori negativi). Scegliendo -10 diciannove volte e +10 una volta si ottiene (-10)^19 x 10 = -10^20, verificato con python3. Le opzioni A e B sono positive, C è nulla, D ha modulo dieci volte più piccolo, quindi il minimo è -(10)^20.

<sub>confidenza: alta · fase: tarata</sub>

### 245 → **D**

Le stringhe distinte con D, G, I, I, T sono 5!/2! = 60 perché le due I sono identiche. Quelle in cui le due I sono adiacenti si contano incollandole in un blocco: 4 oggetti da permutare, 4! = 24 stringhe distinte. Le stringhe con le I separate da almeno un'altra lettera sono 60 − 24 = 36. Verificato per enumerazione esaustiva con python3 (set di permutations): 60 totali, 24 adiacenti, 36 separate.

<sub>confidenza: alta · fase: tarata</sub>

### 246 → **D**

Riconosco le differenze di quadrati: 0,99999999 = 1 − 10^-8 = (1 − 10^-4)(1 + 10^-4), quindi il primo termine è (1 − 10^-4)(1,0001)/1,0001 = 1 − 10^-4 = 0,9999. Analogamente 0,99999991 = 1 − 9x10^-8 = (1 − 3x10^-4)(1 + 3x10^-4), quindi il secondo termine è 1 − 3x10^-4 = 0,9997. La differenza è 0,9999 − 0,9997 = 0,0002 = 2(10^-4). Verificato con Decimal a 50 cifre in python3: risultato esatto 0,0002. Trattandosi di opzioni vicine, ho evitato l'arrotondamento anticipato e usato l'aritmetica esatta.

<sub>confidenza: alta · fase: tarata</sub>

### 247 → **D**

Siano a le copie di A (1,00 $) e b quelle di B (1,25 $). Da p = 100a/(a+b) ricavo b = a(100 − p)/p. Il ricavo è a + 1,25b, quindi r = 100a/(a + 1,25b) = 400a/(4a + 5b); sostituendo b: r = 400a / [4a + 5a(100 − p)/p] = 400p/(4p + 500 − 5p) = 400p/(500 − p). Controllo numerico con python3: per a = b = 1 si ha p = 50 e r = 100/2,25 = 400/9, e l'opzione D dà 400(50)/450 = 400/9; per a = 3, b = 2 si ha p = 60, r = 300/5,5 = 600/11 e D dà 24000/440 = 600/11. Solo D coincide in entrambi i casi.

<sub>confidenza: alta · fase: tarata</sub>

### 248 → **E**

Applico la lezione di lavorare sui totali e non sulle medie: il totale prodotto nei primi n giorni è 50n, e dopo oggi il totale è 50n + 90 su n + 1 giorni con media 55, cioè 50n + 90 = 55(n + 1). Sviluppando: 50n + 90 = 55n + 55, quindi 35 = 5n e n = 7. Verifica: 7 giorni x 50 = 350, più 90 = 440 su 8 giorni = 55 esatti.

<sub>confidenza: alta · fase: tarata</sub>

### 249 → **A**

Sia il numero 10a + b; l'invertito è 10b + a e la differenza è |9(a − b)| = 27, quindi |a − b| = 3. Verificato per enumerazione con python3 su tutti gli interi a due cifre: l'insieme delle differenze di cifre compatibili è esattamente {3} (es. 14 e 41, differenza 27). La risposta chiede la differenza tra le CIFRE (3), non tra i numeri (27).

<sub>confidenza: alta · fase: tarata</sub>

### 250 → **D**

La condizione data è 1/r = 1/x + 1/y = (y + x)/(xy). Invertendo entrambi i membri si ottiene r = xy/(x + y). Il distrattore E è proprio il reciproco (cioè 1/r, il valore intermedio della formula), quindi ho controllato quale grandezza chiede la domanda: r, non 1/r. Controllo dimensionale rapido: con x = y = 2 il parallelo dà r = 1, e xy/(x+y) = 4/4 = 1, corretto.

<sub>confidenza: alta · fase: tarata</sub>

### 251 → **E**

Eventi indipendenti: serve P(X successo) x P(Y successo) x P(Z insuccesso). P(Z insuccesso) = 1 - 5/8 = 3/8. Quindi (1/4)(1/2)(3/8) = 3/64. Ho applicato l'accortezza sul complemento: il complemento va calcolato esplicitamente prima di moltiplicare (5/64 sarebbe il distrattore che usa 5/8 senza complementare).

<sub>confidenza: alta · fase: tarata</sub>

### 252 → **C**

Il primo membro si semplifica: 1/x - 1/(x+1) = (x+1-x)/(x(x+1)) = 1/(x^2+x). L'equazione diventa 1/(x^2+x) = 1/(x+4), quindi x^2 + x = x + 4, cioe' x^2 = 4 e x = 2 oppure x = -2. Fra le opzioni compare solo -2 (e per x=-2 i denominatori -2, -1, 2 sono tutti non nulli, quindi e' valida).

<sub>confidenza: alta · fase: tarata</sub>

### 253 → **B**

Esponenti negativi: (1/2)^-3 = 2^3 = 8, (1/4)^-2 = 4^2 = 16, (1/16)^-1 = 16. Il prodotto e' 8 x 16 x 16 = 2048 = 2^11 = (1/2)^-11. Verificato con Python: log2(2048) = 11. NOTA REFUSO DEL LIBRO: le opzioni C ed E sono identiche ((1/2)^-6), ma cio' non tocca la risposta corretta B.

<sub>confidenza: alta · fase: tarata</sub>

### 254 → **B**

Domanda con elenco I/II/III: valuto ogni caso separatamente cercando i limiti di E-S. 10 decimali (1/3 di 30) hanno decimo pari e vengono arrotondati per eccesso, contribuendo +(1 - parte frazionaria) con parte frazionaria in (0; 0,9], quindi contributo strettamente minore di 1 ciascuno; 20 decimali hanno decimo dispari e vengono arrotondati per difetto, contribuendo -(parte frazionaria) con frazionaria almeno 0,1, quindi al massimo -0,1 ciascuno. Massimo teorico di E-S: strettamente minore di 10x1 - 20x0,1 = 8, quindi III (10) e' impossibile; II (6) si realizza con 10 valori a frazionaria 0,8 (+0,2 ciascuno = +2) e 20 a frazionaria 0,1 (-0,1 ciascuno = -2)... in realta' basta +8 e -2, ad esempio 10 valori a frazionaria 0,2 (+0,8 ciascuno = +8) e 20 a 0,1 (-2): totale 6. I (-16) si ottiene con 10 valori a frazionaria 0,8 (+0,2 ciascuno = +2) e 20 a frazionaria 0,9 (-0,9 ciascuno = -18): 2-18 = -16. Quindi solo I e II.

<sub>confidenza: alta · fase: tarata</sub>

### 255 → **C**

Moltiplico per x (x diverso da 0): 5x - 6 = x^2, cioe' x^2 - 5x + 6 = 0, che fattorizza in (x-2)(x-3) = 0. Le radici sono x = 2 e x = 3, entrambe non nulle e quindi ammissibili. I valori possibili sono due.

<sub>confidenza: alta · fase: tarata</sub>

### 256 → **B**

Problema di miscela: sia p la frazione in peso di X nella miscela. Il loglio (ryegrass) totale e' 0,40p + 0,25(1-p) = 0,30, da cui 0,15p = 0,05 e p = 1/3, cioe' 33 1/3%. Controprova: con 1 kg di X (0,4 rye) e 2 kg di Y (0,5 rye) si ha 0,9 rye su 3 kg = 30%. Il bluegrass e il fescue sono dati irrilevanti.

<sub>confidenza: alta · fase: tarata</sub>

### 257 → **D**

Zeri e polo: -3, -2 (numeratore) e 2 (denominatore, escluso). Studio dei segni: per x < -3 l'espressione e' negativa; in x = -3 e x = -2 vale 0 (accettabile per >=); fra -3 e -2 e' positiva ma non contiene interi; fra -2 e 2 e' negativa; per x > 2 e' positiva. Interi minori di 5 che soddisfano: -3, -2, 3, 4, quindi 4 in tutto (verificato per enumerazione in Python su x da -20 a 4).

<sub>confidenza: alta · fase: tarata</sub>

### 258 → **D**

Conteggi: aria condizionata 90, veranda 75, piscina 45, somma dei singoli = 210. Case con almeno una dotazione = 150 - 5 = 145, con e1+e2+e3 = 145 ed e3 = 5, quindi e1 + e2 = 140. La somma dei singoli conta una volta chi ne ha una, due volte chi ne ha due, tre volte chi ne ha tre: e1 + 2e2 + 3(5) = 210, cioe' e1 + 2e2 = 195. Sottraendo e1 + e2 = 140 si ottiene e2 = 55.

<sub>confidenza: alta · fase: tarata</sub>

### 259 → **C**

Esprimo tutto in unita' di 2^-17: 2^-14 = 8 x 2^-17, 2^-15 = 4 x 2^-17, 2^-16 = 2 x 2^-17, 2^-17 = 1 x 2^-17. La somma vale 15 x 2^-17; divisa per 5 da' 3 x 2^-17. Quindi il valore e' 3 volte 2^-17 (confermato con frazioni esatte in Python).

<sub>confidenza: alta · fase: tarata</sub>

### 260 → **E**

Una frazione ridotta ha sviluppo decimale finito se e solo se il denominatore ha solo fattori 2 e 5. A: 189 = 3^3 x 7, no. B: 196 = 2^2 x 7^2 (il 7 resta), no. C: 225 = 3^2 x 5^2 (il 3 resta), no. D: 144 = 2^4 x 3^2 (il 3 resta), no. E: 128 = 2^7 e 39 e' dispari non riducibile, quindi 39/128 = 0,3046875, finito.

<sub>confidenza: alta · fase: tarata</sub>

### 261 → **D**

Il primo membro e' 1/(5^m x 4^18) = 1/(5^m x 2^36). Il secondo e' 1/(2 x 10^35) = 1/(2 x 2^35 x 5^35) = 1/(2^36 x 5^35). Uguagliando le potenze di 5 con quelle di 2 gia' coincidenti (36 = 36), si ha m = 35. Verificato con frazioni esatte in Python: (1/5)^35 (1/4)^18 = 1/(2 x 10^35).

<sub>confidenza: alta · fase: tarata</sub>

### 262 → **D**

Casi totali: C(8,4) = 70. Casi favorevoli: Andrew dentro e Karen fuori, quindi restano 3 posti da riempire con i 6 volontari rimanenti: C(6,3) = 20. Probabilita' = 20/70 = 2/7. (Controllo alternativo: 4/8 x 4/7 = 2/7 per simmetria posizionale, coerente.)

<sub>confidenza: alta · fase: tarata</sub>

### 263 → **C**

Il testo del libro riporta 6 1/18 dollari per azione (nell'originale GMAT e' 6 1/8): risolvo con entrambi e la risposta non cambia. Con 6+1/18: costo di acquisto 605,56 piu' 2% di commissione = 617,67; ricavo di vendita 2400 meno 2% = 2352; guadagno 1734,33, cioe' 280,8% del capitale investito. Con 6+1/8: costo 612,50 x 1,02 = 624,75, ricavo netto 2352, guadagno 1727,25, cioe' 276,5%. In entrambi i casi il valore piu' vicino fra le opzioni e' 280%. Attenzione applicata: le commissioni vanno aggiunte al costo e sottratte al ricavo, e la percentuale va calcolata sul costo totale effettivo.

<sub>confidenza: alta · fase: tarata</sub>

### 264 → **D**

Il massimo esponente di 5 in 150! si ottiene con la formula di Legendre: floor(150/5) + floor(150/25) + floor(150/125) = 30 + 6 + 1 = 37 (floor(150/625) = 0). Il distrattore 30 e' chi si ferma al primo termine, 36 chi dimentica il contributo di 125.

<sub>confidenza: alta · fase: tarata</sub>

### 265 → **D**

Domanda I/II/III su media contro mediana: ricalcolo entrambe da zero riordinando la lista per ogni valore. Con 3: lista ordinata 3,4,6,7,9,10, somma 39, media 6,5; mediana (6+7)/2 = 6,5, uguali. Con 7: 4,6,7,7,9,10, somma 43, media 7,1667; mediana (7+7)/2 = 7, diverse. Con 12: 4,6,7,9,10,12, somma 48, media 8; mediana (7+9)/2 = 8, uguali. Quindi I e III.

<sub>confidenza: alta · fase: tarata</sub>

### 266 → **E**

Il markup e' il 40% del PREZZO DI VENDITA, non del costo: S = 150 + 0,40S, quindi 0,60S = 150 e S = 250. Il profitto lordo e' 250 - 150 = 100. Il distrattore B (60 dollari) e' il 40% applicato al costo di 150; questo e' esattamente il tipo di trappola sulla base di calcolo su cui la taratura invita a rallentare.

<sub>confidenza: alta · fase: tarata</sub>

### 267 → **C**

I quadrati compresi strettamente fra 10 e 1000 vanno da 4^2 = 16 a 31^2 = 961 (32^2 = 1024 e' fuori, 3^2 = 9 e' sotto 10). Un quadrato e' dispari solo se la base e' dispari: basi dispari da 5 a 31, cioe' 5,7,9,...,31, in numero di (31-5)/2 + 1 = 14. Enumerazione in Python: 25,49,81,121,169,225,289,361,441,529,625,729,841,961, appunto 14.

<sub>confidenza: alta · fase: tarata</sub>

### 268 → **A**

Bilancio del grasso: 0,01x + 0,02y + 0,03z = 0,015(x+y+z). Moltiplico per 100: x + 2y + 3z = 1,5x + 1,5y + 1,5z. Porto a sinistra: 0,5y + 1,5z = 0,5x, quindi x = y + 3z. Controprova numerica: y = 1, z = 1 da' x = 4; grasso totale 4(0,01)+1(0,02)+1(0,03) = 0,09 su 6 galloni = 1,5%.

<sub>confidenza: alta · fase: tarata</sub>

### 269 → **D**

Uso il complemento: selezioni totali di 4 libri su 8 = C(8,4) = 70; selezioni senza alcun tascabile, cioe' 4 fra i 6 rilegati = C(6,4) = 15. Almeno un tascabile = 70 - 15 = 55. (Controllo diretto: esattamente 1 tascabile C(2,1)C(6,3) = 2x20 = 40, esattamente 2 tascabili C(2,2)C(6,2) = 15, totale 55.)

<sub>confidenza: alta · fase: tarata</sub>

### 270 → **E**

M = 4^(1/2) + 4^(1/3) + 4^(1/4) = 2 + 1,5874 + 1,4142 = 5,0016 (calcolato in Python). E' maggiore di 4. Anche solo stimando: il primo termine da' gia' 2 e gli altri due sono entrambi maggiori di 1, quindi M > 4 senza bisogno di precisione.

<sub>confidenza: alta · fase: tarata</sub>

### 271 → **D**

Con incremento costante x, l'altezza a fine anno n e' 4 + nx. La condizione '1/5 piu' alto' e' una variazione relativa: 4 + 6x = (6/5)(4 + 4x). Moltiplicando per 5: 20 + 30x = 24 + 24x, quindi 6x = 4 e x = 2/3. Verifica: h4 = 4 + 8/3 = 20/3, h6 = 4 + 4 = 8, e 8/(20/3) = 1,2 = 1 + 1/5. Ho applicato l'accortezza sulle formulazioni 'taller by 1/5' interpretandole come variazione relativa rispetto al valore di riferimento (anno 4).

<sub>confidenza: alta · fase: tarata</sub>

### 272 → **A**

13 note in progressione geometrica di ragione r: la 13a frequenza e' 440 r^12 = 2 x 440, quindi r^12 = 2 e r = 2^(1/12). La settima nota e' la sesta dopo la prima: 440 r^6 = 440 x 2^(6/12) = 440 x 2^(1/2) = 440 radice di 2 (circa 622,25). Attenzione al conteggio degli intervalli, che e' la trappola: 440 x 2^(7/12) (opzione D) sarebbe l'ottava nota, non la settima.

<sub>confidenza: alta · fase: tarata</sub>
