from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from .database import async_session

async def get_db() -> Generator:
    async with async_session() as session:
        yield session