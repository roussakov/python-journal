from contextlib import asynccontextmanager
from fastapi import FastAPI

from python_journal import db
from python_journal.routes import entry

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Fail fast if unable to connect to DB
        await db.verify_connection()
        yield
    finally:
        db.dispose_connection()


app = FastAPI(lifespan=lifespan)

app.include_router(entry.router)

