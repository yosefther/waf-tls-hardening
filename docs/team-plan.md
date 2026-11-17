# Team plan

Each workstream owns its changes in a separate feature branch and submits a PR.
The backend and integration lead reviews cross-workstream integration; every PR
needs at least one review and passing CI before merge.

| Member | Workstream | Responsibilities | Initial issues |
| --- | --- | --- | --- |
| 1 | Backend and integration lead | FastAPI modular monolith, PostgreSQL, REST API, backend tests, review and integration | SETUP-01, BACK-02 |
| 2 | WAF | Nginx/ModSecurity integration, OWASP CRS, policies, audit logging, detection and blocking tests | WAF-01, WAF-02 |
| 3 | TLS and Linux security | Certificates, HTTPS, TLS 1.2/1.3, redirects, headers, nftables | TLS-01, TLS-02; coordinate firewall work with INFRA-01 |
| 4 | Infrastructure and QA | Ubuntu VMs, private networking, SSH, systemd, setup scripts, end-to-end tests | INFRA-01, INFRA-02, TEST-01 |

No GitHub usernames have been provided, so issues should use workstream labels
and remain unassigned until the team shares usernames.

## Issue order and dependencies

- SETUP-01 and INFRA-01 can start immediately. The `/health` part of SETUP-01
  is present in this initial commit; the issue should verify a fresh clone and
  teammate setup before closure.
- WAF-01 and TLS-01 can start independently in their respective work areas.
- BACK-02 follows SETUP-01. WAF-02 follows WAF-01. TLS-02 follows TLS-01.
- INFRA-02 follows SETUP-01 and INFRA-01.
- TEST-01 follows WAF-02, TLS-02, INFRA-01, and INFRA-02.

The complete issue descriptions and acceptance criteria are in
[issue backlog](issue-backlog.md).

## Learning resources

**Member 1 — Backend:** [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/),
[FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/),
[FastAPI SQL databases](https://fastapi.tiangolo.com/tutorial/sql-databases/),
and [PostgreSQL documentation](https://www.postgresql.org/docs/).

**Member 2 — WAF:** [ModSecurity with Nginx](https://modsecurity.org/docs/2-installation/2-2-libmodsecurity-v3-nginx/index.html),
[OWASP CRS documentation](https://coreruleset.org/docs/), and
[Nginx reverse proxy guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/).

**Member 3 — TLS and Linux security:** [Nginx HTTPS documentation](https://nginx.org/en/docs/http/configuring_https_servers.html),
[Mozilla TLS configuration guidance](https://wiki.mozilla.org/Security/Server_Side_TLS),
[Ubuntu firewall documentation](https://ubuntu.com/server/docs/how-to/security/firewalls/),
and [nftables wiki](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page).

**Member 4 — Infrastructure and QA:** [Ubuntu Server documentation](https://ubuntu.com/server/docs/),
[Ubuntu networking](https://ubuntu.com/server/docs/how-to/networking/),
[systemd service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html),
and [Ansible getting started](https://docs.ansible.com/ansible/latest/getting_started/index.html).

## Milestones

**Week 1:** Build and test the baseline API; provision VMs and private
networking; test WAF and HTTPS independently. Target: a request reaches the
backend through Nginx.

**Week 2:** Integrate WAF and TLS at the gateway, deploy with systemd, apply
firewall policies, and run security verification. Target: HTTPS and normal
traffic work, representative attacks trigger WAF rules, and direct backend
access is restricted.
