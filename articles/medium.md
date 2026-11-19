# S.P.I.N. — A Lightweight Communication Standard for Engineering Teams

## The communication problem

Engineering organisations have no shortage of tools for tickets, incidents, chat, paging, and release coordination. Yet the first message about a problem is often unstructured.

It may identify a component but not the impact. It may use “critical” to mean that somebody is frustrated. It may ask several teams to respond without making ownership clear. Or it may contain a long investigation while never stating what action is required.

The issue is not a missing platform. It is the absence of a shared, lightweight convention at the point where technical work is communicated.

## Ambiguous urgency creates noise

When every issue is urgent, genuine incidents become harder to distinguish. Recipients spend time establishing whether customers are affected, whether a release is blocked, and whether the sender expects an immediate response or normal backlog handling.

This creates interruption without necessarily creating clarity. It can also make a routine cross-team request sound like an organisational escalation.

Priority should follow impact and response need—not the seniority of the sender, the length of time a request has existed, or the intensity of the wording.

## Reporting is not escalation

Reporting makes a condition visible. Escalation changes the response path because the condition warrants it.

Teams should report early without needing complete certainty. They should also be able to report a routine defect without accidentally activating an incident posture. A useful communication convention must support both behaviours.

## Introducing S.P.I.N.

S.P.I.N. stands for Subject, Priority, Impact, and Note.

```text
Subject: @Team | Brief description

Priority: Normal | Non-production | Business Hours

Impact: [Optional] What is affected?

Note: [Optional] Supporting technical information.
```

Only Subject and Priority are mandatory. Ownership is communicated through Subject.

### Subject

Subject states what needs attention and, when ownership is known, who should take the next action.

```text
Subject: @Platform | Investigate elevated API latency
```

The team mention is a routing signal, not an attribution of blame. A useful Subject is specific enough that the recipient understands the technical request without reading a paragraph first.

### Priority

Priority communicates urgency and expected response.

Recommended defaults are:

- **Critical:** active significant production incident or critical operational failure;
- **High:** significant delivery blocker or serious degradation;
- **Normal:** routine defect or non-production issue; and
- **Low:** minor defect, improvement, or non-urgent request.

These labels are starting points. An organisation's incident and severity policies remain authoritative. A non-production issue can still be Critical if the circumstances justify it.

### Impact

Impact states what is affected: customers, operations, delivery, an environment, or a specific function.

```text
Impact: QA regression testing is blocked in staging. Production is unaffected.
```

If impact is unknown, say so. Uncertainty is more useful than unsupported certainty.

### Note

Note contains the minimum additional information needed for the next action: evidence, a suspected cause clearly labelled as a hypothesis, a ticket, dependency, or workaround.

Detailed investigation should remain in the existing system of record. Credentials, tokens, sensitive configuration, and restricted incident evidence never belong in a broadly visible issue report.

## Practical examples

### Production incident

```text
Subject: @Platform | Reward balance API unavailable

Priority: Critical | Production | Immediate

Impact: Customers cannot retrieve reward balances. Production customer impact confirmed.

Note: Elevated HTTP 503 responses observed. Incident response initiated.
```

### Release blocker

```text
Subject: @Backend | Correct leaderboard payout response

Priority: High | UAT | Release Blocker

Impact: Frontend integration testing cannot complete. Scheduled release validation is blocked.

Note: API response differs from the agreed contract. Ticket ENG-1042.
```

### Suspected security incident

```text
Subject: @Security | Potential credential exposure

Priority: Critical | Security Assessment | Immediate

Impact: Exposure scope and production impact are not yet established.

Note: Reported through the approved security incident channel. Sensitive evidence is retained in the restricted incident record.
```

S.P.I.N. does not replace the security incident process. The approved process must be used immediately.

## Introducing the framework

A lightweight four-week trial is enough to learn whether the convention fits:

1. Introduce the four fields, templates, and local priority mappings.
2. Encourage use in selected engineering channels and gather questions.
3. Refine examples and unclear guidance.
4. Decide whether to adopt, revise, or stop.

Do not add an approval step. Do not make every optional field mandatory. Do not score individual engineers on formatting compliance. The goal is clearer collaboration.

## Why simplicity matters

A communication standard is useful only when people can apply it during routine work and operational pressure. Four fields are enough to establish the request, urgency, effect, and supporting context. Two of them are optional.

S.P.I.N. is designed to fit Teams, Slack, Jira, GitHub Issues, email, and incident coordination without replacing any of them.

The open-source specification includes templates, examples, an adoption guide, and a static documentation site. Add the public specification URL here after publication.

> Raise issues early. Communicate clearly. Escalate appropriately.

