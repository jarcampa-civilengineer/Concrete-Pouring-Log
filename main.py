import argparse
from validators import validate_entry
from log_manager import PourLogManager
from report_generator import generate_report

def ask(label, required=False):
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print("This field is required.")

def main():
    parser = argparse.ArgumentParser(description="Concrete Pouring Log")
    parser.add_argument("--data", default="pouring_log.csv")
    args = parser.parse_args()
    print("\nCONCRETE POURING LOG")
    entry = {
        "date": ask("Pour date (YYYY-MM-DD)", True),
        "project": ask("Project name", True),
        "location": ask("Pour location / placement ID", True),
        "supplier": ask("Concrete supplier"),
        "mix_id": ask("Mix design / mix ID"),
        "strength": ask("Specified compressive strength (e.g. 4000 psi)"),
        "ticket": ask("Truck ticket number"),
        "batch_time": ask("Batch time"),
        "arrival_time": ask("Arrival time"),
        "discharge_start": ask("Discharge start time"),
        "discharge_end": ask("Discharge end time"),
        "quantity_yd3": ask("Quantity delivered (yd³)"),
        "slump_in": ask("Slump (in.)"),
        "concrete_temp_f": ask("Concrete temperature (°F)"),
        "air_content_pct": ask("Air content (%)"),
        "weather": ask("Weather conditions"),
        "ambient_temp_f": ask("Ambient temperature (°F)"),
        "placement_method": ask("Placement method (pump/chute/bucket)"),
        "crew": ask("Crew / subcontractor"),
        "samples": ask("Test sample / cylinder IDs"),
        "notes": ask("Observations, delays, rejected loads or corrective actions")
    }
    errors = validate_entry(entry)
    if errors:
        print("\nPlease correct:")
        for error in errors:
            print("-", error)
        return
    PourLogManager(args.data).save(entry)
    report = generate_report(entry)
    print(f"\nRecord saved to {args.data}")
    print(f"Individual report: {report}")

if __name__ == "__main__":
    main()
