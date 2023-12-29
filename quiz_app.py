from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from data_classes.images_loader import ImagesLoader
from screens.main_screen import MainScreen
from screens.image_screen import ImageScreen


class QuizApp(MDApp):
    screen_manager: ScreenManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "500"
        self.title = ""

    def build(self):
        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen()
        self.image_screen = ImageScreen(ImagesLoader(), name="image_mode")

        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.image_screen)

        return self.screen_manager
