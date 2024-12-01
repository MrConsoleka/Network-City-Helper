import os, logging
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from source.misc import db_url
from source.models import Base, User
from sqlalchemy import select, update, null, case, column

logger = logging.getLogger(__name__)

engine = create_async_engine(db_url())

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        try:

            await conn.run_sync(Base.metadata.create_all)

        except Exception as e:
            logger.error(f"error {e}")


async def drop_db():
    async with engine.begin() as conn:
        try:

            await conn.run_sync(Base.metadata.drop_all)

        except Exception as e:
            logger.error(f"error {e}")


async def set_user(tg_id):
    async with async_session() as session:
        try:

            user = await session.scalar(select(User).where(User.user_id == tg_id))

            if not user:
                session.add(User(user_id=tg_id))
                await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def update_privacy(tg_id):
    async with async_session() as session:
        try:

            cmt = (
                update(User)
                .values(privacy_policy=True)
                .filter_by(user_id=tg_id)
            )

            await session.execute(cmt)
            await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def update_auth(tg_id, login, password, role, name, surname, clas):
    async with async_session() as session:
        try:

            if isinstance(role, list) and len(role) > 0:
                role = role[0]

            role = role.lower()

            cmt = (
                update(User)
                .values(login=login, password=password, role=role, name=name, surname=surname, clas=clas)
                .filter_by(user_id=tg_id)
            )

            await session.execute(cmt)
            await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def update_url(tg_id, url, token):
    async with async_session() as session:
        try:

            cmt = (
                update(User)
                .values(url_aiograph=url, token_aiograph=token)
                .filter_by(user_id=tg_id)
            )

            await session.execute(cmt)
            await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def clear_user(tg_id):
    async with async_session() as session:
        try:

            cmt = (
                update(User)
                .values(role="unauth", login=null(), password=null(), name=null(), surname=null(), clas=null(), notice_timetable=0, notice_announcement=0, notice_overdue_assigment=0, url_aiograph=null(), token_aiograph=null())
                .filter_by(user_id=tg_id)
            )

            await session.execute(cmt)
            await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def update_notice(tg_id, column_id):
    async with async_session() as session:
        try:

            cmt = (
                update(User)
                .where(User.user_id == tg_id)
                .values({
                    column(column_id): case(
                        (column(column_id) == True, False),  # Если значение true, делаем false
                        else_=True  # В противном случае делаем true
                    )
                })
            )

            await session.execute(cmt)
            await session.commit()

        except Exception as e:
            logger.error(f"error {e}")


async def get_user(tg_id):
    async with async_session() as session:
        try:

            user = await session.scalar(select(User).where(User.user_id == tg_id))

            await session.commit()

            return user

        except Exception as e:
            logger.error(f"error {e}")


async def get_notice_users(column_id):
    async with async_session() as session:
        try:

            user = await session.scalars(select(User.user_id).where(column(column_id) == True))

            await session.commit()

            return user

        except Exception as e:
            logger.error(f"error {e}")