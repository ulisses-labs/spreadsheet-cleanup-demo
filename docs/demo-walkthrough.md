# Demo Walkthrough

## What This Demo Shows

This demo shows how a messy lead spreadsheet can be transformed into clean, validated, review-ready CSV files with a simple Python workflow.

It is designed for a quick portfolio or client review: what goes in, what the script does, what comes out, and how the result can be checked.

## 1. Messy Input

The input file is `data/input/leads_raw.csv`.

It represents a typical lead spreadsheet with common cleanup issues:

- extra spaces;
- duplicated emails;
- inconsistent capitalization;
- invalid emails;
- missing required fields;
- different phone formats;
- inconsistent lead sources.

## 2. Cleanup Workflow

The script runs a simple cleanup workflow:

- read the CSV;
- normalize fields;
- validate required data;
- remove duplicates;
- separate invalid records;
- write clean output;
- generate a Markdown report.

## 3. Clean Output

The clean, review-ready rows are written to `data/output/leads_clean.csv`.

This file keeps valid leads after formatting, validation, and duplicate removal.

## 4. Invalid Records

Rows that cannot be accepted are written to `data/output/leads_invalid.csv`.

This makes the rejected records easy to review without mixing them with the clean output.

## 5. Cleanup Report

The report is written to `reports/cleanup_report.md`.

It summarizes the cleanup result, including row counts, invalid records, duplicate removal, normalized fields, output locations, and dataset notes.

## 6. How to Validate the Result

1. Open the raw CSV: `data/input/leads_raw.csv`.
2. Run `python3 src/cleanup.py`.
3. Compare `data/output/leads_clean.csv` and `data/output/leads_invalid.csv`.
4. Read `reports/cleanup_report.md`.
5. Check duplicated emails and invalid rows.

## Why This Matters for a Client

This kind of workflow helps reduce manual cleanup, avoid common import errors, and make review criteria clear before data is sent to another system.

It also creates a documented delivery: clean records, invalid records, and a report that explains what happened.

## What This Is Not

This demo is:

- not a SaaS;
- not a dashboard;
- not a CRM;
- not a full data platform;
- not using real data.

It is a small, focused example of a practical spreadsheet cleanup workflow.

## Next Step

This structure can be adapted to real CSV, Excel, Google Sheets exports, CRM imports, or operational spreadsheets after scope validation.
