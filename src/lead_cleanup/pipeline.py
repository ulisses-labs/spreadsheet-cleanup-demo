"""Workflow orchestration for the spreadsheet cleanup use case."""

from __future__ import annotations

import logging

from lead_cleanup.csv_repository import CsvLeadRepository
from lead_cleanup.models import CleanupConfig, CleanupResult
from lead_cleanup.report_writer import MarkdownCleanupReportWriter
from lead_cleanup.service import LeadCleanupService


class SpreadsheetCleanupPipeline:
    """Coordinate CSV input, cleanup rules, CSV output, and report generation."""

    def __init__(
        self,
        config: CleanupConfig,
        repository: CsvLeadRepository | None = None,
        service: LeadCleanupService | None = None,
        report_writer: MarkdownCleanupReportWriter | None = None,
    ) -> None:
        self.config = config
        self.repository = repository or CsvLeadRepository()
        self.service = service or LeadCleanupService()
        self.report_writer = report_writer or MarkdownCleanupReportWriter()

    def run(self) -> CleanupResult:
        """Run the full spreadsheet cleanup workflow."""
        logging.info("Reading input CSV from %s", self.config.input_path)
        rows = self.repository.read(self.config.input_path)
        result = self.service.clean(rows)

        self.repository.write(self.config.clean_output_path, result.clean_rows)
        self.repository.write(self.config.invalid_output_path, result.invalid_rows)
        self.report_writer.write(
            self.config.report_path,
            self.config.clean_output_path,
            self.config.invalid_output_path,
            result,
        )

        logging.info("Clean rows saved to %s", self.config.clean_output_path)
        logging.info("Invalid rows saved to %s", self.config.invalid_output_path)
        logging.info("Report saved to %s", self.config.report_path)
        return result
