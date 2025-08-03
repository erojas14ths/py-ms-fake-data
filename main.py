import uvicorn

from fastapi import FastAPI
from src.router.main_router import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    # In local development, this will run the Uvicorn server
    uvicorn.run("main:app", port=8080, log_level="info")