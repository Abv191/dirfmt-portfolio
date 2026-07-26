# readmegen

Generate a README.md from your project structure and package.json. Perfect for quickly documenting open-source projects.

## Install

```bash
npm install -g readmegen
```

## Usage

Generate README in current directory:
```bash
readmegen
```

Generate README for a specific project:
```bash
readmegen /path/to/project
```

Overwrite existing README:
```bash
readmegen /path/to/project --overwrite
```

## What It Generates

- Project title and description (from package.json)
- Version badge
- License badge
- Dependencies count badge
- Installation section with npm command
- Customizable marker for manual additions

## License

MIT