from fastapi import FastAPI

from app.routers.article_router import router as article_router
from app.routers.health import router as health_router

app = FastAPI()
app.include_router(article_router)
app.include_router(health_router)
