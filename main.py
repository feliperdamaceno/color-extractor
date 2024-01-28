from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.routers.extract import router as extract_router

app = FastAPI()

CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(prefix="/api", router=extract_router)


@app.get("/api")
async def api():
    return {"message": "API is running"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
