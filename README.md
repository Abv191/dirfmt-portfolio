# dirfmt Portfolio

CLI tools and digital products for developers. Built to earn. Built to scale.

## Products

### CLI Tools
| Tool | Description | Install |
|------|-------------|---------|
| dirfmt | Organize files by type, date, or extension | `pip install dirfmt` |
| readmegen | Generate README.md from package.json | `npm install -g readmegen` |
| scraper | Quick web scraper for text and links | `pip install scraper` (coming) |
| converter | Convert between md/html, csv/json | `pip install converter` (coming) |
| backup-tool | File/directory backup with ZIP support | `pip install backup-tool` (coming) |

### Digital Products
| Product | Price | Platform |
|---------|-------|----------|
| Developer Prompt Pack | $19 | Gumroad |
| Solo Dev Notion Template | $29 | Etsy |
| CLI Tool Development Guide | $27 | Gumroad |

## Quick Start

```bash
# Install dirfmt
pip install dirfmt
dirfmt /path/to/directory

# Install readmegen
npm install -g readmegen
readmegen /path/to/project

# Organize current directory
dirfmt
```

## Revenue Goal

Target: $3,000/month within 90 days through tool subscriptions, digital products, and freelance services.

## Project Structure

```
dirfmt-portfolio/
├── dirfmt/              Python CLI tool (organized files)
├── readmegen/           Node.js CLI tool (README generator)
├── tools/               Additional CLI utilities
│   ├── web-scraper/
│   ├── file-converter/
│   └── backup-tool/
├── landing/             Portfolio landing page
├── products/            Digital products
│   ├── prompt-pack/
│   └── notion-template/
├── tests/               Playwright E2E tests
├── .github/workflows/   CI/CD pipeline
└── MONETIZATION.md      Full monetization strategy
```

## Development

```bash
# Test landing page
cd landing && python -m pytest ../tests/test_landing.py -v

# Build dirfmt package
cd dirfmt && python -m build

# Build readmegen package
cd readmegen && npm pack
```

## License

All tools: MIT. Digital products: personal use license.