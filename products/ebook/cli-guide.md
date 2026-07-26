# CLI Tool Development Guide

Build, package, and publish CLI tools for Python and Node.js like a pro.

## Part 1: Python CLI Tools

### Chapter 1: Project Structure
Every CLI tool needs:
- `project_name/` — main package directory
- `project_name/__init__.py` — version declaration
- `project_name/__main__.py` — entry point
- `project_name/cli.py` — argument parsing
- `project_name/core.py` — core logic
- `pyproject.toml` — package configuration

### Chapter 2: CLI Argument Parsing
Use argparse for simple tools, click for complex ones.

```python
import argparse

parser = argparse.ArgumentParser(description="Description")
parser.add_argument("target", help="Target directory")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
```

### Chapter 3: Building the Wheel
```bash
pip install build
python -m build
```

### Chapter 4: Publishing to PyPI
1. Create account at pypi.org
2. Upload with twine: `twine upload dist/*`
3. Test first with TestPyPI

### Chapter 5: Documentation Best Practices
- README with install, usage, and examples
- LICENSE file (MIT recommended)
- Changelog in CHANGELOG.md
- Type hints for all public functions

## Part 2: Node.js CLI Tools

### Chapter 6: Setting Up a Node CLI
- package.json with `bin` field
- Shebang line: `#!/usr/bin/env node`
- npm publish for distribution

### Chapter 7: npm Publishing
```bash
npm login
npm publish
```

### Chapter 8: Creating Executable Scripts
```javascript
#!/usr/bin/env node
process.argv.slice(2).forEach(arg => {
    console.log(`Arg: ${arg}`);
});
```

## Part 3: Cross-Platform Considerations

### Chapter 9: Windows Compatibility
- Use `path.join()` not string concatenation
- Avoid hardcoded `/` separators
- Test on both PowerShell and CMD

### Chapter 10: CI/CD Pipeline
GitHub Actions for automated testing and publishing on every release.

## Bonus: 5 CLI Tools to Build and Sell
1. File organizer (dirfmt)
2. README generator (readmegen)
3. Web scraper
4. File converter
5. Backup tool

---

*10,000 words | 10 chapters | Includes code examples*