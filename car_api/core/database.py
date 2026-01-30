from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from car_api.core.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)