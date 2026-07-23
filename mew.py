#!/usr/bin/env python3
"""MostExpensiveWatches public API CLI.

Usage:
  python mew.py stats
  python mew.py snapshot
  python mew.py brand rolex --limit 8
  python mew.py resolve "Rolex Pepsi"
  python mew.py search "Patek Nautilus" --limit 5
  python mew.py reference patek-philippe-nautilus-5711-1a
  python mew.py answers "5712" --summary --limit 5
  python mew.py answer patek-5711-market-price --lang es
  python mew.py auctions Rolex --limit 10
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

BASE = "https://mostexpensivewatches.net"


def get_json(path: str, params: dict | None = None) -> dict:
    qs = ("?" + urllib.parse.urlencode(params)) if params else ""
    req = urllib.request.Request(BASE + path + qs, headers={"User-Agent": "mew-cli/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def print_json(data: dict) -> None:
    print(json.dumps(data, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query MostExpensiveWatches public data.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("stats")
    sub.add_parser("snapshot")

    brand = sub.add_parser("brand")
    brand.add_argument("slug")
    brand.add_argument("--limit", type=int, default=8)
    brand.add_argument("--lang", default="en")

    resolve = sub.add_parser("resolve")
    resolve.add_argument("query")
    resolve.add_argument("--brand")
    resolve.add_argument("--limit", type=int, default=10)

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)

    ref = sub.add_parser("reference")
    ref.add_argument("slug")

    answers = sub.add_parser("answers")
    answers.add_argument("query", nargs="?", default="")
    answers.add_argument("--brand")
    answers.add_argument("--kind")
    answers.add_argument("--lang", default="en")
    answers.add_argument("--limit", type=int, default=10)
    answers.add_argument("--summary", action="store_true")

    answer = sub.add_parser("answer")
    answer.add_argument("slug")
    answer.add_argument("--lang", default="en")

    reviews = sub.add_parser("reviews")
    reviews.add_argument("query", nargs="?", default="")
    reviews.add_argument("--brand")
    reviews.add_argument("--lang", default="en")
    reviews.add_argument("--limit", type=int, default=10)

    review = sub.add_parser("review")
    review.add_argument("slug")
    review.add_argument("--lang", default="en")

    alternatives = sub.add_parser("alternatives")
    alternatives.add_argument("query")
    alternatives.add_argument("--brand")
    alternatives.add_argument("--lang", default="en")
    alternatives.add_argument("--limit", type=int, default=8)

    alternative = sub.add_parser("alternative")
    alternative.add_argument("slug")
    alternative.add_argument("--lang", default="en")
    alternative.add_argument("--limit", type=int, default=12)

    auctions = sub.add_parser("auctions")
    auctions.add_argument("brand", nargs="?")
    auctions.add_argument("--limit", type=int, default=10)

    args = parser.parse_args(argv)

    if args.cmd == "stats":
        print_json(get_json("/api/stats"))
    elif args.cmd == "snapshot":
        print_json(get_json("/api/snapshot.json"))
    elif args.cmd == "brand":
        print_json(get_json(f"/api/brands/{args.slug}", {"limit": args.limit, "lang": args.lang}))
    elif args.cmd == "resolve":
        params = {"q": args.query, "limit": args.limit}
        if args.brand:
            params["brand"] = args.brand
        print_json(get_json("/api/references/resolve", params))
    elif args.cmd == "search":
        print_json(get_json("/api/listings/search", {"q": args.query, "limit": args.limit}))
    elif args.cmd == "reference":
        print_json(get_json(f"/api/references/{args.slug}"))
    elif args.cmd == "answers":
        params = {"q": args.query, "lang": args.lang, "limit": args.limit}
        if args.brand:
            params["brand"] = args.brand
        if args.kind:
            params["kind"] = args.kind
        if args.summary:
            params["summary"] = "1"
        print_json(get_json("/api/answers/search", params))
    elif args.cmd == "answer":
        print_json(get_json(f"/api/answers/{args.slug}.json", {"lang": args.lang}))
    elif args.cmd == "reviews":
        if not args.query and not args.brand:
            print_json(get_json("/api/reviews/index.json"))
        else:
            params = {"q": args.query, "lang": args.lang, "limit": args.limit}
            if args.brand:
                params["brand"] = args.brand
            print_json(get_json("/api/reviews/search", params))
    elif args.cmd == "review":
        print_json(get_json(f"/api/reviews/{args.slug}", {"lang": args.lang}))
    elif args.cmd == "alternatives":
        params = {"q": args.query, "lang": args.lang, "limit": args.limit}
        if args.brand:
            params["brand"] = args.brand
        print_json(get_json("/api/alternatives/search", params))
    elif args.cmd == "alternative":
        print_json(get_json(f"/api/alternatives/{args.slug}", {"lang": args.lang, "limit": args.limit}))
    elif args.cmd == "auctions":
        params = {"limit": args.limit}
        if args.brand:
            params["brand"] = args.brand
        print_json(get_json("/api/auctions", params))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
