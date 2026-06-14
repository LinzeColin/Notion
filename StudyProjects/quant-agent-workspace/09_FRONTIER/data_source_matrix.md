# Data Source Matrix v1

Project: quant-agent-workspace  
Created: 2026-06-14  
Use: D02 artifact for evidence grading, freshness rules, and fail-closed behavior.

## Core Rule

No data enters signal generation unless the workspace knows:

1. `source`: where it came from.
2. `event_time`: when the market/business event happened.
3. `published_at`: when the source made it public.
4. `received_at`: when the workspace received it.
5. `tradable_at`: the earliest time the strategy could realistically trade on it.
6. `freshness_window`: how long it remains usable.
7. `confidence_grade`: how much trust the system can place on it.
8. `fail_closed_action`: what to block if the data is stale, missing, conflicted, or unverified.
9. `timezone` / `source_timezone`: how source time is normalized.
10. `market_session`: whether the relevant market is open, closed, auction, halt, or suspended.
11. `halt_status`: whether the symbol is halted, suspended, limit-up/down, or otherwise not normally tradable.
12. `latency_ms` / `received_delay`: how late the data arrived versus the source timestamp.
13. `provider_entitlement`: whether the workspace is allowed to use this feed for the intended purpose.
14. `raw_record_id` / `checksum`: how to replay or verify the raw input.
15. `transform_version`: parser and normalization version.
16. `coverage_universe_version`: what symbol universe or survivorship filter was used.
17. `reconciliation_status`: whether broker/account/ledger data is reconciled.

## How To Use This Matrix

When you see any data item, do not ask "is it interesting?" first. Ask these four questions in order:

| Step | Question | Decision |
|---:|---|---|
| 1 | Who produced it? | Assign Grade A/B/C/D |
| 2 | Is it fresh enough for this strategy? | If no, block signal and `OrderIntent` |
| 3 | Does it have event/published/received/tradable time? | If no, research-only or block live-like use |
| 4 | Is there any conflict with a stronger source? | If yes, trust stronger source and reconcile before new order intents |

Simple rule:

```text
A + fresh + timestamped + market open + no halt + normal spread/depth + no conflict = can support signal/order intent after risk gate
B = can support thesis; trade-sensitive use requires A cross-check
C = research lead only
D = reject as evidence
Conflict = stop and reconcile
```

For D02 practice, answer each case with:

```text
Grade=A/B/C/D, OrderIntent=yes/no/conditional, fail-closed=<what the system blocks or downgrades>
```

Worked example:

```text
Source: a blog post summarizing a company result with a link to the official filing.
Grade=B for the blog summary, but upgrade the evidence only if the official filing is checked as Grade A.
OrderIntent=no from the blog alone.
fail-closed=research-only until the Grade A filing is fetched, timestamped, and matched to tradable_at.
```

## Three-Part Grading

Do not grade only the brand name of the source. Grade the exact claim or field.

| Layer | Question | Example |
|---|---|---|
| Source grade | Who produced this record? | Exchange feed, broker report, company filing, news article, social post |
| Claim grade | Which claim/field is being used? | A vendor may be Grade A for bid/ask but not for corporate-action adjustment |
| Trade-use eligibility | Can this field support signal or `OrderIntent` now? | Requires freshness, market session, no halt, normal spread/depth, no stronger-source conflict, risk gate pass |

## Evidence Grades

| Grade | Source type | Typical examples | Agent use | Required handling |
|---|---|---|---|---|
| A | Primary official / direct system source | Exchange data, broker execution logs, SEC/ASX/HKEX filings, company announcements, official regulator docs | Can support strategy/risk decisions if fresh and timestamped | Store raw link or record ID, timestamp, parser version, and freshness window |
| B | Primary-adjacent / professional source | Earnings transcripts, company investor presentations, reputable data vendors, established financial newswires | Can support thesis and monitoring; should not override Grade A conflicts | Cross-check with Grade A when used for trade-sensitive signals |
| C | Secondary analysis / aggregator | Analyst summaries, web articles, dashboards, scraped aggregators, social-derived datasets | Lead generation and context only | Must be labeled unverified until upgraded |
| D | Weak / unverifiable / opinion source | Unsourced posts, screenshots, rumor, black-box model output, stale cached data | Never sufficient for order intent | Block promotion; use only as research lead |

## Minimum Source Matrix

