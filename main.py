from Bot import Client
from configBot import TOKEN
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class BoxApp(App):
    client = Client()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text="0")
        gl = GridLayout(cols=3, spacing=3, size_hint=(1, 0.2))
        bl = BoxLayout(orientation='horizontal')
        al1 = AnchorLayout(anchor_y="top", anchor_x="right", size_hint=(1, .5))
        al1.add_widget(TextInput(size_hint=(1, 0.5)))
        bl.add_widget(self.lbl)
        gl.add_widget(Button(text="RUN", on_press=self.start))
        gl.add_widget(Button(text="Send", on_press=self.add_text))
        gl.add_widget(Button(text="Stop", on_press=self.stop))
        al1.add_widget(gl)
        bl.add_widget(al1)

        return bl

    def start(self, instance):
        client = Client()
        self.formula = str(instance.text)
        print(self.formula)
        client.run(TOKEN)

    def send(self, instance):
        self.formula = str(instance.text)
        print(self.formula)

    def stop(self, instance):
        self.formula = str(instance.text)
        print(self.formula)
        #BoxApp.exit
        Client.logout(TOKEN)

    def update_label(self):
        self.lbl.text = self.formula

    def add_text(self, instance):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()
        self.send(instance)




if __name__ == '__main__':
    app = BoxApp()
    app.run()



