# Backend

The backend is a FastAPI modular monolith. `app/api`, `app/core`, `app/models`,
`app/schemas`, and `app/services` are packages reserved for routes, shared
settings, persistence models, request and response schemas, and application
logic. Only `GET /health` is implemented.

From `backend/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Check the response with `curl http://127.0.0.1:8000/health`. Run the test with
`python -m pytest -q tests`. If `uvicorn` is not found, activate `.venv` and
install the requirements. The loopback address is for local development; VM
networking and the systemd service are planned work.
