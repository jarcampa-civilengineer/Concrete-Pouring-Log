# Concrete Pouring Log

A small command-line Python tool for documenting concrete placement activities.

## Features
- Project, date, placement location, supplier, mix ID and specified strength.
- Truck ticket and batch, arrival and discharge times.
- Delivered volume, slump, concrete temperature and air content.
- Weather, placement method, crew, sample IDs and field notes.
- CSV history, individual text reports and a load/volume summary function.

## Files
- `main.py` — interactive data-entry application.
- `validators.py` — date and numeric input checks.
- `log_manager.py` — appends records to CSV.
- `report_generator.py` — creates a report for each pour entry.
- `summary.py` — summarizes load count and recorded volume.

## Requirements
Python 3.8 or newer. No third-party libraries required.

## Run
```bash
python main.py
```
Optional CSV filename:
```bash
python main.py --data project_A_pours.csv
```
View summary:
```bash
python -c "from summary import summarize_log; print(summarize_log())"
```

## Field-use notes
Enter measurements using the units shown. Record actual test/sample identifiers
and retain batch tickets and testing reports with the project quality records.
This application does not determine acceptance, verify mix-design compliance,
or replace the project's inspection and testing plan. Customize it to approved
submittals, specifications, adopted code and applicable standards (for example,
ASTM C143/C143M for slump and ASTM C1064/C1064M for concrete temperature,
when specified). Follow project document-control requirements.
