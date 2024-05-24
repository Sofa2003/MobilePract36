from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
Config.set('graphics','resizable',0)
Config.set('graphics','width',400)
Config.set('graphics','height',500)


class CalculatorApp(App):
    def update_label(self):
        self.lb1.text = self.formula
    def add_number(self,instatnce):
        if (self.formula == "0"):
            self.formula =""

        self.formula +=str(instatnce.text)
        self.update_label()

    def add_operation(self,instatnce):
        if(str(instatnce.text.lower()) == "x"):
            self.formula += "*"
        else:
            self.formula+=str(instatnce.text)
        self.update_label()

    def calc_result(self,instatnce):
        self.lb1.text = str(eval(self.lb1.text))

    def build(self):
         self.formula = "0"
         b1 = BoxLayout(orientation="vertical", padding=25)
         gl = GridLayout(cols=4,spacing = 3, size_hint = (1,.6))

         self.lb1 = Label(text="0",font_size = 40, halign="right",valign = "center",size_hint =(1,.4),text_size=(500-50,500*.4-50))
         b1.add_widget(self.lb1)

         gl.add_widget(Button(text="7",on_press = self.add_number))
         gl.add_widget(Button(text="8",on_press = self.add_number))
         gl.add_widget(Button(text="9",on_press = self.add_number))
         gl.add_widget(Button(text="X",on_press = self.add_operation))


         gl.add_widget(Button(text="4",on_press = self.add_number))
         gl.add_widget(Button(text="5",on_press = self.add_number))
         gl.add_widget(Button(text="6",on_press = self.add_number))
         gl.add_widget(Button(text="-",on_press = self.add_operation))

         gl.add_widget(Button(text="1",on_press = self.add_number))
         gl.add_widget(Button(text="2",on_press = self.add_number))
         gl.add_widget(Button(text="3",on_press = self.add_number))
         gl.add_widget(Button(text="+",on_press = self.add_operation))

         gl.add_widget(Widget())
         gl.add_widget(Button(text="0",on_press = self.add_number))
         gl.add_widget(Button(text="."))
         gl.add_widget(Button(text="=",on_press = self.calc_result))

         b1.add_widget( gl )
         return b1


if __name__  == "__main__":
    CalculatorApp().run()