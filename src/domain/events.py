from dataclasses import dataclass
from typing import List

from src.domain.models import Person


@dataclass
class Event:
    pass


@dataclass
class PersonIsAdded(Event):
    new_item: Person


@dataclass
class PersonIsRemoved(Event):
    item_id: int


@dataclass
class GotPeople(Event):
    people: List[Person]


@dataclass
class GotGoodPeople(Event):
    good_people: List[Person]
