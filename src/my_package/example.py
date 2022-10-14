import ipywidgets as widgets

def create_button(text):
    return widgets.Button(description=text)

def add_numbers(num1, num2):
    return num1 + num2