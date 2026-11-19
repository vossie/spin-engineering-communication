# The Framework

## Subject — required

Subject is the routing and action signal. It answers: **what needs attention, and who should act?**

Good subjects:

- `@Platform | Investigate elevated API latency`
- `@Mobile | Update authentication configuration`
- `@Backend | Resolve WebSocket connection failures`

Avoid `URGENT!!!`, `Everything is broken`, or `Critical backend issue` unless evidence supports the stated severity—and even then, describe the technical condition.

An ownership mention identifies the best initial responder. It is not a declaration of blame.

## Priority — required

Priority answers: **what response does the actual impact require?**

```text
Priority: Critical | Production | Immediate
Priority: High | Release Blocker | Today
Priority: Normal | Non-production | Business Hours
Priority: Low | Improvement | Backlog
```

The first value is the S.P.I.N. priority. The remaining values are concise context and may be adapted to local policy.

## Impact — optional

Impact answers: **what is affected?** Include the relevant environment, customer, operational, delivery, or functional scope.

Good Impact statements distinguish known facts from uncertainty:

```text
Impact: Customers cannot retrieve reward balances. Production impact confirmed.
```

```text
Impact: Scope and production impact are under investigation.
```

## Note — optional

Note answers: **what concise evidence or context helps the next action?**

Useful content includes a ticket reference, log pattern, suspected cause clearly labelled as a hypothesis, dependency, workaround, or proposed resolution.

Keep detailed investigation in the existing system of record. Never paste credentials, access tokens, sensitive configuration, or restricted incident evidence into a broadly visible S.P.I.N. message.

## Conformance at a glance

A conforming S.P.I.N. message has Subject and Priority, keeps ownership within Subject, treats Impact and Note as optional, and never overrides incident or security policy.

