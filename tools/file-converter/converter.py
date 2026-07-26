#!/usr/bin/env python3
import sys
import os
import argparse
import json
import csv
import subprocess
from pathlib import Path

def convert_md_to_html(input_file, output_file):
    try:
        import markdown
        md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
        with open(input_file, "r", encoding="utf-8") as f:
            html = md.convert(f.read())
        full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{Path(input_file).stem}</title>
<style>body{{max-width:800px;margin:2rem auto;padding:0 1rem;font-family:sans-serif;line-height:1.6;}}</style>
</head><body>{html}</body></html>"""
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        return True
    except ImportError:
        return False

def convert_csv_to_json(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    return True

def convert_json_to_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return True
    return False

def convert_file(input_file, output_format):
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"File not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    stem = input_path.stem
    output_file = str(input_path.parent / f"{stem}.{output_format}")

    if input_path.suffix == ".md" and output_format == "html":
        if convert_md_to_html(str(input_path), output_file):
            print(f"Converted: {input_file} -> {output_file}")
            return True
        else:
            print("Markdown library not installed. Install with: pip install markdown", file=sys.stderr)
            sys.exit(1)

    if input_path.suffix == ".csv" and output_format == "json":
        convert_csv_to_json(str(input_path), output_file)
        print(f"Converted: {input_file} -> {output_file}")
        return True

    if input_path.suffix == ".json" and output_format == "csv":
        if convert_json_to_csv(str(input_path), output_file):
            print(f"Converted: {input_file} -> {output_file}")
            return True
        else:
            print("JSON must be a list of objects for CSV conversion", file=sys.stderr)
            sys.exit(1)

    print(f"No converter for {input_path.suffix} -> {output_format}", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert between file formats (md/html, csv/json)")
    parser.add_argument("input", help="Input file path")
    parser.add_argument("-f", "--format", required=True, choices=["html", "json", "csv"], help="Output format")
    parser.add_argument("-o", "--output", help="Output file path (default: auto-generate)")
    args = parser.parse_args()

    if args.output:
        convert_file(args.input, args.format)
        import shutil
        shutil.move(str(Path(args.input).parent / f"{Path(args.input).stem}.{args.format}"), args.output)
    else:
        convert_file(args.input, args.format)

if __name__ == "__main__":
    main()