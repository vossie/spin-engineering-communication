# Integration Issue

```text
Subject: @Identity | Investigate token refresh contract mismatch

Priority: Normal | Integration | Business Hours

Impact: Automated integration tests fail in the shared test environment. Production is unaffected.

Note: The client expects expiresIn as an integer; the test response currently returns a string. Reproduction is linked in ticket INT-204.
```

