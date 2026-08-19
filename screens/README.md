# Screenshot del libro

Qui vanno le scansioni delle pagine del *GMAT™ Official Guide 2025–2026* usate come
sorgente per la trascrizione in Markdown. Servono a due cose: verificare che il testo
trascritto sia fedele, e permettere a chi riprende il lavoro di controllare senza avere
il libro sottomano.

## ⚠️ Limite tecnico da conoscere

**Le immagini incollate in chat non arrivano al filesystem.** Quando mandi uno screenshot
nella conversazione, io lo *vedo* e lo posso trascrivere, ma non ho modo di scriverne i
byte su disco: non è un file, è contenuto del messaggio. Quindi non posso salvarlo qui da
solo.

Per archiviarle davvero servono i file veri. Due modi:

1. **Allegarli come file** alla sessione (non incollati nel messaggio), e chiedermi di
   spostarli qui.
2. **Metterli tu** in questa cartella e fare commit — è la via più diretta.

Finché non arrivano i file, il registro qui sotto tiene traccia di **cosa è stato
ricevuto e trascritto**, così almeno l'informazione non si perde.

## Come nominare i file

```
screens/chNN/NN-SS_pPPP.png
```

- `NN` = numero del capitolo, due cifre (`01`, `03`)
- `SS` = numero della sezione (`00` per l'introduzione del capitolo)
- `PPP` = numero di pagina del libro, se lo conosci; altrimenti un progressivo

Esempi: `screens/ch03/03-00_p105.png`, `screens/ch01/01-03_p012.png`.

Una pagina che copre due sezioni si nomina con la prima: `03-01_p110.png`.

## Registro delle pagine ricevute

| Capitolo | Sezioni | Pagine ricevute | Trascritto in | File su disco |
|:---|:---|:---:|:---|:---:|
| Indice generale | TOC completa 1.0–9.0 + appendici | 2 | `README.md` (indice del libro) | ❌ non pervenuto |
| 1 | 1.0 → 1.9 (capitolo completo) | 7 | `book/ch01.md` | ❌ non pervenuto |
| 3 | 3.0 (introduzione) | 1 | `book/ch03.md` | ❌ non pervenuto |
| 3 | 3.1 (completa, §1 → §5) | 7 | `book/ch03.md` — ✅ verificata contro le foto | ❌ non pervenuto |

Aggiorna questa tabella ogni volta che arrivano pagine nuove.
