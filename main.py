from fastapi import FastAPI

from routers.routers import routers

app = FastAPI()

app.include_router(routers)