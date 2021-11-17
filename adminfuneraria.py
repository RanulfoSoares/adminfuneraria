import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root
from kivymd.uix.menu import MDDropdownMenu
from libs.uix.baseclass.cidadao_screen import CidadaoScreen

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class adminfuneraria(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(adminfuneraria, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "administracao funeraria"

        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "A400"

        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"
        

    def build(self):
        return Root()

