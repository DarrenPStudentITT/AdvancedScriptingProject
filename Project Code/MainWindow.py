import kivy, psutil

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.label import Label

class appLayout(BoxLayout):
    def __init__(self):
        super(appLayout, self).__init__()

        btn = Button(text = "What is my current CPU usage?")
        btn.bind(on_press = self.clk)

        btnEXIT = Button(text="Exit Application")
        btnEXIT.bind(on_press = self.clkEXIT)

        self.add_widget(btn)
        self.add_widget(btnEXIT)

    def clk(self, obj):
        ##CPULabel = Label(text = "Your CPU usage is currently: ")
        ##self.add_widget(CPULabel)
        print("Your CPU usage is currently: ")
        print(psutil.cpu_percent())

    def clkEXIT(self, obj):
        App.get_running_app().stop()
        Window.close()

class myApp(App):
    def on_stop(self):
        Logger.critical('Thank you for using this App')

    def build(self):
        AL = appLayout()
        return AL

if __name__ == "__main__":
    myApp().run()