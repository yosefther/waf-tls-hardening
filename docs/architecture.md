# Architecture

## Planned deployment

```text
Client / Browser
       | HTTPS
Ubuntu Gateway VM
  Nginx -> ModSecurity + OWASP CRS
  TLS 1.2 / 1.3; nftables
       | HTTP over private network
Ubuntu Backend VM
  FastAPI modular monolith via systemd
  PostgreSQL on the same VM
```

Nginx is the only planned client-facing entry point. The backend listens only
on the private side of the lab network, and network rules must prevent client
connections to its service port. The gateway-to-backend hop is planned as HTTP
on an isolated private network. The team must verify that isolation before
claiming the deployment is secure.

The application has one process and one deployable backend. The `api`, `core`,
`models`, `schemas`, and `services` packages keep responsibilities separate
without splitting them into services. PostgreSQL starts on the backend VM.

## Implemented today

Only a local FastAPI `/health` route and its unit test exist. There are no
gateway, firewall, database, or deployment configuration files yet.
