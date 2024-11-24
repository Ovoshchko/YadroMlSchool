from fastapi import FastAPI
from routes import molecule_router

app = FastAPI()

app.include_router(molecule_router, prefix="/api/v1", tags=["Molecules"])