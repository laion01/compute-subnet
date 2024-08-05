import logging

from fastapi import FastAPI
import uvicorn

from core.config import settings
from routes.apis import apis_router

# Set up logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(apis_router)

if __name__ == "__main__":
    uvicorn.run("validator:app", host="0.0.0.0", port=8010, reload=True)