# WAF & TLS Hardening

## Project overview

This university project puts a FastAPI backend behind an Ubuntu gateway. The
gateway will handle HTTPS and inspect requests with ModSecurity and OWASP CRS.
The repository currently has a local `/health` endpoint, a backend test, and
CI. The gateway, VMs, and PostgreSQL integration are not implemented yet.

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

Only the gateway should accept client traffic. The backend service will be
reachable from the gateway over a private network. See
[architecture](docs/architecture.md) and
[network topology](docs/network-topology.md) for the planned layout.

## Tech stack

Ubuntu Server, Nginx, ModSecurity, OWASP CRS, nftables, FastAPI, systemd, and
PostgreSQL. Python dependencies are listed in
[backend/requirements.txt](backend/requirements.txt).

## Repository structure

| Path | Contents |
| --- | --- |
| `backend/` | FastAPI app and unit tests |
| `gateway/` | Nginx, WAF, and TLS work areas |
| `infrastructure/` | Ansible, systemd, networking, and nftables work areas |
| `tests/` | Planned gateway and integration tests |
| `docs/` | Architecture, team plan, deployment, and testing notes |
| `.github/` | CI and contribution templates |

Empty work areas contain `.gitkeep` files. They do not contain working
configuration.

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
`{"status":"ok"}`. The server command is for local development only.

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
python -m ruff check app tests
python -m ruff format --check app tests
```

The current test covers `/health`. Gateway and network checks are listed in
the [testing plan](docs/testing.md) and will be added with the related issues.

## Resources

- [Team plan and issue assignments](docs/team-plan.md)
- [Deployment notes](docs/deployment.md)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Ubuntu Server documentation](https://ubuntu.com/server/docs/)
