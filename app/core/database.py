from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    AsyncAttrs,
    create_async_engine,
)
from sqlalchemy.schema import MetaData
from sqlalchemy.pool import NullPool

from app.core.settings import settings

async_engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URI,
    future=True,
    **(
        {"poolclass": NullPool}
        if settings.IS_TEST_ENVIRONMENT
        else {"pool_size": 20, "max_overflow": 30}
    )
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


meta_data = MetaData()

SessionLocal = sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=True,
    class_=AsyncSession,
)


async def get_db() -> AsyncSession:
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
