# MostExpensiveWatches — watch auction records API, dataset, MCP server & CLI

Documented ultra-luxury watch auction data ($100k–$31M realized prices, primary-sourced),
free to use, built for AI agents, CLIs and apps. No API key required.

**Live site:** https://mostexpensivewatches.net

## For AI agents — MCP server (one line of config)

```json
{"mcpServers": {"mostexpensivewatches": {"url": "https://mostexpensivewatches.net/mcp"}}}
```

Streamable HTTP, JSON-RPC 2.0. Tools: `search_inventory`, `lookup_reference`,
`search_auction_comps`, `list_upcoming_auctions`, `get_market_estimate`,
`get_brand_info`, `search_answers`, `get_site_stats`.
Install docs: https://mostexpensivewatches.net/mcp/install

## Datasets (CC-BY 4.0, schema.org `Dataset`, refreshed automatically)

| Dataset | Live JSON | Snapshot here |
|---|---|---|
| Record Ledger — every documented watch auction record (all-time, per brand/material/year, record progressions) | [/data/records.json](https://mostexpensivewatches.net/data/records.json) | [`data/records.json`](data/records.json) |
| Auction Records — 1,150+ documented hammer prices with sources | [/api/auctions-dataset.json](https://mostexpensivewatches.net/api/auctions-dataset.json) | [`data/auction-records.json`](data/auction-records.json) |
| Grail Index — the $1M+ segment record (182 results, $616M documented) | [/data/grail-index.json](https://mostexpensivewatches.net/data/grail-index.json) | [`data/grail-index.json`](data/grail-index.json) |
| Price Index — daily repeat-listing index across merchants | [/data/watch-price-index.json](https://mostexpensivewatches.net/data/watch-price-index.json) | [`data/price-index.json`](data/price-index.json) |

Snapshots in this repo are point-in-time copies; the live endpoints recompile daily
via an autonomous verification pipeline. Cite as **"MostExpensiveWatches Record Ledger"**.

## API (43 endpoints, no key)

- OpenAPI 3.1: [`openapi.json`](openapi.json) · live: https://mostexpensivewatches.net/openapi.json
- Docs: https://mostexpensivewatches.net/api
- One-call snapshot: https://mostexpensivewatches.net/api/snapshot.json
- Examples: https://mostexpensivewatches.net/api/examples.json
- `llms.txt`: https://mostexpensivewatches.net/llms.txt

```bash
curl -s "https://mostexpensivewatches.net/api/listings/search?q=nautilus&limit=3"
curl -s "https://mostexpensivewatches.net/api/auctions?brand=Rolex&limit=5"
curl -s "https://mostexpensivewatches.net/api/answers/patek-5711-market-price.json"
```

## CLI (dependency-free Python)

```bash
curl -sO https://mostexpensivewatches.net/cli/mew.py
python3 mew.py search "daytona" --limit 5
```

Also in this repo: [`mew.py`](mew.py)

## Human surfaces the data powers

- [The Record Ledger](https://mostexpensivewatches.net/records) — every auction record, documented
- [How much is it worth?](https://mostexpensivewatches.net/worth) — 650 reference valuations
- [HAMMER](https://mostexpensivewatches.net/hammer) — daily guess-the-hammer-price game
- [Grail Index](https://mostexpensivewatches.net/grail-index) · [Price Index](https://mostexpensivewatches.net/price-index) · [Weekly brief](https://mostexpensivewatches.net/market-brief)

## License

Data: CC-BY 4.0 (attribution: MostExpensiveWatches). Code (`mew.py`): MIT.
