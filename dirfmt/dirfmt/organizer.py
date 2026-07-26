import os
import shutil
from datetime import datetime
from pathlib import Path


CATEGORY_MAP = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff", ".psd"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".csv", ".xlsx", ".xls", ".ppt", ".pptx"},
    "audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".aiff"},
    "video": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpg", ".mpeg"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".dmg", ".iso"},
    "code": {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".go", ".rb", ".php", ".swift", ".kt", ".scala", ".sh", ".bat", ".ps1", ".sql", ".json", ".yaml", ".yml", ".toml", ".xml", ".html", ".css", ".scss", ".less", ".vue", ".svelte", ".rs", ".lua", ".pl", ".r", ".ex", ".exs", ".clj", ".hs"},
    "fonts": {".ttf", ".otf", ".woff", ".woff2", ".eot", ".svg", ".fon"},
    "executables": {".exe", ".msi", ".app", ".deb", ".rpm", ".pkg", ".dmg", ".scr"},
}


def get_category(ext):
    ext = ext.lower()
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return "other"


def organize_directory(directory, dry_run=False, category_by="type", log=False):
    directory = Path(directory).resolve()
    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    moved = 0
    errors = 0
    log_entries = []

    for item in directory.iterdir():
        if item.is_file() and item.name != "README.md":
            ext = item.suffix
            if category_by == "type":
                dest_dir_name = get_category(ext)
            elif category_by == "date":
                mtime = datetime.fromtimestamp(item.stat().st_mtime)
                dest_dir_name = mtime.strftime("%Y-%m")
            else:
                dest_dir_name = "other"

            dest_dir = directory / dest_dir_name
            dest = dest_dir / item.name

            if dest == item:
                continue

            if log:
                log_entries.append(f"{item.name} -> {dest_dir_name}/{item.name}")

            if not dry_run:
                try:
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    if dest.exists():
                        base = dest.stem
                        suffix = dest.suffix
                        counter = 1
                        while dest.exists():
                            dest = dest_dir / f"{base}_{counter}{suffix}"
                            counter += 1
                    shutil.move(str(item), str(dest))
                    moved += 1
                except Exception as e:
                    if log:
                        log_entries.append(f"ERROR: {item.name} -> {e}")
                    errors += 1
            else:
                moved += 1

    return {"moved": moved, "errors": errors, "log": log_entries, "directory": str(directory)}