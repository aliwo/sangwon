from fastapi import FastAPI

from app.routers.article_router import router as article_router

app = FastAPI()
app.include_router(article_router)
