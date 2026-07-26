#!/usr/bin/env python3
import sys
import json
import argparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def fetch_url(url, timeout=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; dirfmt-scraper/1.0)",
        "Accept": "text/html,application/xhtml+xml",
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset), resp.status, dict(resp.headers)

def extract_text(html):
    import re
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_links(html, base_url):
    import re
    from urllib.parse import urljoin
    links = re.findall(r'href=["\'](https?://[^"\']+)["\']', html)
    return list(set(links))

def main():
    parser = argparse.ArgumentParser(description="Quick web scraper for extracting text and links")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("-o", "--output", help="Output file (JSON)")
    parser.add_argument("--text-only", action="store_true", help="Print only extracted text")
    parser.add_argument("--links-only", action="store_true", help="Print only links")
    parser.add_argument("-j", "--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    try:
        html, status, headers = fetch_url(args.url)
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {args.url}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    if args.text_only:
        print(extract_text(html))
    elif args.links_only:
        links = extract_links(html, args.url)
        for link in sorted(links):
            print(link)
    elif args.json or args.output:
        data = {
            "url": args.url,
            "status": status,
            "title": "",
            "text_length": len(extract_text(html)),
            "links_count": len(extract_links(html, args.url)),
            "links": extract_links(html, args.url),
        }
        title_match = __import__("re").search(r"<title>(.*?)</title>", html, __import__("re").IGNORECASE)
        if title_match:
            data["title"] = title_match.group(1)

        output = json.dumps(data, indent=2, ensure_ascii=False)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Saved to {args.output}")
        else:
            print(output)
    else:
        print(f"=== {args.url} (HTTP {status}) ===")
        title_match = __import__("re").search(r"<title>(.*?)</title>", html, __import__("re").IGNORECASE)
        if title_match:
            print(f"Title: {title_match.group(1)}")
        print(f"Text length: {len(extract_text(html))} chars")
        links = extract_links(html, args.url)
        print(f"Links found: {len(links)}")
        print()
        print("--- TEXT ---")
        print(extract_text(html)[:2000])
        print()
        if links:
            print("--- LINKS ---")
            for link in sorted(links)[:20]:
                print(f"  {link}")

if __name__ == "__main__":
    main()