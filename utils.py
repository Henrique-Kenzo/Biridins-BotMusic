import shutil
from pathlib import Path

def get_ffmpeg():
    path = shutil.which("ffmpeg")
    if path:
        return path
    local = Path(__file__).parent / "ffmpeg.exe"
    return str(local) if local.exists() else None

