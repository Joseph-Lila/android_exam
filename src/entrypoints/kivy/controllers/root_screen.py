from src.entrypoints.kivy.views.root_screen.root_screen import RootScreenView


class RootScreenController:
    def __init__(self, bus, *args, **kwargs):
        self.bus = bus
        self._view = RootScreenView(
            controller=self
        )

    def get_view(self):
        return self._view

    def go_to_people_screen(self):
        self._view.screen_manager.current = 'people screen'

    def go_to_welcome_screen(self):
        self._view.screen_manager.current = 'welcome screen'

    def go_to_good_people_screen(self):
        self._view.screen_manager.current = 'good people screen'
