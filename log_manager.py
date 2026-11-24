import csv
from pathlib import Path

FIELDS = [
    "date", "project", "location", "supplier", "mix_id", "strength", "ticket",
    "batch_time", "arrival_time", "discharge_start", "discharge_end",
    "quantity_yd3", "slump_in", "concrete_temp_f", "air_content_pct",
    "weather", "ambient_temp_f", "placement_method", "crew", "samples", "notes"
]

class PourLogManager:
    def __init__(self, filename="pouring_log.csv"):
        self.filename = Path(filename)

    def save(self, entry):
        new_file = not self.filename.exists()
        with self.filename.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            if new_file:
                writer.writeheader()
            writer.writerow({field: entry.get(field, "") for field in FIELDS})
