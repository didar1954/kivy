from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','width',400)
Config.set('graphics','height',600)
class MainWindow(Screen):
    pass

class SectionWindow(Screen):
    pass

class MBazeWindow(Screen):
    pass
class PersonalWindow(Screen):
    pass
class ErbolulyDWindow(Screen):
    pass
class ProgressWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv=Builder.load_file("main2.kv")

class MainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MainApp().run()