"""Application service that applies lead cleanup business rules."""

from __future__ import annotations

from lead_cleanup.models import CleanupResult, LeadRow
from lead_cleanup.normalizer import LeadNormalizer
from lead_cleanup.schema import REQUIRED_COLUMNS
from lead_cleanup.validator import LeadValidator


class LeadCleanupService:
    """Clean, validate, and deduplicate lead records."""

    def __init__(
        self,
        normalizer: LeadNormalizer | None = None,
        validator: LeadValidator | None = None,
    ) -> None:
        self.normalizer = normalizer or LeadNormalizer()
        self.validator = validator or LeadValidator()

    def clean(self, rows: list[LeadRow]) -> CleanupResult:
        """Return clean rows, invalid rows, and cleanup metrics."""
        input_rows = len(rows)
        non_empty_rows = [row for row in rows if not self._is_empty_row(row)]
        empty_rows_removed = input_rows - len(non_empty_rows)

        original_emails = [row.get("email", "") for row in non_empty_rows]
        original_phones = [row.get("phone", "") for row in non_empty_rows]
        original_cities = [row.get("city", "") for row in non_empty_rows]
        original_sources = [row.get("source", "") for row in non_empty_rows]

        normalized_rows = [self._normalize_row(row) for row in non_empty_rows]
        invalid_rows = [row for row in normalized_rows if not self.validator.is_valid_lead(row)]
        valid_rows = [row for row in normalized_rows if self.validator.is_valid_lead(row)]
        clean_rows, duplicate_rows_removed = self._deduplicate_by_email(valid_rows)

        metrics = {
            "input_rows": input_rows,
            "empty_rows_removed": empty_rows_removed,
            "valid_rows": len(clean_rows),
            "invalid_rows": len(invalid_rows),
            "duplicate_rows_removed": duplicate_rows_removed,
            "emails_normalized": self._count_changed(
                original_emails,
                [row["email"] for row in normalized_rows],
            ),
            "phones_normalized": self._count_changed(
                original_phones,
                [row["phone"] for row in normalized_rows],
            ),
            "cities_normalized": self._count_changed(
                original_cities,
                [row["city"] for row in normalized_rows],
            ),
            "sources_normalized": self._count_changed(
                original_sources,
                [row["source"] for row in normalized_rows],
            ),
            "empty_phones": sum(1 for row in normalized_rows if row["phone"] == ""),
        }

        return CleanupResult(clean_rows=clean_rows, invalid_rows=invalid_rows, metrics=metrics)

    def _normalize_row(self, row: LeadRow) -> LeadRow:
        return {
            "lead_id": self.normalizer.squeeze_spaces(row.get("lead_id", "")),
            "name": self.normalizer.name(row.get("name", "")),
            "email": self.normalizer.email(row.get("email", "")),
            "phone": self.normalizer.phone(row.get("phone", "")),
            "city": self.normalizer.city(row.get("city", "")),
            "source": self.normalizer.source(row.get("source", "")),
            "created_at": self.normalizer.squeeze_spaces(row.get("created_at", "")),
        }

    def _is_empty_row(self, row: LeadRow) -> bool:
        return all(
            self.normalizer.squeeze_spaces(row.get(column, "")) == ""
            for column in REQUIRED_COLUMNS
        )

    def _deduplicate_by_email(self, rows: list[LeadRow]) -> tuple[list[LeadRow], int]:
        clean_rows: list[LeadRow] = []
        seen_emails: set[str] = set()
        duplicates = 0

        for row in rows:
            if row["email"] in seen_emails:
                duplicates += 1
                continue
            clean_rows.append(row)
            seen_emails.add(row["email"])

        return clean_rows, duplicates

    def _count_changed(self, before: list[str], after: list[str]) -> int:
        return sum(1 for old, new in zip(before, after, strict=True) if old.strip() and old != new)