| Data domain | Preferred grade | Required fields | Freshness window | Common failure | Fail-closed action |
|---|---|---|---|---|---|
| Live price / quote | A | symbol, venue, bid, ask, last, volume, timestamp, provider | seconds to minutes, strategy-specific | stale quote, crossed market, abnormal spread | block signal and order intent |
| OHLCV bars | A/B | symbol, venue, interval, open/high/low/close/volume, timezone, adjusted flag | minutes to daily, by strategy | missing bars, wrong timezone, bad adjustment | quarantine backtest or live signal |
| Order book / depth | A | venue, levels, sizes, timestamp, update sequence | sub-second to seconds | sequence gaps, stale depth, thin book | block marketable order intent |
| Broker account / positions | A | account, cash, margin, positions, buying power, timestamp | seconds to minutes | mismatch with local ledger | block new order intent; reconcile |
| Broker execution / fills | A | order id, fill id, price, qty, fees, venue, timestamp | immediate | missing fill, partial fill mismatch | stop paper/live reconciliation |
| Corporate actions | A | split/dividend/symbol change/effective date/source | daily before backtest/live use | stale adjustment | block backtest promotion |
| Filings / announcements | A | company, filing type, published_at, source url, accession/id | event-driven | delayed ingestion, duplicate filing | allow research only; block trade signal until timestamped |
| Fundamentals | A/B | period, metric, currency, restated flag, source, published_at | quarterly/annual; refresh on restatement | stale/restated values | downgrade signal confidence |
| News / event feed | B/C | headline, body/link, publisher, published_at, received_at | minutes to hours, event-specific | duplicate, rumor, late arrival | require corroboration for order intent |
| Alternative / scraped data | C/D | collection time, methodology, sample coverage, parser version | source-specific | scraping drift, sample bias | research-only until validated |
| Model output | D unless evidence-backed | model version, prompt/config, inputs, output, confidence, citations | expires with inputs | hallucination, missing citations | never directly create order intent without evidence refs |
| Market calendar / session | A | market, venue, holiday, session, auction, close, timezone | daily and intraday | wrong session or timezone | block `tradable_at` and order intent |
| Halt / suspension / limit state | A | symbol, venue, halt type, start/end, official source | immediate | missed halt or stale status | block signal and order intent |
| Fees / commissions / taxes | A/B | fee schedule, tax rule, commission tier, currency | before backtest and order intent | stale fees or wrong account tier | quarantine cost model |
| Borrow / short availability / margin | A | symbol, borrow availability, borrow rate, margin requirement, timestamp | immediate to daily | unavailable borrow or changed margin | block short/leveraged order intent |
| FX rates | A/B | pair, source, timestamp, bid/ask/mid, timezone | seconds to daily, by strategy | stale conversion | block cross-currency sizing |
| Index / benchmark constituents | A/B | index id, effective date, constituent, weight, vendor/source | daily or rebalance-specific | survivorship bias | quarantine backtest universe |
| Liquidity / ADV / volume profile | A/B | symbol, ADV, intraday volume curve, lookback, venue, timestamp | daily/intraday | stale capacity estimate | cap size or block order intent |
| Macro / event calendar | A/B | event name, scheduled time, country, source, release status | event-driven | wrong release time | block event-sensitive signal |
| Vendor entitlement / license | A | vendor, dataset, allowed use, account/license id, expiry | before use | unauthorized use | block ingestion/use |

## Time Semantics

| Field | Meaning | Why it matters |
|---|---|---|
| `event_time` | When the real-world event happened | Prevents lookahead bias |
| `published_at` | When the source publicly released it | Determines whether a backtest could know it |
| `received_at` | When the workspace ingested it | Measures data latency and pipeline delay |
| `tradable_at` | When a strategy could realistically act | Converts information into a realistic trading window |

Decision rule: if `tradable_at` is unknown, the data cannot be used for a live-like backtest or an `OrderIntent`.

## Conflict Rules

| Conflict | Example | Action |
|---|---|---|
| A vs B conflict | Broker position differs from dashboard estimate | Trust A, block new order intents until local ledger reconciles |
| A vs A conflict | Two market data providers disagree materially | Halt strategy using that field; log both sources |
| B/C only | News lead without filing or official confirmation | Research note only; no order intent |
| D only | Model says a catalyst exists with no citation | Reject as evidence; ask for source |

## Reconciliation Rules

When broker/account/fill data conflicts with the local ledger:

1. Freeze new `OrderIntent` for affected symbols and strategies.
2. Mark existing related `OrderIntent` as `expired` or `requires_recheck`.
3. Treat broker fill/account report as Grade A for actual account state, but do not proceed until the local ledger is rebuilt or explained.
4. Record `reconciliation_owner`, `reconciliation_status`, evidence used to restore service, and audit log reference.
5. Resume only after the ledger, positions, fills, fees, and cash reconcile within defined tolerance.

## Promotion Gates

Data can support a strategy only if:

1. Source grade is A or verified B for the relevant decision.
2. `event_time`, `published_at`, `received_at`, and `tradable_at` are recorded.
3. Freshness window is not expired.
4. Conflicts are resolved or explicitly downgraded.
5. The parser/data transformation has a version and reproducible log.
6. The data survived at least one replay check.

## D02 Practice Prompt

Classify these three sources:

1. An official exchange quote feed with bid/ask timestamp 30 seconds old.
2. A Twitter/X post claiming a company won a major contract, with no filing link.
3. A broker fill report that disagrees with the local paper ledger.

For each one, answer:

- Grade: A/B/C/D
- Can it support `OrderIntent`? yes/no/conditional
- Required fail-closed action

## D02 Practice Rubric

| Case | Strong answer | Why |
|---|---|---|
| 1 | Grade=A; `OrderIntent=conditional`; fail-closed=block if 30 seconds violates strategy freshness SLA, market is closed/halted, spread/depth abnormal, latency unknown, risk gate fails, or conflicts exist | A source alone is not enough; trade-use eligibility depends on freshness, session, liquidity, and risk |
| 2 | Grade=D or C; `OrderIntent=no`; fail-closed=research-only until official filing/company announcement or other Grade A/B corroboration is fetched and timestamped | Social claims without primary evidence cannot support order intent |
| 3 | Grade=A for broker fill report; `OrderIntent=no until reconciled`; fail-closed=freeze new order intents, expire/recheck related intents, reconcile broker report vs local ledger, then resume only with audit evidence | Strong source conflict means stop and reconcile before new decisions |
