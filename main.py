from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.extract import router as extract_router

app = FastAPI()

CORS_ALLOWED_ORIGINS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(extract_router)


@app.get("/")
async def root():
    return {"message": "Server is running"}
