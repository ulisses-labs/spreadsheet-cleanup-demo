from lead_cleanup.normalizer import LeadNormalizer
from lead_cleanup.service import LeadCleanupService
from lead_cleanup.validator import LeadValidator


def test_normalize_email() -> None:
    normalizer = LeadNormalizer()

    assert normalizer.email(" MARIA@EMAIL.COM ") == "maria@email.com"


def test_normalize_phone() -> None:
    normalizer = LeadNormalizer()

    assert normalizer.phone("(11) 99999-8888") == "11999998888"


def test_normalize_name() -> None:
    normalizer = LeadNormalizer()

    assert normalizer.name("  maria   silva ") == "Maria Silva"


def test_detect_invalid_email() -> None:
    validator = LeadValidator()

    assert validator.is_valid_email("maria@example.com")
    assert not validator.is_valid_email("maria.example.com")


def test_deduplicate_by_email() -> None:
    rows = [
        {
            "lead_id": "1",
            "name": "Maria Silva",
            "email": "maria@example.com",
            "phone": "(11) 99999-8888",
            "city": "sao paulo",
            "source": "insta",
            "created_at": "2026-01-01",
        },
        {
            "lead_id": "2",
            "name": "Maria Silva",
            "email": " MARIA@EXAMPLE.COM ",
            "phone": "11 99999 8888",
            "city": "Sao Paulo",
            "source": "instagram",
            "created_at": "2026-01-02",
        },
    ]

    result = LeadCleanupService().clean(rows)

    assert len(result.clean_rows) == 1
    assert len(result.invalid_rows) == 0
    assert result.metrics["duplicate_rows_removed"] == 1
