import tkinter as tk
from tkinter import ttk


class Widgets():
    entry_widget = []
    label_widget = []
    button_widget = []
    checkbox_widget = []
    root = None
    def __init__(self, root):
        self.root = root
    def add_entry(self, name:str, column:int, row:int, columnspan:int=1):
        self.entry_widget.append(ttk.Entry(self.root))
        self.entry_widget[-1].name = name
        self.entry_widget[-1].grid(row=row, column=column, columnspan = columnspan, pady = 5, padx = 2, sticky = "ew")
    def add_label(self, name:str, text:str, column:int, row:int):
        self.label_widget.append(ttk.Label(self.root, text=text))
        self.label_widget[-1].name = name
        self.label_widget[-1].grid(row=row, column=column, pady = 2)
    def add_button(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        self.button_widget.append(ttk.Button(self.root, text=text))
        self.button_widget[-1].name = name
        self.button_widget[-1].grid(row=row, column=column, columnspan = columnspan, pady = 5, padx = 2, sticky = "ew")
    def add_checkbox(self, name:str, text:str, column:int, row:int):
        self.checkbox_widget.append(ttk.Checkbutton(self.root, text=text))
        self.checkbox_widget[-1].name = name
        self.checkbox_widget[-1].grid(row=row, column=column, pady = 5)

root = tk.Tk()
root.title("Scanner")
#root.geometry("800x600")
widgets = Widgets(root)
widgets.add_label("Gateway", "Gateway Padrão:", 0, 0)
widgets.add_entry("Gateway", 1, 0, 4)

widgets.add_label("Prefix", "Prefixo:", 0, 2)
widgets.add_entry("Prefix", 1, 2)
widgets.add_label("Speed", "Velocidade(Mb):", 2, 2)
widgets.add_entry("Speed", 3, 2)

widgets.add_label("Options", "Opções de Scan:", 0, 3)
widgets.add_entry("Options", 1, 3)
widgets.add_label("Config", "Delay(min):", 2, 3)
widgets.add_entry("Config", 3, 3)

widgets.add_checkbox("Debug", "Debug", 0, 4)
widgets.add_checkbox("Log", "Log", 1, 4)
widgets.add_button("Start", "Iniciar", 0, 5, 4)

root.mainloop()
