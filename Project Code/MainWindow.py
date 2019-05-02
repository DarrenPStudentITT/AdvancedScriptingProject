import psutil
import datetime
from kivy.app import App
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

now = datetime.datetime.now()


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
        result = psutil.cpu_percent()
        f = open("CPU_TestResults.txt", "a+")
        f.write("\n" + now.strftime("%Y-%m-%d %H:%M \t Your current CPU usage is: ") + str(result))

        popup = Popup(title = 'CPU Usage',
                      size_hint=(None, None),
                      content = Label(text='Your current CPU usage is: ' + str(result) + '%'),
                      size=(400, 400))
        popup.open()

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