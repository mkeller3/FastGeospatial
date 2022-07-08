from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from routers import analysis
import db

DESCRIPTION = """
A lightweight python api to perform geospatial analysis from PostGIS.
"""

app = FastAPI(
    title="FastVector",
    description=DESCRIPTION,
    version="0.0.1",
    contact={
        "name": "Michael Keller",
        "email": "michaelkeller03@gmail.com",
    },
    license_info={
        "name": "The MIT License (MIT)",
        "url": "https://mit-license.org/",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    analysis.router,
    prefix="/api/v1/analysis",
    tags=["analysis"],
)

@app.on_event("startup")
async def startup_event():
    """Application startup: register the database connection and create table list."""
    await db.connect_to_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown: de-register the database connection."""
    await db.close_db_connection(app)

Instrumentator().instrument(app).expose(app)
