# Network topology

## Planned

```text
Client network -- HTTPS/443 --> Gateway public interface
Gateway private interface -- HTTP/backend port --> Backend private interface
Backend VM -- local PostgreSQL connection --> PostgreSQL
```

The gateway may also accept HTTP/80 solely to redirect clients to HTTPS.
Only the gateway should reach the backend service port. The backend VM should
have no client-facing route to that service. SSH access must be limited to the
lab administration path. Exact subnets, addresses, interfaces, and ports will
be chosen and recorded during INFRA-01, after checking the lab environment.

## Implemented

No VMs, interfaces, routes, firewall policies, or gateway configuration are
included in this repository yet. The local development server binds to
`127.0.0.1:8000` when launched with the README command. This is not evidence
of deployed network isolation.

## Verification required

- From the gateway, connect to the backend service over the private network.
- From the client network, show the backend service port cannot be reached.
- From the client, show HTTPS reaches the gateway and the proxied `/health`.
- Record the topology and command output in the integration test evidence.
