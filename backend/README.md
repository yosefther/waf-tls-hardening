# Backend

The backend is a small FastAPI modular monolith. `app/api` will hold routes,
`app/core` shared settings, `app/models` persistence models, `app/schemas`
request and response models, and `app/services` application logic. These are
placeholders for future work; only `/health` is implemented.

From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

In a second terminal, run `curl http://127.0.0.1:8000/health`.
Run tests with `python -m pytest -q tests` from this directory.
The loopback bind above is for local development. Production networking and
service binding will be defined and verified in the infrastructure workstream.
