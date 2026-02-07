"""Basic package metadata tests."""

import circpacker


def test_package_exposes_version() -> None:
    """The package publishes a non-empty version string."""

    assert isinstance(circpacker.__version__, str)
    assert circpacker.__version__
