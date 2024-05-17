from fastapi import FastAPI
from app.routers import prop

app = FastAPI()

app.include_router(prop.rt)

@app.get("/")
def index():
    return "Welcome to the Property Management API"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
