from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager 
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
#from kivymd.uix.carousel import MDFileManager
Windowsize=(310, 580)

class Slope(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager
    

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="Poppins\Poppins-Medium.ttf")
    LabelBase.register(name="MPoppins", fn_regular="Poppins\Poppins-SemiBold.ttf")
    Slope().run()