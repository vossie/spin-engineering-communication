# S.P.I.N. Engineering Communication Standard

**Clear Issues. Appropriate Urgency. Better Engineering.**

S.P.I.N. is a lightweight convention for reporting engineering issues, incidents, defects, integration problems, and cross-team requests. It gives the recipient four predictable signals without introducing another workflow or approval process.

> Raise issues early. Communicate clearly. Escalate appropriately.

## The format

| Field | Purpose | Required? |
|---|---|---|
| **S — Subject** | What needs attention and, where appropriate, who should act | Yes |
| **P — Priority** | Actual urgency and expected response | Yes |
| **I — Impact** | What is affected and at what scope | No |
| **N — Note** | Concise evidence, context, links, or workaround | No |

```text
Subject: @Platform | Investigate elevated API latency

Priority: High | Production Degradation | Prompt Coordination

Impact: Response times exceed the service objective for approximately 20% of requests.

Note: Started at 14:20 UTC. Investigation is linked in the incident record.
```

Only **Subject** and **Priority** are mandatory. Ownership belongs in the Subject when a responsible team or person is known.

## Why use it?

Engineering messages often mix technical impact, urgency, ownership, and emotion into an unstructured alert. Recipients must first decode the request before they can act. S.P.I.N. creates a small, consistent message envelope that helps teams:

- distinguish reporting from escalation;
- route work without inventing new ownership processes;
- state impact without overstating certainty;
- preserve normal workflows for routine issues; and
- give genuine incidents the attention required by existing policy.

S.P.I.N. does not replace incident management, security reporting, on-call escalation, PagerDuty, xMatters, Jira, ServiceNow, release management, or an organisation's severity policy.

## Start in under a minute

1. Copy the template.
2. Write a specific Subject and include ownership when known.
3. Map Priority to your organisation's severity policy.
4. Add Impact for urgent work or when scope is useful.
5. Add only the Note needed to support the next action.

```text
Subject: @Team | Brief description

Priority: Normal | Non-production | Business Hours

Impact: [Optional] What is affected?

Note: [Optional] Supporting technical information.
```

Routine use should take less than one minute.

## Priority defaults

| Priority | Definition | Expected response |
|---|---|---|
| Critical | Active significant production incident or critical operational failure | Immediate incident response |
| High | Significant delivery blocker or serious degradation | Prompt technical coordination |
| Normal | Routine defects and non-production issues | Normal business-hours workflow |
| Low | Minor defects, improvements, and non-urgent requests | Backlog prioritisation |

These are illustrative defaults. Existing organisational policy takes precedence. A non-production issue can still be Critical when circumstances justify it. Suspected security incidents must use the established security process regardless of environment or known impact.

## Use it with existing tools

S.P.I.N. is deliberately tool-neutral. The same four fields work in Teams, Slack, Jira, GitHub Issues, email, and incident coordination channels. Use the provided [templates](templates/) and keep detailed investigation in the system that already owns it.

## Documentation

- [Formal specification](SPECIFICATION.md)
- [Design principles](PRINCIPLES.md)
- [Getting started](docs/getting-started.md)
- [Framework guide](docs/framework.md)
- [Priority guidelines](docs/priorities.md)
- [Examples](docs/examples.md)
- [Adoption guide](docs/adoption-guide.md)
- [FAQ](docs/faq.md)
- [Licensing recommendation](LICENSING.md)
- [Publication checklist](PUBLICATION_CHECKLIST.md)

## Contributing

Contributions that improve clarity, accessibility, examples, translations, and integrations are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Licence

Documentation, the specification, examples, templates, and original SVG artwork are licensed under [CC BY 4.0](LICENSE). Website software and workflow code are licensed under the [MIT License](LICENSE-CODE). These licences do not grant trademark rights or exclusive rights to the acronym “S.P.I.N.”

