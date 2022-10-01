from fastapi import FastAPI

from fastapi_starter.routers import health
from logger import logger

logger.info("Booting up FastAPI")


app = FastAPI()
app.include_router(health.router)
