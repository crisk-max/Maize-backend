from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Maize Precision API")
app.include_router(router)
