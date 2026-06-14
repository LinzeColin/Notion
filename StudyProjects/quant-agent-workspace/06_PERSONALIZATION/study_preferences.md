# Study Preferences

## Current Fit

- User wants aggressive, high-ROI, system-level learning.
- User is comfortable with trading-agent concepts and wants real-world applicability.
- Teaching must be direct and practical, not motivational.
- User understands that paper/model results are not realized returns because of execution friction, timing, slippage, spread, market regime, and event sensitivity.
- User's core motivation for trading agents is reducing time loss between signal detection and action, not merely producing research reports.

## Teaching Adjustment

Use the pattern:

`concept -> system contract -> failure mode -> artifact -> verification`

## Safety Adjustment

For trading-agent content, keep live execution behind human approval while still teaching the full research, paper-validation, risk, and order-intent pipeline.

Translate requests for "unattended live execution" into a supervised live execution workflow: independent monitoring, validation, risk checks, `OrderIntent`, urgent alerts, approval TTL, kill switch, audit log, and human-confirmed execution.
