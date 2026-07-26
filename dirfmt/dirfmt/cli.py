import argparse
import sys

from dirfmt import __version__
from dirfmt.organizer import organize_directory


def main():
    parser = argparse.ArgumentParser(
        prog="dirfmt",
        description="Organize files in a directory by type, date, or extension.",
        epilog="Example: dirfmt /path/to/folder --by type",
    )
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize (default: current directory)")
    parser.add_argument("-b", "--by", choices=["type", "date", "ext"], default="type", help="Organize files by category (default: type)")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Show what would be done without moving files")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print moved files")
    parser.add_argument("--version", action="version", version=f"dirfmt {__version__}")

    args = parser.parse_args()

    try:
        result = organize_directory(args.directory, dry_run=args.dry_run, category_by=args.by, log=args.verbose)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        print(f"Dry run: would organize {result['moved']} files in {result['directory']}")
    else:
        print(f"Organized {result['moved']} files in {result['directory']}")

    if result["errors"]:
        print(f"Errors: {result['errors']}", file=sys.stderr)

    if args.verbose and result["log"]:
        for entry in result["log"]:
            print(entry)


if __name__ == "__main__":
    main()