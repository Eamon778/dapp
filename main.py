from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file('./cal.kv')
Window.size = (350, 550)

class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = '0'

    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"
        elif prev_number == "Error":
            prev_number = ''
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    def sings(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"
        last_char = prev_number[-1] if prev_number else ''
        
        if last_char in ['+', '-', '×', '÷']:
            # Replace the last character with the new sign
            self.ids.input_box.text = f"{prev_number[:-1]}{sing}"
        else:
            self.ids.input_box.text = f"{prev_number}{sing}"

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def results(self):
        prev_number = self.ids.input_box.text
        expression = prev_number.replace("\u00D7", "*").replace("\u00F7", "/")
        try:
            result = eval(expression)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text="Error"

    def pos_neg(self):
        prev_number = self.ids.input_box.text
        first_value = prev_number[0] if prev_number else None

        if first_value.isdigit():
            self.ids.input_box.text = f"+{prev_number}"
        elif first_value == '+':
            self.ids.input_box.text = f"-{prev_number[1:]}"
        elif first_value == '-':
            self.ids.input_box.text = f"+{prev_number[1:]}"

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()
    
if __name__ == "__main__":
    CalculatorApp().run()