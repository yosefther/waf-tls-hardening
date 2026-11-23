# Architecture

## Planned request path

```text
Client -> HTTPS -> Ubuntu gateway -> HTTP over private network -> Ubuntu backend
                      Nginx                                      FastAPI
                      ModSecurity + OWASP CRS                    systemd
                      TLS 1.2 / 1.3                              PostgreSQL
                      nftables
```

Nginx will accept client requests and proxy them to the backend. ModSecurity
with OWASP CRS will inspect requests at the gateway. PostgreSQL will run on the
backend VM. The backend service must not accept connections from the client
network. See [network topology](network-topology.md) for the isolation checks.

The FastAPI application is one deployable backend. The `api`, `core`, `models`,
`schemas`, and `services` packages separate code within that application.

## Current files

- `backend/app/main.py` defines `GET /health` and includes the item API.
- `backend/app/api/items.py` defines authenticated CRUD routes.
- `backend/app/core/` configures bearer authentication and database sessions.
- `backend/app/models/` and `backend/app/schemas/` define items and API data.
- `backend/migrations/` contains the PostgreSQL schema migration.
- `backend/tests/` checks health, CRUD, authentication, and PostgreSQL persistence.
- `gateway/` and `infrastructure/` contain empty work areas only.

Run the backend locally with the commands in the [backend README](../backend/README.md).
No deployed gateway or firewall configuration is available to verify yet.
