from src.bootstrap import bootstrap
from src.entrypoints.kivy.controllers.good_people_screen import GoodPeopleScreenController
from src.entrypoints.kivy.controllers.people_screen import PeopleScreenController
from src.entrypoints.kivy.controllers.root_screen import RootScreenController
from src.entrypoints.kivy.controllers.weclome_screen import WelcomeScreenController

SCREENS = {
    "root screen": RootScreenController,
    "welcome screen": WelcomeScreenController,
    "people screen": PeopleScreenController,
    "good people screen": GoodPeopleScreenController,
}


class ScreenGenerator:
    def __init__(self, screens=SCREENS):
        self.screens = screens
        self.bus = bootstrap()
        self._parent_screen_name = 'root screen'

    def build_app_view(self):
        parent_view = self._generate_view(self._parent_screen_name)
        for key in self.screens.keys():
            if key != self._parent_screen_name:
                parent_view.screen_manager.add_widget(self._generate_view(key, parent_view.controller))
        return parent_view

    def _generate_view(self, key, main_controller=None):
        controller = self.screens[key](self.bus, main_controller)
        view = controller.get_view()
        view.name = key
        return view
