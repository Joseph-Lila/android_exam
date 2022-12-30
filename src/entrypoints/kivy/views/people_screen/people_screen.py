from typing import List
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineAvatarIconListItem, IconRightWidget
from kivymd.uix.screen import MDScreen

from src.domain.models import Person


class PeopleScreenView(MDScreen):
    main_controller = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_person_popup_content_cls = None

    def on_enter(self, *args):
        self.controller.send_fill_people_list_command()

    def fill_people_list(self, people: List[Person]):
        self.container.clear_widgets()
        for person in people:
            new_person = self._get_person_list_item(person)
            self.container.add_widget(new_person)

    def remove_person(self, item_id):
        person_to_del = None
        for i in range(len(self.container.children)):
            if self.container.children[i].item_id == item_id:
                person_to_del = self.container.children[i]
                break
        if person_to_del:
            self.container.remove_widget(person_to_del)

    def add_person(self, person: Person):
        new_person = self._get_person_list_item(person)
        self.container.add_widget(new_person)

    def _get_person_list_item(self, person: Person):
        two_line_avatar_icon_list_item = TwoLineAvatarIconListItem(
            theme_text_color='Custom',
            secondary_theme_text_color='Custom',
            text_color=[1, 0, 0, 1],
            secondary_text_color=[0, 1, 0, 1] if person.behaviour == 'GOOD' else [1, 0, 0, 1],
            text=f"{person.name}, {person.age}",
            secondary_text=f"{person.behaviour} PERSON"
        )
        icon_right_widget = Factory.RemovePersonRightIconWidget()
        icon_right_widget.controller = self.controller
        two_line_avatar_icon_list_item.add_widget(icon_right_widget)
        two_line_avatar_icon_list_item.item_id = person.item_id
        return two_line_avatar_icon_list_item

    def open_add_person_popup(self, *args):
        self.add_person_popup_content_cls = Factory.DialogAddPerson()
        buttons = Factory.OKButton(on_release=self._prepare_person_to_adding)
        MDDialog(
            title='Add person',
            type='custom',
            content_cls=self.add_person_popup_content_cls,
            buttons=[buttons]
        ).open()

    def _prepare_person_to_adding(self, *args):
        person_to_add = Person(
            name=self.add_person_popup_content_cls.name.text,
            age=int(self.add_person_popup_content_cls.age.text),
            behaviour=self.add_person_popup_content_cls.behaviour.text,
        )
        self.controller.send_add_person_command(person_to_add)
