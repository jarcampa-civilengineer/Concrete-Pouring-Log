from datetime import datetime

def validate_entry(entry):
    errors = []
    try:
        datetime.strptime(entry["date"], "%Y-%m-%d")
    except ValueError:
        errors.append("Date must be in YYYY-MM-DD format.")
    for key, label in [
        ("quantity_yd3", "Quantity"), ("slump_in", "Slump"),
        ("concrete_temp_f", "Concrete temperature"),
        ("air_content_pct", "Air content"), ("ambient_temp_f", "Ambient temperature")
    ]:
        value = entry.get(key, "").strip()
        if value:
            try:
                if float(value) < 0:
                    errors.append(f"{label} cannot be negative.")
            except ValueError:
                errors.append(f"{label} must be numeric.")
    for key, label in (("project", "Project"), ("location", "Pour location")):
        if not entry.get(key, "").strip():
            errors.append(f"{label} is required.")
    return errors
