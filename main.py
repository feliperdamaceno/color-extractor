from fastapi import FastAPI

from api.routers.extract import router as extract_router

app = FastAPI()

app.include_router(extract_router)


@app.get("/")
async def root():
    return {"message": "Server is running."}
