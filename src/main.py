from fastapi import FastAPI
from dotenv import load_dotenv

from src.routers.collections import router as collections_router
from src.routers.chat import router as chat_router

# TODO: Replace with pydantic settings?
load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(collections_router)
app.include_router(chat_router)
