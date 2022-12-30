from dataclasses import dataclass
from enum import Enum


class Behaviour(Enum):
    GOOD = 'GOOD'
    WRONG = 'WRONG'


@dataclass
class BaseEntity:
    """ BaseEntity implementation """
    item_id: int = 0


@dataclass
class Person(BaseEntity):
    name: str = 'Unknown'
    age: int = 0
    behaviour: str = 'Unknown'
