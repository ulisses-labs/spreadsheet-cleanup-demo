"""CSV persistence adapter for lead rows."""

from __future__ import annotations

import csv
from pathlib import Path

from lead_cleanup.models import LeadRow
from lead_cleanup.schema import REQUIRED_COLUMNS


class CsvLeadRepository:
    """Read and write lead rows using CSV files."""

    def read(self, input_path: Path) -> list[LeadRow]:
        """Read a CSV file and keep blank rows for reporting."""
        self._validate_input_file(input_path)

        with input_path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self._validate_columns(reader.fieldnames or [])
            return [
                {column: row.get(column, "") for column in REQUIRED_COLUMNS}
                for row in reader
            ]

    def write(self, output_path: Path, rows: list[LeadRow]) -> None:
        """Write lead rows to a CSV file."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=REQUIRED_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)

    def _validate_input_file(self, input_path: Path) -> None:
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

    def _validate_columns(self, columns: list[str]) -> None:
        missing = [column for column in REQUIRED_COLUMNS if column not in columns]
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")
