# Deployment notes

The backend can run locally, but VM deployment is not configured. The planned
files will go under `infrastructure/networking/`, `infrastructure/systemd/`,
`infrastructure/nftables/`, and `gateway/`. No systemd unit or Nginx
configuration is present yet.

## Local backend check

From `backend/`, install dependencies and start the server using the
[backend README](../backend/README.md). In a second terminal, run:

```bash
curl --fail-with-body http://127.0.0.1:8000/health
```

The response should be `{"status":"ok"}`. A connection error usually means
the server is not running or is listening on a different port.

## VM deployment work

INFRA-01 will document Ubuntu VM setup, private addresses, and SSH access in
[network topology](network-topology.md). INFRA-02 will add a dedicated service
account and systemd unit, then document install, start, restart, reboot, and
`journalctl` checks. WAF-01 and TLS-01 will add gateway configuration. VM
commands will be added when the VM addresses and service files exist.
