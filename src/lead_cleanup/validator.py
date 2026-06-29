"""Validation rules for lead cleanup."""

from __future__ import annotations

import re

from lead_cleanup.models import LeadRow


class LeadValidator:
    """Validate lead rows after normalization."""

    email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def is_valid_email(self, value: str) -> bool:
        """Return True when an email has a basic valid format."""
        return bool(self.email_pattern.match(value))

    def is_valid_lead(self, row: LeadRow) -> bool:
        """Return True when a normalized lead has required valid fields."""
        return (
            row["name"] != ""
            and row["email"] != ""
            and self.is_valid_email(row["email"])
        )
