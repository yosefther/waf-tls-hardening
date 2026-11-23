# Backend

Python 3.12 or newer is required. From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

`curl http://127.0.0.1:8000/health` returns `{"status":"ok"}` without a
database. Use the loopback address for local development; VM deployment must
bind to its private backend interface and restrict access to the gateway.

## PostgreSQL and authentication

Install PostgreSQL, then create a dedicated local database and login. For
example, in `psql` as a PostgreSQL administrator:

```sql
CREATE ROLE waf_api LOGIN PASSWORD 'replace-this-password';
CREATE DATABASE waf_api OWNER waf_api;
```

Set the connection URL and a long random bearer token in your shell or the
service environment. Replace the sample values; do not commit real secrets.

```bash
export DATABASE_URL='postgresql+psycopg://waf_api:replace-this-password@127.0.0.1:5432/waf_api'
export API_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
alembic upgrade head
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Run `alembic upgrade head` before starting a new deployment. The migration
creates the `items` table. Data stays in PostgreSQL when the API restarts.
The API never creates or changes tables at startup. `/health` checks only the
web process; it does not check PostgreSQL.

All `/items` routes require `Authorization: Bearer <API_TOKEN>`:

| Method | Path | Action |
| --- | --- | --- |
| POST | `/items` | Create an item with `name` and optional `description` |
| GET | `/items` | List items in ID order |
| GET | `/items/{id}` | Read one item |
| PATCH | `/items/{id}` | Change `name` or `description` |
| DELETE | `/items/{id}` | Delete one item |

For example:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Authorization: Bearer $API_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Example","description":"A sample item"}'
curl -H "Authorization: Bearer $API_TOKEN" http://127.0.0.1:8000/items
```

The token is a shared service credential for this project, not per-user
identity. Keep it out of URLs and logs. The gateway must enforce HTTPS before
clients use the API.

## Tests

```bash
python -m pytest -q tests
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

The API tests use an in-memory SQLite database. To run the PostgreSQL migration
and persistence test, create a separate disposable test database and set
`TEST_DATABASE_URL` to its `postgresql+psycopg://` URL before running pytest.
CI provisions PostgreSQL and runs this test on every push and pull request.
