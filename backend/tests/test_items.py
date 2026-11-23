from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    monkeypatch.setenv("API_TOKEN", "test-secret")
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    def test_db() -> Iterator[Session]:
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_db] = test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    engine.dispose()


def test_authentication_is_required(client: TestClient) -> None:
    assert client.get("/items").status_code == 401
    assert (
        client.get("/items", headers={"Authorization": "Bearer wrong"}).status_code
        == 401
    )
    assert client.get("/health").status_code == 200


def test_missing_token_configuration_returns_503(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("API_TOKEN")
    assert client.get("/items").status_code == 503


def test_crud_and_validation(client: TestClient) -> None:
    headers = {"Authorization": "Bearer test-secret"}
    assert client.post("/items", headers=headers, json={"name": ""}).status_code == 422

    created = client.post(
        "/items", headers=headers, json={"name": "Example", "description": "first"}
    )
    assert created.status_code == 201
    item = created.json()
    assert item["name"] == "Example"
    assert item["description"] == "first"
    assert item["created_at"]
    item_id = item["id"]

    assert client.get(f"/items/{item_id}", headers=headers).json() == item
    assert client.get("/items", headers=headers).json() == [item]

    updated = client.patch(
        f"/items/{item_id}", headers=headers, json={"description": None}
    )
    assert updated.status_code == 200
    assert updated.json()["description"] is None
    assert updated.json()["name"] == "Example"
    assert (
        client.patch(
            f"/items/{item_id}", headers=headers, json={"name": None}
        ).status_code
        == 422
    )

    assert client.delete(f"/items/{item_id}", headers=headers).status_code == 204
    assert client.get(f"/items/{item_id}", headers=headers).status_code == 404
    assert client.delete(f"/items/{item_id}", headers=headers).status_code == 404
