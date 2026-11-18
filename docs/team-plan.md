# Team plan

| Member | Responsibilities | Issues |
| --- | --- | --- |
| 1, backend and integration lead | FastAPI, PostgreSQL, backend tests, code review, integration | [SETUP-01](https://github.com/yosefther/waf-tls-hardening/issues/1), [BACK-02](https://github.com/yosefther/waf-tls-hardening/issues/2) |
| 2, WAF | ModSecurity, OWASP CRS, WAF policies, audit logs, blocking tests | [WAF-01](https://github.com/yosefther/waf-tls-hardening/issues/3), [WAF-02](https://github.com/yosefther/waf-tls-hardening/issues/4) |
| 3, TLS and Linux security | HTTPS, certificates, TLS settings, security headers, nftables | [TLS-01](https://github.com/yosefther/waf-tls-hardening/issues/5), [TLS-02](https://github.com/yosefther/waf-tls-hardening/issues/6) |
| 4, infrastructure and QA | Ubuntu VMs, networking, SSH, systemd, setup scripts, integration tests | [INFRA-01](https://github.com/yosefther/waf-tls-hardening/issues/7), [INFRA-02](https://github.com/yosefther/waf-tls-hardening/issues/8), [TEST-01](https://github.com/yosefther/waf-tls-hardening/issues/9) |

Member 3 owns nftables policy. Member 4 owns VM networking and coordinates
firewall deployment with Member 3. Issues use workstream labels because GitHub
usernames have not been provided.

## Dependencies

- BACK-02 follows SETUP-01.
- WAF-02 follows WAF-01. TLS-02 follows TLS-01.
- WAF-01 and TLS-01 need INFRA-01 for gateway deployment, but lab tests can
  start earlier.
- INFRA-02 follows SETUP-01 and INFRA-01.
- TEST-01 follows WAF-02, TLS-02, INFRA-01, and INFRA-02.

The initial commit includes `/health` and its test. SETUP-01 remains open for
a fresh-clone check by another team member.

## Schedule

| Week | Work | Target |
| --- | --- | --- |
| 1 | Baseline API, Ubuntu VMs and private network, separate WAF and HTTPS tests | A request reaches the backend through Nginx |
| 2 | Gateway integration, systemd, firewall policy, integration tests | HTTPS works, expected traffic passes, selected attacks trigger WAF rules, direct backend access is restricted |

## Reading

| Member | Documentation |
| --- | --- |
| 1 | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/), [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/), [PostgreSQL](https://www.postgresql.org/docs/) |
| 2 | [ModSecurity with Nginx](https://modsecurity.org/docs/2-installation/2-2-libmodsecurity-v3-nginx/index.html), [OWASP CRS](https://coreruleset.org/docs/) |
| 3 | [Nginx HTTPS](https://nginx.org/en/docs/http/configuring_https_servers.html), [nftables](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page) |
| 4 | [Ubuntu Server](https://ubuntu.com/server/docs/), [Ubuntu networking](https://ubuntu.com/server/docs/how-to/networking/), [systemd service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) |

Open a branch for each issue. Submit a PR, wait for one teammate review and
passing CI, then merge. Use short commit messages that name the change.
