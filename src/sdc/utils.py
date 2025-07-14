from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

def check_duplicate(song_path: Path) -> bool:
    """Placeholder for duplicate check logic."""
    # TODO: implement duplicate check
    return False
