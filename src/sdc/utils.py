from pathlib import Path
import os
import random

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Directory that contains music files mounted from the NAS.
MUSIC_DIR = Path(os.getenv("NAS_PATH", "/music"))

# Build timestamp provided at Docker image creation time. If not set,
# defaults to "unknown". This is used to display when the running
# container was built/deployed.
BUILD_TIMESTAMP = os.getenv("BUILD_TIMESTAMP", "unknown")


def _list_music_files() -> list[Path]:
    """Return a list of all files under ``MUSIC_DIR`` recursively."""
    return [Path(root) / name for root, dirs, files in os.walk(MUSIC_DIR) for name in files]


def get_nas_diagnostics() -> str:
    """Return a message with basic diagnostics about ``MUSIC_DIR``."""
    path_str = str(MUSIC_DIR)
    if not MUSIC_DIR.exists():
        return f"NAS path {path_str} not found"
    if not MUSIC_DIR.is_dir():
        return f"NAS path {path_str} is not a directory"
    try:
        file_count = len(_list_music_files())
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
    files = _list_music_files()
    if not files:
        return "No music files found"
    return random.choice([f.name for f in files])


def get_build_timestamp() -> str:
    """Return the build/deploy timestamp for the running container."""
    return BUILD_TIMESTAMP
