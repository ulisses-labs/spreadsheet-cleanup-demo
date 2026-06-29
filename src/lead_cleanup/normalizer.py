"""Field normalization rules for lead rows."""

from __future__ import annotations

import re
from typing import Any


class LeadNormalizer:
    """Normalize raw lead fields into a consistent format."""

    source_map = {
        "google ads": "Google Ads",
        "google": "Google",
        "instagram": "Instagram",
        "insta": "Instagram",
        "site": "Website",
        "website": "Website",
        "referral": "Referral",
        "indicacao": "Referral",
        "indicação": "Referral",
    }

    def squeeze_spaces(self, value: Any) -> str:
        """Return text with leading, trailing, and repeated spaces removed."""
        if value is None:
            return ""
        return " ".join(str(value).strip().split())

    def name(self, value: Any) -> str:
        """Normalize a lead name to simple title case."""
        return self.squeeze_spaces(value).title()

    def email(self, value: Any) -> str:
        """Normalize an email address for validation and deduplication."""
        if value is None:
            return ""
        return str(value).strip().replace(" ", "").lower()

    def phone(self, value: Any) -> str:
        """Normalize a phone number by keeping digits only."""
        if value is None:
            return ""
        return re.sub(r"\D", "", str(value))

    def city(self, value: Any) -> str:
        """Normalize a city name to simple title case."""
        return self.squeeze_spaces(value).title()

    def source(self, value: Any) -> str:
        """Normalize common lead source variations."""
        source = self.squeeze_spaces(value).lower()
        return self.source_map.get(source, source.title() if source else "")
