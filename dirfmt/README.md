# dirfmt

Organize files in any directory by type, date, or extension in seconds.

## Install

```bash
pip install dirfmt
```

## Usage

Organize files by type (default):
```bash
dirfmt /path/to/directory
```

Organize by date:
```bash
dirfmt /path/to/directory --by date
```

Organize by extension group:
```bash
dirfmt /path/to/directory --by ext
```

Dry run (preview without moving):
```bash
dirfmt /path/to/directory --dry-run -v
```

Organize current directory:
```bash
dirfmt
```

## Categories

By type, files are sorted into:
- `images` — .jpg, .png, .gif, .svg, .webp, .ico, .tiff, .psd
- `documents` — .pdf, .doc, .txt, .md, .csv, .xlsx, .ppt, .rtf, .odt
- `audio` — .mp3, .wav, .flac, .aac, .ogg, .m4a, .wma
- `video` — .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm
- `archives` — .zip, .rar, .7z, .tar, .gz, .bz2
- `code` — .py, .js, .ts, .java, .c, .cpp, .html, .css, .sql, .json, .yaml, etc.
- `fonts` — .ttf, .otf, .woff, .woff2
- `executables` — .exe, .msi, .app, .deb, .rpm, .pkg
- `other` — everything else

## Development

```bash
git clone https://github.com/dirfmt/dirfmt.git
cd dirfmt
pip install -e .
```

## License

MIT