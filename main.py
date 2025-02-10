from fastapi import FastAPI
import logging
import logging.config
from app.routers.v1.category_routes import router as category_router
app = FastAPI()

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app.include_router(router=category_router, prefix="/v1/category",tags=["categories"])