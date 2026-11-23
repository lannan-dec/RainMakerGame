from pathlib import Path

CONCEPT = Path(__file__).resolve().parent.parent / "docs" / "Rainmaker_The_Campaign.txt"


def test_concept_document_present():
    assert CONCEPT.is_file(), f"missing {CONCEPT}"
    assert CONCEPT.stat().st_size > 0, f"empty {CONCEPT}"
