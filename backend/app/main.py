from fastapi import FastAPI

app = FastAPI(title="WAF & TLS Hardening API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
