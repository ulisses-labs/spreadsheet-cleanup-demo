"""Command-line entrypoint for the spreadsheet cleanup workflow."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from lead_cleanup import CleanupConfig, SpreadsheetCleanupPipeline


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Clean a messy lead spreadsheet.")
    parser.add_argument("--input", default="data/input/leads_raw.csv", type=Path)
    parser.add_argument("--output", default="data/output/leads_clean.csv", type=Path)
    parser.add_argument("--invalid", default="data/output/leads_invalid.csv", type=Path)
    parser.add_argument("--report", default="reports/cleanup_report.md", type=Path)
    return parser.parse_args()


def main() -> None:
    """Run the CLI workflow."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = parse_args()

    config = CleanupConfig(
        input_path=args.input,
        clean_output_path=args.output,
        invalid_output_path=args.invalid,
        report_path=args.report,
    )
    SpreadsheetCleanupPipeline(config).run()


if __name__ == "__main__":
    main()
