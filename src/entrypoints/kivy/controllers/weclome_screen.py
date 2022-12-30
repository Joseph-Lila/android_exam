from src.entrypoints.kivy.views.welcome_screen.welcome_screen import WelcomeScreenView


class WelcomeScreenController:
    def __init__(self, bus, main_controller):
        self.bus = bus
        self._view = WelcomeScreenView(
            controller=self,
            main_controller=main_controller
        )

    def get_view(self):
        return self._view

    def open_sources_menu(self):
        self._view.sources_menu.open()

