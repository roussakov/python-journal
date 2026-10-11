import os
from typing import AsyncIterator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.sql import text

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_async_engine(os.environ["DATABASE_URL"])

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def verify_connection() -> None:
    async with engine.connect():
        pass

def dispose_connection() -> None:
    engine.dispose()


async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session