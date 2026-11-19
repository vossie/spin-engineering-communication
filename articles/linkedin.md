# S.P.I.N. — A Lightweight Communication Standard for Engineering Teams

Engineering teams rarely struggle because nobody reports problems. They struggle because reports arrive with different assumptions about urgency, ownership, evidence, and the response expected.

“Urgent backend issue” might describe a production outage, a blocked test environment, or a request that has simply waited too long. The recipient has to decode the message before starting technical work.

Ambiguous urgency creates operational noise. Genuine incidents compete with routine defects. Cross-team requests can sound like escalations. Engineers are interrupted to establish context that could have been present in the first message.

Reporting and escalation are not the same action. Reporting makes a technical condition visible. Escalation changes the response path because impact or time sensitivity requires it. Teams need a small convention that supports both without turning every report into a new process.

S.P.I.N. uses four fields:

- **Subject** — what needs attention and, when known, who should act.
- **Priority** — actual urgency and expected response.
- **Impact** — what is affected.
- **Note** — concise evidence, context, or a reference.

Only Subject and Priority are mandatory.

```text
Subject: @Backend | Correct leaderboard payout response

Priority: High | UAT | Release Blocker

Impact: Frontend integration testing cannot complete. Scheduled release validation is blocked.

Note: API response differs from the agreed contract. Ticket ENG-1042.
```

The format is intentionally small. A routine report should take less than one minute. Ownership stays in Subject rather than becoming another required field. Detailed diagnosis remains in the ticket or incident record that already owns it.

Priority is not a measure of frustration. Critical should mean that the established incident response is required. High signals a serious degradation or delivery blocker. Normal covers routine engineering work. Low supports backlog prioritisation. Organisations should map those defaults to their existing severity policy.

Impact is optional because not every routine request needs a paragraph of consequences. For urgent work, however, it should normally be explicit. If the scope is unknown, say that it is under investigation rather than guessing.

S.P.I.N. does not replace incident management, security reporting, on-call escalation, PagerDuty, xMatters, Jira, ServiceNow, or release management. A suspected security incident still goes through the approved security process immediately.

A practical introduction can be a four-week trial: explain the format, use it in a few engineering channels, gather feedback, refine examples, then decide whether it improves clarity enough to adopt more broadly. Avoid compliance scoring and new approval gates. It is a writing convention, not bureaucracy.

Simplicity matters because communication standards only help when engineers can use them under real delivery pressure.

The open-source specification, templates, examples, and adoption guide are prepared in the S.P.I.N. repository. Add the public repository URL here after publication.

> Raise issues early. Communicate clearly. Escalate appropriately.

