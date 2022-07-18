from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import declarative_base, registry, sessionmaker

from settings import settings

mapper_registry = registry()

db_uri = f'postgresql://{settings.db_user}:{settings.db_password}@{settings.db_url}/{settings.db_name}'

engine = create_async_engine(db_uri, echo=True, future=True)
async_session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
async_db_session = async_scoped_session(async_session_factory, scopefunc=current_task)

Base = declarative_base()
