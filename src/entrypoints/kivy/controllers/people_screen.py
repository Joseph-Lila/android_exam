import asyncio

from src.domain.commands import GetPeople, RemovePerson, AddPerson
from src.entrypoints.kivy.views.people_screen.people_screen import PeopleScreenView


class PeopleScreenController:
    def __init__(self, bus, main_controller):
        self.bus = bus
        self._view = PeopleScreenView(
            controller=self,
            main_controller=main_controller
        )

    def get_view(self):
        return self._view

    def send_add_person_command(self, person):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            loop.create_task(self.add_person(person))

    async def send_remove_person_command(self, person):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            loop.create_task(self.remove_person(person))

    def send_fill_people_list_command(self):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            loop.create_task(self.fill_people_list())

    async def fill_people_list(self):
        event = await self.bus.handle_command(GetPeople())
        if event:
            self._view.fill_people_list(event.people)

    async def remove_person(self, item_id):
        event = await self.bus.handle_command(RemovePerson(item_id))
        if event:
            self._view.remove_person(event.item_id)

    async def add_person(self, person):
        event = await self.bus.handle_command(AddPerson(person))
        if event:
            self._view.add_person(event.new_item)
