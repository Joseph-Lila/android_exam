""" Module adapters.create_db """

import asyncio
import pathlib
from typing import Optional

import aiosqlite
from loguru import logger

from src.config import get_sqlite_connection_str

CREATE_PEOPLE_TABLE = "CREATE TABLE IF NOT EXISTS people (" \
                    "item_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "name TEXT," \
                    "age INTEGER," \
                    "behaviour TEXT" \
                    ");"

CREATE_CONSTRUCTIONS = [
    CREATE_PEOPLE_TABLE,
]


def check_sqlite_connection_right(connection_string: Optional[str] = None):
    """
    Method to check if db_file exists.
    :param connection_string: Optional[str]
    :return: Optional[bool]
    """
    if connection_string == ':memory:' or pathlib.Path(connection_string).exists():
        return True
    return None


async def create_tables(connection_string: Optional[str] = None):
    """
    Method to prepare db file and build tables
    :param connection_string: Optional[str]
    :return: None
    """
    current_connection_str = connection_string or get_sqlite_connection_str()
    if not check_sqlite_connection_right(current_connection_str):
        try:
            logger.info("Trying to create database file...")
            with open(current_connection_str, 'w+') as f:
                pass
            logger.info("Database file is created successfully!")
        except Exception as exception:
            logger.exception(exception)
    async with aiosqlite.connect(current_connection_str) as database:
        for command in CREATE_CONSTRUCTIONS:
            try:
                await database.execute(command)
            except Exception as exception:
                logger.exception(exception)
        await database.commit()
        logger.info("Tables are created!")


if __name__ == "__main__":
    asyncio.run(create_tables())
