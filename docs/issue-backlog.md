# Initial GitHub issue backlog

These issue definitions are ready for publication when GitHub authentication
works. The identifier is part of each title. Workstream labels identify the
owner; no GitHub user should be assigned without a supplied username.

## SETUP-01 — Create repository and baseline API

**Workstream:** Backend<br>
**Labels:** `backend`, `enhancement`, `documentation`, `integration`<br>
**Dependencies:** None.

**Description:** Initialize FastAPI, implement `GET /health`, add basic tests,
and document how to run the application. The initial commit supplies a starting
implementation; verify it from a fresh clone and improve it if needed.

**Acceptance criteria:**
- [ ] A teammate can clone the repository and install backend dependencies.
- [ ] The teammate can start the backend and successfully call `/health`.
- [ ] Backend tests pass and startup steps are documented.

## BACK-02 — Implement application endpoints and PostgreSQL

**Workstream:** Backend<br>
**Labels:** `backend`, `enhancement`<br>
**Dependencies:** SETUP-01.

**Description:** Build a small authenticated CRUD API with PostgreSQL
persistence, database migrations, and automated tests.

**Acceptance criteria:**
- [ ] Authenticated CRUD endpoints work.
- [ ] Data persists in PostgreSQL across application restarts.
- [ ] Migrations and automated tests pass and are documented.

## WAF-01 — Install and configure ModSecurity + OWASP CRS

**Workstream:** WAF<br>
**Labels:** `waf`, `enhancement`<br>
**Dependencies:** INFRA-01 for deployment; independent lab testing may start earlier.

**Description:** Configure a compatible Nginx and ModSecurity integration and
enable OWASP CRS in detection-only mode. Document versions and audit log path.

**Acceptance criteria:**
- [ ] ModSecurity and CRS load successfully with Nginx.
- [ ] A controlled suspicious request appears in the WAF audit log with a rule ID.
- [ ] Detection-only behavior is demonstrated and documented.

## WAF-02 — Enable and verify WAF blocking

**Workstream:** WAF<br>
**Labels:** `waf`, `testing`, `enhancement`<br>
**Dependencies:** WAF-01.

**Description:** Tune the WAF configuration and enable blocking for
representative test requests. Record any rule exclusions and reasons.

**Acceptance criteria:**
- [ ] Normal requests succeed through the gateway.
- [ ] Selected malicious test requests are blocked.
- [ ] Blocked requests appear in audit logs with matching rule IDs.

## TLS-01 — Configure HTTPS on gateway

**Workstream:** TLS<br>
**Labels:** `tls`, `enhancement`, `documentation`<br>
**Dependencies:** INFRA-01 for deployment; independent lab testing may start earlier.

**Description:** Configure Nginx HTTPS with certificates signed by a local
test CA and add HTTP-to-HTTPS redirects. Keep CA private keys out of Git.

**Acceptance criteria:**
- [ ] `curl` verifies HTTPS using the test CA certificate.
- [ ] HTTP requests redirect to HTTPS.
- [ ] Certificate generation and local trust steps are documented without secrets.

## TLS-02 — Harden TLS configuration

**Workstream:** TLS<br>
**Labels:** `tls`, `testing`, `enhancement`<br>
**Dependencies:** TLS-01.

**Description:** Configure TLS 1.2/1.3, appropriate cipher settings, and
secure HTTP response headers. Test protocol compatibility.

**Acceptance criteria:**
- [ ] Modern TLS connections succeed.
- [ ] Obsolete TLS versions are rejected.
- [ ] Protocol, cipher, and header test results are documented.

## INFRA-01 — Provision Ubuntu lab

**Workstream:** Infrastructure<br>
**Labels:** `infrastructure`, `documentation`, `enhancement`<br>
**Dependencies:** None.

**Description:** Create Ubuntu gateway and backend VMs with private networking,
SSH access, and a documented network topology. Coordinate nftables policy
with the TLS and Linux security engineer.

**Acceptance criteria:**
- [ ] The gateway can reach the backend over the private network.
- [ ] Clients cannot connect directly to the backend service.
- [ ] Network addresses, interfaces, SSH path, and evidence are documented.

## INFRA-02 — Deploy backend as systemd service

**Workstream:** Infrastructure<br>
**Labels:** `infrastructure`, `integration`, `documentation`<br>
**Dependencies:** SETUP-01 and INFRA-01.

**Description:** Create a dedicated Linux service account, configure the
systemd unit, and document deployment and operations.

**Acceptance criteria:**
- [ ] The application runs under the dedicated account as a systemd service.
- [ ] The service starts after reboot.
- [ ] Logs are accessible through `journalctl` and steps are documented.

## TEST-01 — Implement end-to-end verification

**Workstream:** Infrastructure/QA<br>
**Labels:** `testing`, `integration`, `infrastructure`, `documentation`<br>
**Dependencies:** WAF-02, TLS-02, INFRA-01, and INFRA-02.

**Description:** Create repeatable tests for HTTPS functionality, TLS protocol
restrictions, WAF detection and blocking, reverse proxy functionality, and
backend network isolation.

**Acceptance criteria:**
- [ ] A documented test suite produces PASS/FAIL for each security behavior.
- [ ] Results include sanitized command output or logs as evidence.
- [ ] A teammate can reproduce the test run in the lab.
