#!/usr/bin/env python3
import sys
import os
import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path

def create_backup(source, destination=None, compress=False):
    source = Path(source).resolve()
    if not source.exists():
        print(f"Source does not exist: {source}", file=sys.stderr)
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = source.name

    if destination is None:
        destination = Path.home() / "backups"
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)

    if source.is_file():
        base_name = f"{name}_{timestamp}"
        if compress:
            import zipfile
            zip_path = destination / f"{base_name}.zip"
            with zipfile.ZipFile(str(zip_path), "w", zipfile.ZIP_DEFLATED) as zf:
                zf.write(source, arcname=name)
            size = zip_path.stat().st_size
            print(f"Backed up {source} -> {zip_path} ({size} bytes)")
            return str(zip_path)
        else:
            dest_path = destination / f"{base_name}"
            shutil.copy2(source, dest_path)
            print(f"Backed up {source} -> {dest_path}")
            return str(dest_path)

    elif source.is_dir():
        base_name = f"{name}_{timestamp}"
        if compress:
            import zipfile
            zip_path = destination / f"{base_name}.zip"
            with zipfile.ZipFile(str(zip_path), "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        full_path = Path(root) / file
                        arcname = full_path.relative_to(source.parent)
                        zf.write(full_path, arcname=arcname)
            size = zip_path.stat().st_size
            print(f"Backed up {source} -> {zip_path} ({size} bytes)")
            return str(zip_path)
        else:
            dest_path = destination / base_name
            shutil.copytree(source, dest_path)
            print(f"Backed up {source} -> {dest_path}")
            return str(dest_path)

def list_backups(destination=None):
    destination = Path(destination or (Path.home() / "backups")).resolve()
    if not destination.exists():
        print("No backups directory found.")
        return

    backups = sorted(destination.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
    for b in backups:
        size = b.stat().st_size
        modified = datetime.fromtimestamp(b.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        print(f"{modified}  {size:>10,} bytes  {b.name}")

def main():
    parser = argparse.ArgumentParser(description="Simple file/directory backup tool")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("backup")
    p_backup = sub.add_parser("list")

    parser.add_argument("source", nargs="?", default=".")
    parser.add_argument("-d", "--destination", help="Backup destination directory")
    parser.add_argument("-z", "--compress", action="store_true", help="Create ZIP archive")

    args = parser.parse_args()

    if args.command == "backup":
        create_backup(args.source, args.destination, args.compress)
    elif args.command == "list":
        list_backups(args.destination)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()