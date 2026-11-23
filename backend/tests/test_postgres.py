import os
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

from app.core.database import get_engine
from app.main import create_app


def test_postgresql_migration_and_restart(monkeypatch: pytest.MonkeyPatch) -> None:
    url = os.getenv("TEST_DATABASE_URL")
    if not url:
        pytest.skip("Set TEST_DATABASE_URL to run the PostgreSQL integration test")
    monkeypatch.setenv("DATABASE_URL", url)
    monkeypatch.setenv("API_TOKEN", "test-postgres-secret")
    command.upgrade(Config("alembic.ini"), "head")
    headers = {"Authorization": "Bearer test-postgres-secret"}
    name = f"restart-check-{uuid4()}"

    with TestClient(create_app()) as client:
        response = client.post("/items", headers=headers, json={"name": name})
        assert response.status_code == 201
        item_id = response.json()["id"]

    get_engine(url).dispose()
    get_engine.cache_clear()
    with TestClient(create_app()) as client:
        response = client.get(f"/items/{item_id}", headers=headers)
        assert response.status_code == 200
        assert response.json()["name"] == name
        assert client.delete(f"/items/{item_id}", headers=headers).status_code == 204
