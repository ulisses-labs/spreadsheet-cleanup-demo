"""Shared data structures for the cleanup workflow."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


LeadRow = dict[str, str]


@dataclass(frozen=True)
class CleanupConfig:
    """Input and output paths used by the cleanup workflow."""

    input_path: Path
    clean_output_path: Path
    invalid_output_path: Path
    report_path: Path


@dataclass(frozen=True)
class CleanupResult:
    """Cleaned rows, invalid rows, and summary metrics."""

    clean_rows: list[LeadRow]
    invalid_rows: list[LeadRow]
    metrics: dict[str, int]
