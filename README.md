# WAF & TLS Hardening

## Project overview

This is our graduation project repo. We plan to run Nginx, ModSecurity, and
OWASP CRS on one Ubuntu VM, with FastAPI and PostgreSQL on another. The backend
has `/health`, authenticated item CRUD, a PostgreSQL migration, and tests. VMs
and gateway setup are still to do.

## Architecture

Planned deployment:

```text
Client
   |
 HTTPS
   |
Ubuntu Gateway
   | Nginx
   | ModSecurity + OWASP CRS
   | TLS 1.2 / 1.3
   | nftables
   |
Private Network
   |
Ubuntu Backend
   | FastAPI (modular monolith)
   | systemd
   | PostgreSQL
```

Clients should only reach the gateway. The gateway will talk to the backend
over a private network. See [architecture](docs/architecture.md) and
[network topology](docs/network-topology.md).

## Tech stack

Ubuntu Server, Nginx, ModSecurity, OWASP CRS, nftables, FastAPI, systemd, and
PostgreSQL. Python dependencies are listed in
[backend/requirements.txt](backend/requirements.txt).

## Repository structure

| Path | Contents |
| --- | --- |
| `backend/` | FastAPI app, migrations, and tests |
| `gateway/` | Nginx, WAF, and TLS work areas |
| `infrastructure/` | Ansible, systemd, networking, and nftables work areas |
| `tests/` | Planned gateway and integration tests |
| `docs/` | Architecture, team plan, deployment, and testing notes |
| `.github/` | CI and contribution templates |

The gateway and infrastructure folders are empty apart from `.gitkeep` files.

## Local setup

Use Python 3.12 or newer. From the repository root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

In another terminal, run `curl http://127.0.0.1:8000/health`. It should return
`{"status":"ok"}`. The server command is for local development only. See the
[backend setup guide](backend/README.md) for PostgreSQL and authenticated routes.

## Team responsibilities

| Member | Work |
| --- | --- |
| 1, backend and integration lead | FastAPI, PostgreSQL, backend tests, code review, integration |
| 2, WAF | ModSecurity, OWASP CRS, WAF policies, audit logs, blocking tests |
| 3, TLS and Linux security | HTTPS, certificates, TLS settings, security headers, nftables |
| 4, infrastructure and QA | Ubuntu VMs, networking, SSH, systemd, setup scripts, integration tests |

See the [team plan](docs/team-plan.md) for issues and reading links.

## Development workflow

`main` is the integration branch. Create a branch for each issue, make focused
commits, and open a pull request. Use names such as `feat/backend-postgresql`
or `test/security-integration`. A teammate should review the PR and CI should
pass before merging. Do not push directly to `main`. Never commit credentials,
private keys, or local `.env` files.

## Testing

From `backend/` with the virtual environment active:

```bash
python -m pytest -q tests
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

CI tests `/health`, CRUD, and PostgreSQL migration and persistence. See
[testing](docs/testing.md) for gateway and VM checks still to add.

## Resources

- [Team plan and issue assignments](docs/team-plan.md)
- [Deployment notes](docs/deployment.md)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Ubuntu Server documentation](https://ubuntu.com/server/docs/)
