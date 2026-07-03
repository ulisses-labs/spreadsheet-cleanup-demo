# Client Case Study: Lead Spreadsheet Cleanup

## Problem

Small businesses often receive lead spreadsheets from different sources such as websites, forms, social media, manual entries, and CRM exports.

These spreadsheets may contain:

- duplicated contacts;
- invalid emails;
- missing required fields;
- inconsistent names;
- inconsistent phone formats;
- inconsistent cities;
- inconsistent lead sources.

This creates manual review work and increases the risk of importing bad data into another system.

## Solution

This demo shows a small cleanup workflow that:

- reads a messy CSV file;
- validates required fields;
- normalizes names, emails, phones, cities, and lead sources;
- removes duplicated leads by email;
- separates invalid records;
- generates a clean CSV file;
- generates a simple Markdown report.

## Delivered Files

The delivery includes:

- clean CSV with valid leads;
- invalid-records CSV for review;
- cleanup report;
- documented source code;
- instructions to run the workflow;
- validation steps.

## Business Value

This type of automation helps:

- reduce manual spreadsheet cleanup;
- make lead review more reliable;
- document what changed;
- avoid importing invalid records;
- create a repeatable cleanup process;
- make acceptance criteria clear.

## How To Validate

A client can validate the result by:

1. reviewing the input CSV;
2. running the cleanup command;
3. checking the clean output;
4. reviewing invalid records;
5. reading the cleanup report;
6. confirming duplicate and invalid rows were handled as expected.

## What This Demo Proves

This demo proves the ability to deliver a small, focused, documented automation for spreadsheet cleanup.

It is not a full CRM, SaaS, dashboard, or data platform.
