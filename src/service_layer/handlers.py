import functools
from typing import Callable, Dict, Type

from loguru import logger

from src.domain import commands, events
from src.domain.models import Behaviour
from src.service_layer.unit_of_work.abstract_unit_of_work import \
    AbstractUnitOfWork


def my_logger_decorator():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(
                cmd: commands.Command,
                uow: AbstractUnitOfWork,
        ):
            logger.info(f'Handling {cmd} command...')
            return await func(cmd, uow)
        return wrapped
    return wrapper


@my_logger_decorator()
async def add_person(
        cmd: commands.AddPerson,
        uow: AbstractUnitOfWork,
):
    async with uow:
        await uow.people.create(cmd.new_item)
        await uow.commit()
    return events.PersonIsAdded(cmd.new_item)


@my_logger_decorator()
async def remove_person(
        cmd: commands.RemovePerson,
        uow: AbstractUnitOfWork,
):
    async with uow:
        await uow.people.delete(cmd.item_id)
        await uow.commit()
    return events.PersonIsRemoved(cmd.item_id)


@my_logger_decorator()
async def get_people(
        cmd: commands.GetPeople,
        uow: AbstractUnitOfWork,
):
    async with uow:
        people = await uow.people.get_all()
    return events.GotPeople(people)


@my_logger_decorator()
async def get_good_people(
        cmd: commands.RemovePerson,
        uow: AbstractUnitOfWork,
):
    async with uow:
        people = await uow.people.get_all()
    good_people = [person for person in people if person.behaviour == Behaviour.GOOD.value]
    return events.GotGoodPeople(good_people)


COMMAND_HANDLERS = {
    commands.AddPerson: add_person,
    commands.RemovePerson: remove_person,
    commands.GetPeople: get_people,
    commands.GetGoodPeople: get_good_people,
}  # type: Dict[Type[commands.Command], Callable]
