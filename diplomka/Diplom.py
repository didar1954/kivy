from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','width',400)
Config.set('graphics','height',600)

Builder.load_string('''
<Main>:
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint_y:.25
            padding:25
            BoxLayout:
                orientation:"vertical"
                Label:
                    text:"Спорт Кешені"
                    font_style:"H4"
                BoxLayout:
                    adaptive_size:True
                    spacing:dp(10)
                    Label:
                        text:"Home"
                        text_size:None,None
                        adaptive_width:True

        GridLayout:
            size_hint_y:.30
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            Button:
                Image:
                    source: 'image/section.png'                 
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y

            Button:
                text:"Қызметкерлер"
                on_press:root.manager.current='personal'

            Button:
                text:"Қызметкерлер"
                on_press:root.manager.current='mbaze'

            Button:
                text:"Жетістіктер"
                on_press:root.manager.current='progress'

''')
class Main(Screen):
    pass

class Section(Screen):
    pass

class MBaze(Screen):
    pass

class Personal(Screen):
    pass

class Progress(Screen):
    pass

class MainApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Main(name='main'))
        sm.add_widget(Section(name='section'))
        sm.add_widget(MBaze(name='mbaze'))
        sm.add_widget(Personal(name='personal'))
        sm.add_widget(Progress(name='progress'))
        return sm

if __name__ == "__main__":
    MainApp().run()