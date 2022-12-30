from dataclasses import dataclass

from src.domain.models import Person


@dataclass
class Command:
    pass


@dataclass
class AddPerson(Command):
    new_item: Person


@dataclass
class RemovePerson(Command):
    item_id: int


@dataclass
class GetPeople(Command):
    pass


@dataclass
class GetGoodPeople(Command):
    pass
