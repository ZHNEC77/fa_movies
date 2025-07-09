from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from models import db_helper
from api import build_jsonapi_app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    builder = build_jsonapi_app(app)
    builder.initialize()
    yield
    await db_helper.dispose()
