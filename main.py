from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.graphics.texture import Texture
from kivymd.uix.widget import MDWidget
from kivy.core.window import Window
from kivy.uix.image import Image
import webbrowser
from kivy.animation import Animation
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
from kivy.graphics import Color, Line
from kivy.graphics import ClearColor
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivy.factory import Factory
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivy.config import Config
from kivy.uix.video import Video
from kivy.config import Config


class TelaInicial(Screen):
    pass


class TelaLoginScreen(Screen):
    pass


class TelaRegisterScreen(Screen):
    pass


class TelaProdutos(Screen):
    pass


class TelaCarrinho(Screen):
    pass


class TelaPagamento(Screen):
    pass


class Gerenciador(ScreenManager):
    pass


class LojaApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        return Gerenciador()


LojaApp().run()
