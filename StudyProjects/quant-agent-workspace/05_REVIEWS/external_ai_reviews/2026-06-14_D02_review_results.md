# External AI Review Results - 2026-06-14 D02

Status: completed_subagent_review
Reviewer: Codex reviewer sub-agent `Nietzsche`
Agent id: `019ec431-be0c-7f40-9696-9648356de974`

## Findings

1. High: D2 practice was not sufficiently gradable. Case 1 could teach the wrong shortcut that `Grade A + fresh` automatically means `OrderIntent=yes`; the stronger answer is `OrderIntent=conditional`.
2. High: `data_source_matrix.md` lacked several trade-use fields: market calendar/session, halt/suspension, timezone normalization, provider entitlement/license, latency SLA, raw checksum, survivorship/universe version, fees/tax/borrow/margin/FX, benchmark constituents.
3. Medium: evidence grading mixed source grade and claim/field usability. The system should grade exact claims/fields, not source brands only.
4. Medium: conflict handling needed more operational detail: reconciliation owner, restore criteria, audit record, and whether existing `OrderIntent` should expire or require recheck.
5. Low/Medium safety: no direct unattended live execution path was found, but `OrderIntent` was close to broker payload shape and needed a non-executable safety watermark.

## Adopted Fixes

- Updated D2 rubric so Case 1 is `OrderIntent=conditional`, not unconditional yes.
- Added required trade-use fields to `data_source_matrix.md`: timezone, market session, halt status, latency, entitlement, raw record/checksum, transform version, universe version, reconciliation status.
- Added three-part grading: source grade, claim grade, trade-use eligibility.
- Added additional source categories: market calendar/session/halts, fees/commissions/tax, borrow/short availability/margin, FX, index constituents, liquidity/ADV, macro calendar, vendor entitlement.
- Added reconciliation rules for broker/account/fill conflicts.
- Added `OrderIntent` safety flags in D01: `non_executable`, `requires_manual_rekey`, `approval_actor_required`, and forbidden broker execution fields.

## Can D2 Continue?

Yes. D2 can continue, but D3 should stay closed until the user completes the three-case source classification exercise and understands:

- Case 1 is conditional, not automatic yes.
- Case 2 is research-only without primary evidence.
- Case 3 freezes new order intents until reconciliation.
