""" Module src.adapters.sqlite_repositories.abstract_repository """
import abc
from typing import List

from src.domain import models


class AbstractRepository(abc.ABC):
    """ Abstract repository structure """
    @abc.abstractmethod
    async def get_all(self) -> List[models.Person]:
        """
        Abstract method to get list of objects.
        :return: List[models.Person]
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_id(self, item_id: int) -> models.Person:
        """
        Abstract method to get object by id.
        :param item_id: int
        :return: models.Person
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, item):
        """
        Abstract method to update object.
        :param item: models.Person.
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, item_id: int):
        """
        Abstract method to delete object.
        :param item_id: int
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, item):
        """
        Abstract method to create new object.
        :param item: models.Person
        :return: None
        """
        raise NotImplementedError
