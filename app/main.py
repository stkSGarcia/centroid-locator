from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, server

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(server.router)
