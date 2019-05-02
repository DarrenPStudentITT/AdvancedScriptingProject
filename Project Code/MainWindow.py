import psutil #This is necessary to read the CPU usage
import datetime #This is necessary to print the date/time to results file

from kivy.app import App
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

#All of the above kivy import statements are necessary to get the GUI windows, and their various components
# up and running.

now = datetime.datetime.now() #Gets the current date/time


class appLayout(BoxLayout): #This program works by essentially "rendering" everything first,
                            # which is what all the below code does
    def __init__(self):
        super(appLayout, self).__init__() #Define the layout of the MainWindow

        btnFUNC = Button(text = "What is my current CPU usage?")
        btnFUNC.bind(on_press = self.clkFUNC)

        btnREAD = Button(text = "Read Previous Results")
        btnREAD.bind(on_press = self.clkREAD)

        btnEXIT = Button(text="Exit Application")
        btnEXIT.bind(on_press = self.clkEXIT)

        #Render 3 buttons, and what functions to execute when pressed

        self.add_widget(btnFUNC)
        self.add_widget(btnREAD)
        self.add_widget(btnEXIT)
        #Add the buttons to the main app screen


    def clkFUNC(self, obj): #The function behind the CPU Usage button
        result = psutil.cpu_percent() #Psutil function to query the CPU usage as a percentage
        f = open("CPU_TestResults.txt", "a+") #Open the results txt file, creates it if it doesn't exists
        f.write("\n" + now.strftime("%Y-%m-%d %H:%M \t Your current CPU usage is: ") + str(result))
        #Writes the current date/time (minus milliseconds), and the result of the CPU usage (as a string) to the txt file

        popup = Popup(title = 'CPU Usage',
                      size_hint=(None, None),
                      content = Label(text='Your current CPU usage is: ' + str(result) + '%'),
                      size=(400, 400))
        popup.open()
        #Creates the popup window when the button is clicked, and displays the current CPU usage result (as a string)

    def clkREAD(self, obj):
        f = open("CPU_TestResults.txt", "r") #Opens the results txt file in read mode
        contents = f.read() #Copies the contents of the results file to a variable "contents"

        popup = Popup(title='CPU Results Log',
                      size_hint=(None, None),
                      content=Label(text=contents),
                      size=(400, 400))
        popup.open()
        #Creates the popup window when the button is clicked, and displays the "contents" variable in the popup window

    def clkEXIT(self, obj):
        App.get_running_app().stop()
        Window.close()

    #Simple Function that closes application upon the button being clicked

class myApp(App):
    def on_stop(self):
        Logger.critical('Thank you for using this App') #Prints a message to the console upon app closure

    def build(self):
        AL = appLayout()
        return AL
    # Finally after everything is "rendered", these two actually display the app layout to the screen

if __name__ == "__main__":
    myApp().run()