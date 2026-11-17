"""Publish the initial labels and issues after GitHub authentication is fixed.

Usage: python3 scripts/publish-issues.py OWNER/waf-tls-hardening
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "backend": "1f6feb",
    "waf": "d73a4a",
    "tls": "8250df",
    "infrastructure": "0e8a16",
    "testing": "fbca04",
    "documentation": "0075ca",
    "integration": "5319e7",
    "bug": "b60205",
    "enhancement": "a2eeef",
    "blocked": "b7b7b7",
}


def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], check=True, text=True, capture_output=True)
    return result.stdout.strip()


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(
        r"[A-Za-z0-9-]+/waf-tls-hardening", sys.argv[1]
    ):
        raise SystemExit(
            "Usage: python3 scripts/publish-issues.py OWNER/waf-tls-hardening"
        )

    repo = sys.argv[1]
    account = gh("api", "user", "--jq", ".login")
    if account.lower() != repo.split("/")[0].lower():
        raise SystemExit(f"Authenticated as {account}; requested owner is {repo}.")
    actual = gh(
        "repo", "view", repo, "--json", "nameWithOwner", "--jq", ".nameWithOwner"
    )
    if actual.lower() != repo.lower():
        raise SystemExit(f"Repository mismatch: {actual}")

    for name, color in LABELS.items():
        gh("label", "create", name, "--repo", repo, "--color", color, "--force")
        print(f"Label: {name}")

    existing = {
        issue["title"]
        for issue in json.loads(
            gh(
                "issue",
                "list",
                "--repo",
                repo,
                "--state",
                "all",
                "--limit",
                "1000",
                "--json",
                "title",
            )
        )
    }
    backlog = (ROOT / "docs" / "issue-backlog.md").read_text()
    sections = re.split(r"(?=^## [A-Z]+-\d+ — )", backlog, flags=re.MULTILINE)
    for section in sections[1:]:
        title, body = section.split("\n", 1)
        title = title.removeprefix("## ").strip()
        if title in existing:
            print(f"Already exists: {title}")
            continue
        labels = re.search(r"\*\*Labels:\*\* (.+)", body)
        if labels is None:
            raise SystemExit(f"Missing labels: {title}")
        names = re.findall(r"`([^`]+)`", labels.group(1))
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md") as issue_file:
            issue_file.write(body.strip() + "\n")
            issue_file.flush()
            url = gh(
                "issue",
                "create",
                "--repo",
                repo,
                "--title",
                title,
                "--body-file",
                issue_file.name,
                "--label",
                ",".join(names),
            )
        print(f"Created: {url}")


if __name__ == "__main__":
    main()
