from fastapi import FastAPI
from routes.car import car

app = FastAPI(
    title="Cars API",
    description="a REST API using python and mysql",
    version="0.0.1"
)

app.include_router(car)