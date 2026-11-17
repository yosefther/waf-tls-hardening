# Deployment plan

Deployment is not implemented. INFRA-01 will document VM images, interfaces,
addresses, SSH access, and the private network. INFRA-02 will add a dedicated
service account, a systemd unit, startup verification after reboot, and
`journalctl` instructions. WAF-01 and TLS-01 will supply gateway configuration
through separate pull requests. No production commands should be inferred
from the local `uvicorn --reload` development command.
