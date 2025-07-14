from pathlib import Path
import os
import random

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Directory that contains music files mounted from the NAS.
MUSIC_DIR = Path(os.getenv("NAS_PATH", "/music"))

def check_duplicate(song_path: Path) -> bool:
    """Placeholder for duplicate check logic."""
    # TODO: implement duplicate check
    return False


def get_random_music_file() -> str:
    """Return the name of a random music file from ``MUSIC_DIR``.

    If no files are found, a message stating so is returned.
    """
    files = [p.name for p in MUSIC_DIR.rglob("*") if p.is_file()]
    if not files:
        return "No music files found"
    return random.choice(files)
