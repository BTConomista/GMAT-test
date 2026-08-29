# Quanto divergono i due file, e perché

> ⚠️ Vale l'avvertenza in [README.md](README.md): materiale di studio, non una fonte.

## Il numero

**Zero.** Su 267 domande, la prova cieca e la prova tarata danno la **stessa lettera in tutti
i casi**.

| | Prova cieca | Prova tarata |
|:---|:---:|:---:|
| Domande risolte | 267 | 267 |
| Punteggio sulle 29 note | 29/29 | 29/29 |
| Risposte in disaccordo fra i due file | — | **0** |
| Confidenza «alta» | 264 | 265 |
| Confidenza «media» | 3 | 2 |
| Confidenza «bassa» | 0 | 0 |

Anche dentro la prova cieca, dove ogni blocco era risolto due volte da agenti indipendenti,
le discordanze sono state **0 su 267**.

## Cosa questo dimostra, e cosa no

**Dimostra che le risposte sono stabili.** Due procedimenti diversi — uno alla cieca con
doppia risoluzione, uno tarato su 29 risposte note e armato di 28 regole operative — arrivano
allo stesso punto. Non c'è un pezzo del capitolo dove il metodo oscilli.

**Non dimostra che siano giuste.** È la distinzione che conta, e va detta senza attenuazioni:

> I due file non sono osservatori indipendenti. Escono dallo stesso modello, con le stesse
> tendenze e gli stessi punti ciechi. Se una domanda viene fraintesa per una ragione
> strutturale — un'ambiguità letta sempre nello stesso modo, una formula ricordata storta —
> **entrambi la sbagliano allo stesso modo**, e l'accordo fra loro non se ne accorge.

Un accordo del 100% fra due misure correlate non è una conferma: è la stessa misura fatta due
volte. L'unico controllo davvero esterno di cui disponiamo sono le **29 risposte ufficiali del
libro**, ed è lì che il 29/29 acquista valore — non nell'accordo reciproco.

## Perché lo zero, secondo me

Tre ragioni, in ordine di peso.

**1. Le domande sono progettate per avere una risposta netta.** Il GMAT quantitativo è
costruito perché una persona preparata arrivi alla soluzione in circa due minuti, con una sola
opzione corretta e quattro distrattori riconoscibili. Non è un dominio con zone grigie: o il
conto torna su un'opzione, o si è sbagliato qualcosa. Su materiale così, due tentativi
competenti tendono a convergere.

**2. La taratura non aveva errori da correggere.** Il secondo workflow doveva imparare dagli
sbagli sulle prime 29 — e di sbagli non ce n'erano. Le 28 «lezioni» che ne sono uscite sono
quindi le accortezze che hanno *evitato* i distrattori, non correzioni di rotta. Applicarle
alle 238 successive ha confermato risposte già corrette invece di cambiarne. **Il canale
attraverso cui la taratura avrebbe potuto far divergere i due file era chiuso in partenza.**

**3. I conti sono stati fatti eseguire, non ricordati.** A entrambi i gruppi era prescritto di
usare `python3` per fattoriali, potenze, combinatoria e probabilità. Questo elimina proprio la
classe di errori più rumorosa — quelli aritmetici — che è anche la più casuale, cioè quella che
avrebbe prodotto divergenze sparse fra le due esecuzioni. Restano gli errori di
*impostazione*, che sono sistematici: e quelli, per definizione, si ripetono uguali.

## Dove i due file divergono davvero

Non nelle risposte: nel **contenuto**.

- `risposte-ragionate.md` contiene 267 ragionamenti e nient'altro.
- `risposte-tarate.md` contiene gli stessi 267 ragionamenti **più 28 lezioni operative e 12
  tipologie di domanda a rischio**, ricavate guardando da vicino i distrattori delle prime 29.

Quelle 28 lezioni sono la cosa più utile prodotta da tutto l'esercizio, e sono utili
**indipendentemente dal fatto che le risposte siano giuste**: descrivono come è fatta una
trappola del GMAT quantitativo. Per esempio, che nelle commissioni a scaglioni il distrattore è
quasi sempre l'aliquota alta applicata all'intero importo; o che nelle conversioni di unità
composte il reciproco è sempre fra le opzioni.

## Due riserve che è giusto mettere per iscritto

**Il campione di verifica è piccolo e sbilanciato.** Le 29 risposte note sono tutte nella
fascia *Easy* (domande 1–96). Delle 96 *Hard* (177–272), dove stanno combinatoria, probabilità
condizionata e teoria dei numeri, **non conosciamo nemmeno una risposta**. Un 29/29 su un
estremo non si estende all'altro.

| Fascia | Domande | Risposte ufficiali note |
|:---|:---:|:---:|
| Easy (1–96) | 96 | 29 |
| Medium (97–176) | 75 | 0 |
| Hard (177–272) | 96 | 0 |

**La confidenza dichiarata non porta informazione.** Su 267 risposte, 264 e 265 sono marcate
«alta» e nessuna «bassa». Un indicatore che non varia mai non distingue niente: non si può
usarlo per decidere quali risposte guardare per prime. Sulle 29 verificate è risultato
azzeccato, ma proprio per questo non è mai stato messo alla prova.

## Cosa servirebbe per sapere davvero

Il modo per rompere la correlazione è **una fonte esterna**, non un altro tentativo:

1. **Le risposte ufficiali dalla 30 in poi.** Sono nel libro, alle pagine successive a quella
   già trascritta. È il controllo decisivo e costa solo qualche scansione.
2. **La sezione 4.4, «Answer Explanations».** Contiene il procedimento del libro, quindi
   permette di confrontare non solo la lettera ma il *percorso* — e di scoprire i casi in cui
   si arriva alla risposta giusta per la ragione sbagliata, che questo esercizio non può vedere.

Finché mancano, il dato onesto è: **29 verificate, 238 coerenti ma non verificate.**
