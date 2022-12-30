import asyncio
from typing import List

from kivy.properties import ObjectProperty
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.screen import MDScreen

from src.domain.models import Person


class GoodPeopleScreenView(MDScreen):
    main_controller = ObjectProperty()
    controller = ObjectProperty()

    def on_enter(self, *args):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            loop.create_task(self.controller.fill_good_people_list())

    def fill_good_people_list(self, good_people: List[Person]):
        self.container.clear_widgets()
        for good_person in good_people:
            new_person = self._get_person_list_item(good_person)
            self.container.add_widget(new_person)

    @staticmethod
    def _get_person_list_item(person: Person):
        two_line_avatar_icon_list_item = TwoLineAvatarIconListItem(
            theme_text_color='Custom',
            secondary_theme_text_color='Custom',
            text_color=[1, 0, 0, 1],
            secondary_text_color=[0, 1, 0, 1],
            text=f"{person.name}, {person.age}",
            secondary_text=f"{person.behaviour} PERSON"
        )
        icon_left_widget = IconLeftWidget(icon='gift-outline')
        icon_right_widget = IconRightWidget(icon='truck-snowflake')
        two_line_avatar_icon_list_item.add_widget(icon_left_widget)
        two_line_avatar_icon_list_item.add_widget(icon_right_widget)
        return two_line_avatar_icon_list_item
