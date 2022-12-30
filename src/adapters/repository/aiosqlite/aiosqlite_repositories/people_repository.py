from typing import List, Optional

from src.adapters.repository.abstract_repository import AbstractRepository
from src.domain import models
from src.domain.models import Person


class PeopleRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    async def get_all(self) -> List[models.Person]:
        items = []
        async with self.session.execute(
                "SELECT * FROM people;"
        ) as cursor:
            async for row in cursor:
                items.append(Person(*row))
        return items

    async def get_by_id(self, item_id: int) -> Optional[models.Person]:
        cursor = await self.session.execute(
            "SELECT * "
            "FROM people "
            "WHERE item_id = ?;",
            (item_id,)
        )
        row = await cursor.fetchone()
        await cursor.close()
        if row is None:
            return None
        return Person(*row)

    async def update(self, item):
        await self.session.execute(
            "UPDATE people "
            "SET name = ?,"
            "age = ?,"
            "behaviour = ? "
            "WHERE item_id = ?;",
            (item.name, item.age, item.behaviour, item.item_id)
        )

    async def delete(self, item_id: int):
        await self.session.execute(
            "DELETE FROM people "
            "WHERE item_id = ?;",
            (item_id,)
        )

    async def create(self, item):
        await self.session.execute(
            "INSERT INTO people "
            "(name, age, behaviour) "
            "values (?, ?, ?);",
            (item.name, item.age, item.behaviour)
        )
