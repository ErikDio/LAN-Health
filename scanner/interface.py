import tkinter as tk
from tkinter import ttk
import variaveis
import ipaddress
import scan
import threading

class Widgets():
    entry_widget:tk.Entry = {}
    entry_text:tk.Text
    label_widget:ttk.Label = {}
    button_widget:ttk.Button = {}
    checkbox_widget:ttk.Checkbutton = {}
    text_widget:tk.Text = {}
    root = None
    def __init__(self, root):
        self.root = root
        self.checkbox_vars = {}
    def add_entry(self, name:str, column:int, row:int, columnspan:int=1):
        self.entry_widget[name] = tk.Entry(self.root, bg="white")
        self.entry_widget[name].grid(row=row, column=column, columnspan=columnspan, pady=5, padx=2, sticky="ew")
    def add_label(self, name:str, text:str, column:int, row:int):
        self.label_widget[name] = ttk.Label(self.root, text=text)
        self.label_widget[name].grid(row=row, column=column, pady=2, padx=2)
    def add_button(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        self.button_widget[name] = (ttk.Button(self.root, text=text, command=self.click))
        self.button_widget[name].grid(row=row, column=column, columnspan=columnspan, pady=5, padx=2, sticky="ew")
    def add_checkbox(self, name:str, text:str, column:int, row:int, valor=False):
        self.checkbox_vars[name] = tk.BooleanVar(value=False)
        self.checkbox_widget[name] = ttk.Checkbutton(self.root, text=text, variable=self.checkbox_vars[name], command=lambda: self.atualizar(name))
        self.checkbox_widget[name].grid(row=row, column=column, pady=5)
    def add_text(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        frame = tk.Frame(self.root)  # Create a frame to hold the text widget and scrollbar
        frame.grid(row=row, column=column, columnspan=columnspan, rowspan=6, pady=5, padx=10, sticky="ew")
        
        self.text_widget[name] = tk.Text(frame, height=10, width=50, wrap="word", state="disabled")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.text_widget[name].yview)
        self.text_widget[name].configure(yscrollcommand=scrollbar.set)
        
        self.text_widget[name].pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def click(self):
        if (variaveis.RUNNING.is_set() == False):
            start = True
            try:
                ipaddress.IPv4Address(self.entry_widget["gateway"].get())
                self.entry_widget["gateway"].config(bg="white")
            except:
                self.entry_widget["gateway"].config(bg="red")
                start = False
            if (self.entry_widget["delay"].get().isdigit() == False):
                self.entry_widget["delay"].config(bg="red")
                start = False
            else:
                self.entry_widget["delay"].config(bg="white")
            if (self.entry_widget["speed"].get().isdigit() == False):
                self.entry_widget["speed"].config(bg="red")
                start = False
            else:
                self.entry_widget["speed"].config(bg="white")
            if (self.entry_widget["prefix"].get().isdigit() == False):
                self.entry_widget["prefix"].config(bg="red")
                start = False
            else:
                self.entry_widget["prefix"].config(bg="white")
            if(start == True):
                variaveis.RUNNING.set()
                self.button_widget["start"].config(text="Parar")
                for formulario in self.entry_widget:
                    self.entry_widget[formulario].config(state="disabled")
                for chkbox in self.checkbox_widget:
                    self.checkbox_widget[chkbox].config(state="disabled")
        else:
            variaveis.RUNNING.clear()
            self.button_widget["start"].config(text="Iniciar")
            for formulario in self.entry_widget:
                self.entry_widget[formulario].config(state="normal", bg="white")
            for chkbox in self.checkbox_widget:
                self.checkbox_widget[chkbox].config(state="normal")

    def atualizar(self, name:str):
        print("Atualizando")
        if(name.lower() == "debug"):
            variaveis.DEBUG = self.checkbox_vars[name].get()
        elif(name.lower() == "log"):
            variaveis.LOG = self.checkbox_vars[name].get()