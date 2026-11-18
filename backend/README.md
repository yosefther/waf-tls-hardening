# Backend

The backend is one FastAPI app. The `api`, `core`, `models`, `schemas`, and
`services` packages are there for future routes, shared settings, database
models, request and response schemas, and application logic. For now, the app
only has `GET /health`.

From `backend/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Check the response with `curl http://127.0.0.1:8000/health`. Run the test with
`python -m pytest -q tests`. If `uvicorn` is not found, activate `.venv` and
install the requirements. The loopback address is for local development.
