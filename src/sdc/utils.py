from pathlib import Path
import os
import random

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Directory that contains music files mounted from the NAS.
MUSIC_DIR = Path(os.getenv("NAS_PATH", "/music"))


def get_nas_diagnostics() -> str:
    """Return a message with basic diagnostics about ``MUSIC_DIR``."""
    path_str = str(MUSIC_DIR)
    if not MUSIC_DIR.exists():
        return f"NAS path {path_str} not found"
    if not MUSIC_DIR.is_dir():
        return f"NAS path {path_str} is not a directory"
    try:
        file_count = len([p for p in MUSIC_DIR.rglob("*") if p.is_file()])
    except Exception as exc:  # pragma: no cover - diagnostics only
        return f"Error accessing {path_str}: {exc}"
    return f"NAS path {path_str} accessible, {file_count} files visible"

def check_duplicate(song_path: Path) -> bool:
    """Placeholder for duplicate check logic."""
    # TODO: implement duplicate check
    return False


def get_random_music_file() -> str:
    """Return the name of a random music file from ``MUSIC_DIR``.

    If no files are found, a message stating so is returned.
    """
    if not MUSIC_DIR.exists():
        return f"Music directory {MUSIC_DIR} not found"
    files = [p.name for p in MUSIC_DIR.rglob("*") if p.is_file()]
    if not files:
        return "No music files found"
    return random.choice(files)
