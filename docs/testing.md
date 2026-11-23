# Testing

## Available checks

From `backend/` with the dependencies installed:

```bash
python -m pytest -q tests
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

The tests check `GET /health`, bearer authentication, item CRUD, validation,
and 404 responses. With `TEST_DATABASE_URL` set, the PostgreSQL test runs the
Alembic migration and checks that an item survives an application restart.
CI provides PostgreSQL, runs these checks, and compiles the Python files.
A missing module usually means the virtual environment is inactive or
requirements were not installed.

## Planned integration checks

TEST-01 will add repeatable checks for HTTPS certificate validation, TLS
protocol restrictions, WAF detection and blocking with rule IDs, reverse
proxy behavior, and backend network isolation. The checks will use the actual
gateway address, test CA certificate, and VM network details after those files
exist.

For each check, record the command, expected result, actual result, and
sanitized logs. Do not include certificate private keys or credentials in test
evidence. Current CI does not test WAF, TLS, or VM networking.
