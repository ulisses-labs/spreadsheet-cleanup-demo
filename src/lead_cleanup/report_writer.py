"""Markdown report adapter for cleanup results."""

from __future__ import annotations

from pathlib import Path

from lead_cleanup.models import CleanupResult


class MarkdownCleanupReportWriter:
    """Write cleanup metrics as a Markdown report."""

    def write(
        self,
        report_path: Path,
        clean_path: Path,
        invalid_path: Path,
        result: CleanupResult,
    ) -> None:
        """Write a Markdown cleanup report."""
        report_path.parent.mkdir(parents=True, exist_ok=True)
        metrics = result.metrics
        report = f"""# Cleanup Report

## Summary

- Input rows: {metrics["input_rows"]}
- Empty rows removed: {metrics["empty_rows_removed"]}
- Valid rows: {metrics["valid_rows"]}
- Invalid rows: {metrics["invalid_rows"]}
- Duplicate rows removed: {metrics["duplicate_rows_removed"]}
- Emails normalized: {metrics["emails_normalized"]}
- Phones normalized: {metrics["phones_normalized"]}
- Cities normalized: {metrics["cities_normalized"]}
- Sources normalized: {metrics["sources_normalized"]}
- Empty phones: {metrics["empty_phones"]}

## Output Files

- Clean data: `{clean_path}`
- Invalid rows: `{invalid_path}`

## Notes

- No real data was used.
- This is a public demo dataset.
- The script is intentionally small and easy to review.
"""
        report_path.write_text(report, encoding="utf-8")
