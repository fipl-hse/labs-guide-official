"""
TextRank keyword extraction starter.
"""

from pathlib import Path


if __name__ == "__main__":
    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / "assets"

    result = None
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert result, "Keywords are not extracted"
