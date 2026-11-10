from importlib.metadata import version

import fonderie_burin


def test_version_matches_installed_metadata() -> None:
    assert fonderie_burin.__version__ == version("fonderie-burin")
