from pathlib import Path
from datetime import datetime

LABELS = {
    "date":"Pour date", "project":"Project", "location":"Pour location / placement ID",
    "supplier":"Concrete supplier", "mix_id":"Mix design / ID",
    "strength":"Specified compressive strength", "ticket":"Truck ticket",
    "batch_time":"Batch time", "arrival_time":"Arrival time",
    "discharge_start":"Discharge start", "discharge_end":"Discharge end",
    "quantity_yd3":"Quantity delivered (yd³)", "slump_in":"Slump (in.)",
    "concrete_temp_f":"Concrete temperature (°F)", "air_content_pct":"Air content (%)",
    "weather":"Weather", "ambient_temp_f":"Ambient temperature (°F)",
    "placement_method":"Placement method", "crew":"Crew / subcontractor",
    "samples":"Test sample / cylinder IDs", "notes":"Observations / corrective actions"
}

def generate_report(entry, output_dir="pour_reports"):
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in entry["location"])
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = folder / f"pour_{safe}_{stamp}.txt"
    lines = ["CONCRETE POURING LOG", "=" * 32]
    lines.extend(f"{label}: {entry.get(key) or 'Not recorded'}" for key, label in LABELS.items())
    lines.extend(["", "REVIEW NOTE",
        "Verify field measurements and test results against approved mix submittals,",
        "project specifications, inspection/testing plan and applicable standards.",
        "This log does not establish concrete acceptance."])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
