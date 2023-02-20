import kivy
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('tictactoe.kv')
    board = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = {
            1: self.root.ids.btn1,
            2: self.root.ids.btn1,
            3: self.root.ids.btn1,
            4: self.root.ids.btn1,
            5: self.root.ids.btn1,
            6: self.root.ids.btn1,
            7: self.root.ids.btn1,
            8: self.root.ids.btn1,
            9: self.root.ids.btn1

        }



    def pressed(self):
        pass


MainApp().run()
