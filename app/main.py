from fastapi import FastAPI
from .routers import prop

app = FastAPI()

app.include_router(prop.rt)

@app.get("/")
def index():
    return "Welcome to the Property Management API"
