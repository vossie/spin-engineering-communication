# S.P.I.N. Engineering Communication Standard

Version 1.0.0-draft

## 1. Purpose

S.P.I.N. defines a compact message structure for communicating engineering issues, incidents, defects, integration problems, and cross-team requests.

It is a communication convention. It is not an incident management system, ticketing platform, severity policy, approval process, or replacement for established operational procedures.

## 2. Normative language

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirements and recommendations for conforming messages.

## 3. Message structure

A S.P.I.N. message contains four fields in this order:

1. Subject
2. Priority
3. Impact
4. Note

Subject and Priority are mandatory. Impact and Note are optional. Implementations MUST NOT require additional S.P.I.N. fields. Tools MAY retain their own metadata outside the S.P.I.N. message.

```text
Subject: @Team | Brief description

Priority: Normal | Non-production | Business Hours

Impact: [Optional] What is affected?

Note: [Optional] Supporting technical information.
```

### 3.1 Subject — required

Subject identifies the issue, action, or request. It SHOULD be concise, specific, and action-oriented. Where responsibility is known, it SHOULD include the responsible team or person.

```text
Subject: @Backend | Resolve WebSocket connection failures
```

The Subject MUST NOT exaggerate severity beyond available evidence. Labels such as “urgent,” “critical,” or “everything is broken” SHOULD NOT replace a technical description.

### 3.2 Priority — required

Priority communicates urgency and the expected response. It MUST reflect actual impact and operational need rather than frustration, seniority, or organisational pressure.

Recommended defaults:

| Priority | Definition | Expected response |
|---|---|---|
| Critical | Active significant production incident or critical operational failure | Immediate incident response |
| High | Significant delivery blocker or serious degradation | Prompt technical coordination |
| Normal | Routine engineering defects and non-production issues | Normal business-hours workflow |
| Low | Minor defects, improvements, and non-urgent requests | Backlog prioritisation |

Organisations SHOULD map these labels to existing severity and response policies. Existing incident and security policies always take precedence.

```text
Priority: Critical | Production | Immediate
Priority: High | UAT | Release Blocker
Priority: Normal | Non-production | Business Hours
Priority: Low | Improvement | Backlog
```

A non-production issue MAY be Critical when circumstances justify it. Environment alone does not determine priority.

### 3.3 Impact — optional

Impact describes what is affected. When known, it SHOULD identify relevant customer, operational, delivery, environment, functional, or scope effects.

```text
Impact: QA regression testing is blocked in staging. Production is unaffected.
```

Unknown impact SHOULD be stated explicitly rather than guessed.

```text
Impact: Scope and production impact are under investigation.
```

Although optional in the basic format, Impact SHOULD normally be present for urgent escalation.

### 3.4 Note — optional

Note provides concise supporting information such as evidence, logs, a suspected cause, a ticket reference, dependencies, a workaround, or a suggested resolution.

Detailed investigation SHOULD remain in the existing ticket, incident record, or engineering system of record. Notes MUST NOT expose credentials, access tokens, personal data, or sensitive configuration.

## 4. Ownership

Ownership is expressed in Subject. S.P.I.N. introduces no separate mandatory owner field.

```text
Subject: @Mobile | Update authentication configuration
```

An ownership mention is a routing signal, not proof of fault. When ownership is unclear, the sender SHOULD name the best initial coordinating team or omit the mention and ask for routing assistance.

## 5. Reporting and escalation

Reporting makes an issue visible. Escalation changes the response path because impact or urgency requires it. A clear report is not automatically an escalation.

Senders SHOULD raise issues early with the best evidence available, state uncertainty, and revise Priority when facts change. Recipients SHOULD respond to the technical content rather than infer blame from the ownership mention.

## 6. Incident and security compatibility

S.P.I.N. MUST NOT replace:

- production incident management;
- security incident reporting;
- on-call escalation;
- PagerDuty or xMatters;
- Jira or ServiceNow;
- release management; or
- existing severity classification policies.

A suspected security incident MUST be reported promptly through the established security process, even when production impact is unknown. Sensitive evidence SHOULD remain in the restricted incident record.

## 7. Conformance

A message conforms to S.P.I.N. when:

- Subject is present;
- Priority is present;
- ownership, when stated, appears within Subject;
- Impact and Note remain optional;
- no additional S.P.I.N. field is treated as mandatory; and
- use of S.P.I.N. does not bypass a controlling incident, security, or operational policy.

## 8. Example

```text
Subject: @Backend | Correct leaderboard payout response

Priority: High | UAT | Release Blocker

Impact: Frontend integration testing cannot complete. Scheduled release validation is blocked.

Note: API response differs from the agreed contract. Ticket ENG-1042.
```

