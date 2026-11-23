from fastapi import FastAPI

from app.api.items import router as items_router


def create_app() -> FastAPI:
    application = FastAPI(title="WAF & TLS Hardening API")
    application.include_router(items_router)

    @application.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()
