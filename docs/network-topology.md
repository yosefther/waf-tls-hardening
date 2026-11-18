# Network topology

## Planned layout

```text
Client network -> HTTPS/443 -> Gateway public interface
Gateway private interface -> HTTP/backend port -> Backend private interface
Backend VM -> local connection -> PostgreSQL
```

The gateway may accept HTTP/80 to redirect clients to HTTPS. Only the gateway
should reach the backend service port. SSH access should use the lab
administration path. INFRA-01 will record the actual VM addresses, interfaces,
ports, and firewall rules here after provisioning.

## Current state

There are no VM, route, or firewall configuration files yet. The development
server listens on `127.0.0.1:8000` when started with the README command. This
does not test isolation between VMs.

## Checks after provisioning

1. From the gateway, request the backend `/health` endpoint on its private
   address. Record the command and response.
2. From the client network, try the same backend address and port. Record the
   connection failure and the relevant firewall rule.
3. From the client, request the gateway `/health` endpoint over HTTPS. Record
   certificate validation and the response.

These checks require the addresses and certificates from INFRA-01 and TLS-01.
See [testing](testing.md) for the test evidence format.
