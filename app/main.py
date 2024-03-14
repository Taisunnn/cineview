from fastapi import FastAPI

from app.core.middleware import log_request_time
import app.api as v1


app = FastAPI()

app.middleware("http")(log_request_time)


@app.get("/health")
async def healthcheck():
    return {"status": "healthy"}


app.include_router(v1.router)
