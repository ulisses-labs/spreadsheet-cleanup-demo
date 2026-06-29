# Spreadsheet Cleanup Demo

## Overview

This demo shows how a messy lead spreadsheet can be cleaned, deduplicated, normalized, and documented with a simple Python workflow.

It is intentionally small: one CSV input, one Python script, one clean CSV output, one invalid-records CSV, and one Markdown report.

## Problem

Lead spreadsheets often arrive with inconsistent formatting, duplicate contacts, missing required fields, and values that are hard to review reliably. Even a simple file can become risky when names, emails, phone numbers, cities, and lead sources are written in many different ways.

## Solution

The command in `src/cleanup.py` runs a small object-oriented cleanup pipeline. The code separates CSV persistence, business rules, validation, normalization, and report generation so the workflow stays easy to maintain.

## Before and After

Before:

| name | email | phone | city | source |
| --- | --- | --- | --- | --- |
| `  maria   silva ` | ` MARIA@EMAIL.COM ` | `(11) 99999-8888` | `sao paulo` | `insta` |
| `JOAO santos` | `joao@email.com` | `11 98888 7777` | `RIO DE JANEIRO` | `site` |
| `Ana Costa` | `ANA.COSTA@EMAIL.COM` | `+55 (31) 97777-6666` | ` belo horizonte ` | `indicacao` |

After:

| name | email | phone | city | source |
| --- | --- | --- | --- | --- |
| `Maria Silva` | `maria@email.com` | `11999998888` | `Sao Paulo` | `Instagram` |
| `Joao Santos` | `joao@email.com` | `11988887777` | `Rio De Janeiro` | `Website` |
| `Ana Costa` | `ana.costa@email.com` | `5531977776666` | `Belo Horizonte` | `Referral` |

## Features

- Validates the input file and required columns.
- Removes fully empty rows.
- Trims extra spaces from fields.
- Normalizes names, emails, phones, cities, and lead sources.
- Detects missing names, missing emails, and invalid email formats.
- Keeps empty phones allowed while reporting how many were found.
- Removes duplicate leads by normalized email.
- Exports clean and invalid records separately.
- Generates a Markdown cleanup report.

## Project Structure

```text
spreadsheet-cleanup-demo/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   ├── input/
│   │   └── leads_raw.csv
│   └── output/
├── reports/
│   └── cleanup_report.md
├── src/
│   ├── cleanup.py
│   └── lead_cleanup/
│       ├── __init__.py
│       ├── csv_repository.py
│       ├── models.py
│       ├── normalizer.py
│       ├── pipeline.py
│       ├── report_writer.py
│       ├── schema.py
│       ├── service.py
│       └── validator.py
└── tests/
    └── test_cleanup.py
```

## How to Run

Create and activate a virtual environment on Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If `python3 -m venv .venv` fails on Debian/Ubuntu with an `ensurepip is not available` message, install the system venv package first:

```bash
sudo apt install python3-venv
```

For Python 3.14 specifically, the package may be:

```bash
sudo apt install python3.14-venv
```

Then recreate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run with the default paths:

```bash
python3 src/cleanup.py
```

Or pass explicit paths:

```bash
python3 src/cleanup.py \
  --input data/input/leads_raw.csv \
  --output data/output/leads_clean.csv \
  --invalid data/output/leads_invalid.csv \
  --report reports/cleanup_report.md
```

Run the tests:

```bash
python3 -m pytest
```

## Example Input

```csv
lead_id,name,email,phone,city,source,created_at
1,  maria   silva , MARIA@EMAIL.COM ,(11) 99999-8888,sao paulo,insta,2026-01-03
2,JOAO santos,joao@email.com,11 98888 7777,RIO DE JANEIRO,site,2026-01-04
3,Ana Costa,ANA.COSTA@EMAIL.COM,+55 (31) 97777-6666, belo horizonte ,indicacao,2026-01-05
```

## Example Output

```csv
lead_id,name,email,phone,city,source,created_at
1,Maria Silva,maria@email.com,11999998888,Sao Paulo,Instagram,2026-01-03
2,Joao Santos,joao@email.com,11988887777,Rio De Janeiro,Website,2026-01-04
3,Ana Costa,ana.costa@email.com,5531977776666,Belo Horizonte,Referral,2026-01-05
```

## Cleanup Report

The script writes a report to `reports/cleanup_report.md` with:

- input row count;
- empty rows removed;
- valid and invalid row counts;
- duplicate rows removed;
- normalized email, phone, city, and source counts;
- output file locations;
- notes confirming that the dataset is fictitious.

## Technologies

- Python 3.12
- pytest

## What This Demo Shows

This project demonstrates a practical data cleanup workflow for spreadsheets used in sales, operations, marketing, and back-office processes. It shows the ability to turn messy CSV data into a clean, validated, review-ready dataset with clear documentation.

It also shows a maintainable Python structure:

- `cleanup.py`: command-line entrypoint.
- `pipeline.py`: use-case orchestration.
- `service.py`: cleanup business rules.
- `normalizer.py` and `validator.py`: field-level domain logic.
- `csv_repository.py`: CSV input and output adapter.
- `report_writer.py`: Markdown reporting adapter.

## Future Improvements

- Add configurable source mappings.
- Add richer phone validation by country.
- Export a summary as JSON for automated workflows.
- Add optional column-level quality checks.

## License

This project is licensed under the MIT License.
