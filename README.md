# WAF & TLS Hardening

A four-student university project to build and verify a secure path from a
client through an Ubuntu gateway to a FastAPI backend. The repository currently
contains the foundation only: a working `/health` endpoint, a unit test, CI,
and planning documents. Gateway security and PostgreSQL are planned work.

## Planned architecture

```text
Client / Browser
       | HTTPS
Ubuntu Gateway VM: Nginx, ModSecurity, OWASP CRS, TLS 1.2/1.3, nftables
       | HTTP over private network
Ubuntu Backend VM: FastAPI modular monolith, systemd, PostgreSQL
```

The backend service must be unreachable from the client network. PostgreSQL
will initially run on the backend VM. The current repository does not provision
VMs or provide an operational gateway. See [architecture](docs/architecture.md)
and [network topology](docs/network-topology.md).

## Stack and repository layout

| Path | Purpose |
| --- | --- |
| `backend/` | FastAPI application and unit tests |
| `gateway/nginx/`, `gateway/waf/`, `gateway/tls/` | Gateway configuration work areas |
| `infrastructure/` | Ansible, systemd, networking, and nftables work areas |
| `tests/` | WAF, TLS, and end-to-end verification work areas |
| `docs/` | Architecture, team plan, deployment, and testing plans |
| `.github/` | CI and collaboration templates |

## Team

1. Backend developer and integration lead: FastAPI, PostgreSQL, API tests,
   review, and integration.
2. WAF engineer: Nginx/ModSecurity, OWASP CRS, policy tuning, audit logs, and
   detection and blocking tests.
3. TLS and Linux security engineer: HTTPS, certificates, protocol hardening,
   redirects, headers, and nftables.
4. Linux infrastructure and QA engineer: Ubuntu VMs, private networking, SSH,
   systemd, scripts, and end-to-end tests.

See [team plan](docs/team-plan.md) for issue ownership, dependencies, and
learning resources.

## Local development

Prerequisite: Python 3.12 or newer. From the repository root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

In another terminal, run `curl http://127.0.0.1:8000/health`. Expected response:
`{"status":"ok"}`. Run `python -m pytest -q tests` and
`python -m ruff check app tests` from `backend/` before opening a PR.

## Contribution workflow

`main` is the stable integration branch. Create one feature branch per task,
such as `feat/setup-baseline-api`, `feat/backend-postgresql`,
`feat/waf-modsecurity`, `feat/tls-https`, `feat/infra-ubuntu`, or
`test/security-integration`. Use descriptive commits and open a pull request
linked to the issue. Obtain at least one review and passing CI before merging.
Do not push directly to `main` after initialization. Do not commit credentials,
private keys, certificate private material, or local `.env` files.

## Status and milestones

**Current:** The backend `/health` endpoint and its test are implemented.
Gateway protection, database persistence, VM provisioning, and deployment have
not been implemented or verified.

**Week 1 — Foundation:** Add the baseline API, provision the Ubuntu VMs and
private network, and test ModSecurity/CRS and HTTPS separately. The target is
a request reaching the backend through Nginx.

**Week 2 — Security integration:** Integrate WAF and TLS on the gateway,
deploy the backend with systemd, configure firewall policies, and run security
tests. The target is verified HTTPS, legitimate traffic passing, representative
malicious requests triggering WAF rules, and direct backend access restricted.
