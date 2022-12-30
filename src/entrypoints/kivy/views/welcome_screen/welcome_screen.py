from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


class WelcomeScreenView(MDScreen):
    main_controller = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sources_menu = None
        self._init_drop_down_sources_menu()

    def _change_sources_button_text(self, text):
        self.sources.text = text

    def _init_drop_down_sources_menu(self):
        sources_menu_items = [
            {
                "text": "SQLite",
                "viewclass": "OneLineListItem",
                "on_release": lambda x='SQLite': self._change_sources_button_text(x),
            },
            {
                "text": "CSV",
                "viewclass": "OneLineListItem",
                "on_release": lambda x='CSV': self._change_sources_button_text(x),
            }
        ]
        self.sources_menu = MDDropdownMenu(
            caller=self.sources,
            items=sources_menu_items,
            radius=[24, 0, 24, 0],
            background_color='purple',
            width_mult=2,
        )
