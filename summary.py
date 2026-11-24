import csv
from pathlib import Path

def summarize_log(filename="pouring_log.csv"):
    path = Path(filename)
    if not path.exists():
        return {"load_count": 0, "total_quantity_yd3": 0.0}
    count, total = 0, 0.0
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            count += 1
            try:
                total += float(row.get("quantity_yd3") or 0)
            except ValueError:
                pass
    return {"load_count": count, "total_quantity_yd3": round(total, 2)}
