"""Smoke tests for package imports."""


def test_import_circpacker_smoke() -> None:
    """Importing top-level package should succeed."""

    import circpacker  # noqa: PLC0415

    assert circpacker.__name__ == "circpacker"
