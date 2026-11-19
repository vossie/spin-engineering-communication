# Ownership Without Blame

S.P.I.N. places ownership in Subject because a message is easier to route when the intended responder is visible.

```text
Subject: @Identity | Review token refresh failures
```

This means “please coordinate the next technical action,” not “your team caused the problem.”

## When ownership is known

Mention the team or person responsible for the component or decision. Prefer stable team ownership over naming an individual unless the request is genuinely personal.

## When ownership is uncertain

Choose the best initial coordinating team and state uncertainty in Note, or omit the mention and ask the channel to help route it.

```text
Subject: Identify owner for intermittent checkout timeout

Priority: Normal | Staging | Business Hours

Note: The failing boundary appears to be between Checkout and Payments; ownership is not yet confirmed.
```

Do not broadcast-tag multiple teams to manufacture urgency. Add participants when evidence identifies a dependency or the established incident process requires them.

