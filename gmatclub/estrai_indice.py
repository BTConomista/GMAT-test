#!/usr/bin/env python3
"""Ricostruisce l'indice delle domande del GMAT Official Guide 2025-2026.

La fonte sono i quattro error log che GMAT Club pubblica come fogli Google, discussi
in https://gmatclub.com/forum/error-log-for-gmat-official-guide-445984.html

Dal foglio principale si prendono due cose che nel repo non abbiamo:

  - l'indice del libro (numero di domanda, difficolta', concetto, pagina della domanda,
    pagina della spiegazione) - le stesse colonne del capitolo 9 del libro;
  - i dati di GMAT Club sulla singola domanda (risposta esatta, difficolta' reale
    misurata sugli utenti, percentile, categoria).

Uso:  python3 gmatclub/estrai_indice.py
Serve openpyxl.  Scrive gmatclub/og-2025-2026.csv e gmatclub/og-2025-2026-online.csv
"""

import csv
import io
import os
import urllib.request

import openpyxl

FOGLIO = "1DT4ddI7x3HeRkIG_DwRDz0Z5mghd87cTZL_Z9-DjCrY"
URL = f"https://docs.google.com/spreadsheets/d/{FOGLIO}/export?format=xlsx"

QUI = os.path.dirname(os.path.abspath(__file__))

# Le sette schede per tipo di domanda. Per ognuna: da quale colonna leggere
# numero, id, difficolta', percentile, risposta esatta e categoria.
# Gli header non sono uniformi fra le schede, quindi le colonne si indicano a mano.
SCHEDE = {
    #          num  id  diff  perc   oa  cat  passage
    "PS":  dict(num=0, id=1, diff=3, perc=4, oa=5, cat=6),
    "DS":  dict(num=0, id=1, diff=3, perc=4, oa=5, cat=6),
    "TPA": dict(num=0, id=1, diff=3, perc=4, oa=5, cat=6),
    "RC":  dict(num=1, id=2, diff=4, perc=5, oa=6, cat=7, passage=0),
    "CR":  dict(num=0, id=1, diff=3, perc=4, oa=5, cat=6),
    "G&T": dict(num=0, id=2, diff=4, perc=5, oa=7, cat=6, tipo=1),
    "MSR": dict(num=0, id=1, diff=3, perc=4, oa=6, cat=5),
}


def scarica():
    """Scarica il foglio come xlsx. Restituisce il workbook."""
    with urllib.request.urlopen(URL, timeout=120) as r:
        dati = r.read()
    return openpyxl.load_workbook(io.BytesIO(dati), data_only=True)


def righe(ws, marcatore=("Question", "Passage")):
    """Le righe di una scheda, saltando titoli e intestazioni.

    Le schede si aprono con una o due righe di titolo prima dell'intestazione vera,
    e non tutte con lo stesso numero: l'intestazione si cerca, non si conta.
    """
    tutte = list(ws.iter_rows(values_only=True))
    for i, r in enumerate(tutte):
        if r and any(c and str(c).strip().startswith(marcatore) for c in r[:3]):
            return tutte[i + 1:]
    raise SystemExit(f"intestazione non trovata in '{ws.title}'")


def intero(v):
    return int(v) if v is not None and str(v).strip() != "" else None


def testo(v):
    return str(v).strip() if v is not None and str(v).strip() != "" else ""


def leggi_schede(wb):
    """Numero di domanda -> dati di GMAT Club, da tutte e sette le schede."""
    out = {}
    passaggio = None  # nella scheda RC l'id del brano e' scritto solo sulla prima domanda
    for nome, col in SCHEDE.items():
        for r in righe(wb[nome]):
            n = intero(r[col["num"]])
            if n is None:
                continue
            if "passage" in col:
                p = intero(r[col["passage"]])
                if p is not None:
                    passaggio = p
            out[n] = {
                "section": nome,
                "passage": passaggio if "passage" in col else None,
                "type": testo(r[col["tipo"]]) if "tipo" in col else "",
                "gmatclub_id": intero(r[col["id"]]),
                "gmatclub_difficulty": testo(r[col["diff"]]),
                "gmatclub_percentile": r[col["perc"]],
                "oa": testo(r[col["oa"]]),
                "gmatclub_category": testo(r[col["cat"]]),
            }
    return out


def leggi_indice(wb):
    """Numero di domanda -> dati dell'indice del libro (capitolo 9)."""
    out = {}
    for r in righe(wb["OG 2025-2026 Index"], marcatore="Difficulty"):
        n = intero(r[3])
        if n is None:
            continue
        out[n] = {
            "book_difficulty": testo(r[0]),
            "book_type": testo(r[1]),
            "book_concept": testo(r[2]),
            "page": intero(r[6]),
            "explanation_page": intero(r[7]),
        }
    return out


COLONNE = [
    "question", "section", "passage", "book_difficulty", "book_concept",
    "page", "explanation_page", "oa", "gmatclub_id", "gmatclub_difficulty",
    "gmatclub_percentile", "gmatclub_category",
]

COLONNE_ONLINE = [
    "question", "section", "type", "oa", "gmatclub_id",
    "gmatclub_difficulty", "gmatclub_percentile", "gmatclub_category",
]


def scrivi(percorso, colonne, righe_dati):
    with open(percorso, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=colonne, extrasaction="ignore")
        w.writeheader()
        for r in righe_dati:
            w.writerow(r)


def main():
    wb = scarica()
    schede = leggi_schede(wb)
    indice = leggi_indice(wb)

    stampate, online = [], []
    for n in sorted(schede):
        r = {"question": n, **schede[n]}
        if n in indice:
            r.update(indice[n])
            if r["book_type"] and r["book_type"] != r["section"]:
                raise SystemExit(f"Q{n}: indice dice {r['book_type']}, scheda {r['section']}")
            stampate.append(r)
        else:
            online.append(r)

    mancanti = sorted(set(indice) - set(schede))
    if mancanti:
        raise SystemExit(f"domande nell'indice senza scheda: {mancanti[:10]}")

    scrivi(os.path.join(QUI, "og-2025-2026.csv"), COLONNE, stampate)
    scrivi(os.path.join(QUI, "og-2025-2026-online.csv"), COLONNE_ONLINE, online)
    print(f"{len(stampate)} domande stampate -> og-2025-2026.csv")
    print(f"{len(online)} domande solo online -> og-2025-2026-online.csv")


if __name__ == "__main__":
    main()
