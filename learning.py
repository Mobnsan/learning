
from kivy.uix.label import Label

class TestApp(App):
    
    def build(self):

        return Label(text="Kivy يعمل الآن!")

TestApp().run()
