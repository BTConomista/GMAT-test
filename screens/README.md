# Scansioni del libro

Le pagine del *GMAT™ Official Guide 2025–2026* da cui è tratta la trascrizione in
`book/`. Servono a due cose: verificare che il testo trascritto sia fedele, e permettere a
chi riprende il lavoro di controllare senza avere il libro sottomano.

## Come sono organizzate

```
screens/
  ch01/            7 pagine    capitolo 1 completo
  ch02/            8 pagine    capitolo 2 completo
  ch03/
    3.0-3.1/       9 pagine
    3.2/          17 pagine
    3.3/          10 pagine
    3.4/          13 pagine
    3.5/          10 pagine
  ch04/           29 pagine    solo le domande 50-165
```

Il nome di ogni file segue questo schema:

```
NNN_sezioni_descrizione.ext
    │      │        └── di cosa parla la pagina
    │      └─────────── sezione o sezioni che tocca
    └────────────────── posizione nell'ordine di lettura del libro, 001-074
```

Esempio: `049_3.3.5-3.3.6_Tabelle-percentuali_Problemi-di-lavoro.jpeg` è la 49ª pagina, e
copre la fine di 3.3.5 e l'inizio di 3.3.6.

**Il capitolo 4 fa eccezione.** Le sue pagine sono arrivate in momenti diversi e le prime non
sono mai state archiviate, quindi la loro posizione nella sequenza globale non è stabilibile.
Lì il prefisso è `qNNN` e indica la **prima domanda della pagina**: `q074_4.2_Q74-76_...`
comincia dalla domanda 74. Fa lo stesso lavoro — un buco si vede come un salto nei numeri di
domanda — senza fingere una posizione nel libro che non conosciamo.

**Il numero progressivo è la cosa che conta di più:** è continuo su tutto il libro,
attraverso i capitoli, quindi una pagina mancante si vede subito come un buco nella
sequenza.

**Attenzione a un'insidia dei nomi:** quando una pagina copre tre sezioni, il nome cita
solo la prima e l'ultima. `004_1.4-1.6` contiene anche **1.5**, e `009_2.1-2.3` contiene
anche **2.2**. Leggendo solo i nomi sembrano buchi, ma non lo sono — verificato aprendo le
due pagine. Non dare per scontato che le sezioni non citate manchino.

## Stato della copertura

| Capitolo | Pagine | Copertura | Trascritto in | Verificato |
|:---|:---:|:---|:---|:---|
| 1 | 001–007 | completa, 1.0 → 1.9 | `book/ch01.md` | ⬜ |
| 2 | 008–015 | completa, 2.0 → 2.6 | `book/ch02.md` | ⬜ |
| 3 — 3.0/3.1 | 016–024 | completa | `book/ch03.md` | ✅ |
| 3 — 3.2 | 025–041 | completa | `book/ch03.md` | ✅ |
| 3 — 3.3 | 042–051 | completa | `book/ch03.md` | ✅ |
| 3 — 3.4 | 052–064 | completa | `book/ch03.md` | ⬜ |
| 3 — 3.5 | 065–074 | completa | `book/ch03.md` | ✅ |
| 4 | q050–q162 | **parziale**: dalla domanda 50 in poi | `book/ch04.md` | 🔄 in corso |

Le verifiche già fatte sono descritte in [CONVENZIONI.md](../CONVENZIONI.md) §8.

**Del capitolo 4 mancano le prime pagine.** Ci sono le 13 pagine che coprono le domande
50–102, ma non quelle di 4.0, 4.1, delle istruzioni di 4.2 e delle domande 1–49: quelle sono
arrivate come immagini incollate in chat, che non raggiungono il filesystem. Quella parte di
`book/ch04.md` resta quindi non verificabile contro una fonte su disco.

**La domanda 165 è tagliata.** L'ultima pagina ricevuta ne mostra l'enunciato e la sola
opzione A: le altre quattro sono fuori inquadratura. Non è stata trascritta — una domanda con
una risposta su cinque inganna più di una domanda assente. Serve la pagina successiva, che
conterrebbe anche le domande dalla 166 alla 176.

## Aggiungere pagine nuove

Mantieni lo schema di nomi: se le pagine nuove proseguono il libro, continua la
numerazione da 075 in avanti. Poi aggiorna la tabella qui sopra.
