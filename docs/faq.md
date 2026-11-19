# FAQ

## Is S.P.I.N. a ticketing system?

No. It structures a message and works alongside the ticketing system already in use.

## Are all four fields required?

No. Subject and Priority are the only mandatory fields. Impact and Note are optional, although urgent escalation should normally include Impact.

## Where does ownership go?

In Subject: `Subject: @Platform | Investigate elevated API latency`. There is no separate mandatory Owner field.

## Does Critical automatically page someone?

Only if your existing incident policy and tooling say it does. S.P.I.N. does not create a parallel paging mechanism.

## Can a staging issue be Critical?

Yes. Environment informs impact but does not determine it. Apply the organisation's severity policy.

## What if impact is unknown?

Say so: `Impact: Scope and production impact are under investigation.` Do not delay a material report while waiting for certainty.

## Should detailed logs go in Note?

Usually not. Summarise the evidence and link to the appropriate restricted or durable system. Never include secrets or sensitive incident evidence in a public message.

## Does S.P.I.N. replace security reporting?

No. Suspected security incidents must follow the established security process immediately.

## Is “SPIN” unique?

No. The acronym is used by unrelated sales, communication, influencing, and software-process frameworks. The project does not claim exclusive ownership of the acronym. Complete a legal naming review before formal public launch.

