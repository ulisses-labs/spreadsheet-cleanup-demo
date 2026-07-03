# Buyer FAQ

## What kind of files can this workflow handle?

This demo focuses on CSV files. The same approach can be adapted to Excel files, Google Sheets exports, CRM exports, or other structured spreadsheet formats after scope validation.

## What does the cleanup process do?

It reads a messy lead spreadsheet, validates required fields, normalizes values, removes duplicates, separates invalid records, and generates a cleanup report.

## What counts as a duplicate?

In this demo, duplicated leads are identified by normalized email.

For a real project, the duplicate rule must be confirmed before implementation.

## What happens to invalid rows?

Invalid rows are not mixed with the clean output. They are exported to a separate invalid-records file so they can be reviewed.

## Can this work with real client data?

Yes, but real client data should not be committed to a public repository.

For demos and initial validation, use fictitious, anonymized, or masked data.

## Does this integrate with a CRM?

Not by default.

This demo focuses on cleanup and validation. CRM import or API integration can be treated as a separate scope.

## Does this include a dashboard?

No.

This is a small automation demo, not a dashboard or SaaS product.

## Does this include long-term maintenance?

Not by default.

Bug fixes, revisions, new features, and ongoing maintenance should be defined separately.

## How can I validate the result?

You can validate the result by reviewing:

- the original input file;
- the clean output file;
- the invalid-records file;
- the generated cleanup report;
- the documented rules and limitations.

## What makes this useful?

It turns messy spreadsheet cleanup into a repeatable and documented process, reducing manual review and making the final output easier to trust.
