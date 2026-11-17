# Testing plan

## Available now

From `backend/`, run `python -m pytest -q tests`. This checks the local
`GET /health` response. CI also checks Python syntax and Ruff style.

## Planned security verification

TEST-01 will supply repeatable PASS/FAIL tests and evidence for:

1. HTTPS certificate validation using the local test CA.
2. TLS 1.2/1.3 acceptance and obsolete protocol rejection.
3. WAF detection events and blocking events with matching rule IDs.
4. Nginx reverse proxy behavior for normal requests.
5. Backend service isolation from the client network.

Record test commands, environment, expected results, actual results, and
sanitized logs. These checks are not implemented yet.
