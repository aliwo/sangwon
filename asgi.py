from app.main import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


"gunicorn asgi:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001"
