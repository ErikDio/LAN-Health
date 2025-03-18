
import tkinter as tk
from tkinter import ttk
import variaveis

class Widgets():
    entry_widget = []
    label_widget = []
    button_widget = []
    checkbox_widget = []
    root = None
    def __init__(self, root):
        self.root = root
        self.checkbox_vars = {}  # Add this line to store checkbox variables
    def add_entry(self, name:str, column:int, row:int, columnspan:int=1):
        self.entry_widget.append(ttk.Entry(self.root))
        self.entry_widget[-1].name = name
        self.entry_widget[-1].grid(row=row, column=column, columnspan = columnspan, pady = 5, padx = 2, sticky = "ew")
    def add_label(self, name:str, text:str, column:int, row:int):
        self.label_widget.append(ttk.Label(self.root, text=text))
        self.label_widget[-1].name = name
        self.label_widget[-1].grid(row=row, column=column, pady = 2)
    def add_button(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        self.button_widget.append(ttk.Button(self.root, text=text, command=self.click))
        self.button_widget[-1].name = name
        self.button_widget[-1].grid(row=row, column=column, columnspan = columnspan, pady = 5, padx = 2, sticky = "ew")
    def add_checkbox(self, name:str, text:str, column:int, row:int, valor=False):
        self.checkbox_vars[name] = tk.BooleanVar(value=False)
        self.checkbox_widget.append(ttk.Checkbutton(self.root, text=text, variable=self.checkbox_vars[name], command = lambda: self.atualizar(name)))
        self.checkbox_widget[-1].name = name
        self.checkbox_widget[-1].grid(row=row, column=column, pady = 5)

    def click(self):
        print(variaveis.DEBUG)
        print("Button clicked")

    def atualizar(self, name:str):
        print("Atualizando")
        if(name.lower() == "debug"):
            variaveis.DEBUG = self.checkbox_vars[name].get()
        elif(name.lower() == "log"):
            variaveis.LOG = self.checkbox_vars[name].get()