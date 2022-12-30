import asyncio

from kivy.utils import platform
from kivymd.app import MDApp

from src.entrypoints.kivy.screens import ScreenGenerator

if platform == 'android':
    from android.permissions import Permission, request_permissions
    request_permissions(
        [
            Permission.INTERNET,
            Permission.VIBRATE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.ACCESS_FINE_LOCATION,
            Permission.ACCESS_COARSE_LOCATION,
        ]
    )


class KivyApp(MDApp):
    title = 'Santa Claus notebook'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "200"
        self.theme_cls.material_style = "M3"
        return ScreenGenerator().build_app_view()


if __name__ == '__main__':
    asyncio.run(KivyApp().async_run(async_lib='asyncio'))
