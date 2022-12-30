from src.domain.commands import GetGoodPeople
from src.entrypoints.kivy.views.good_people_screen.good_people_screen import GoodPeopleScreenView


class GoodPeopleScreenController:
    def __init__(self, bus, main_controller):
        self.bus = bus
        self._view = GoodPeopleScreenView(
            controller=self,
            main_controller=main_controller
        )

    def get_view(self):
        return self._view

    async def fill_good_people_list(self):
        event = await self.bus.handle_command(GetGoodPeople())
        if event:
            self._view.fill_good_people_list(event.good_people)
