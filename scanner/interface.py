import tkinter as tk
from tkinter import ttk
import variaveis
import ipaddress
import scan
import threading
import log

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
        threading.Thread(target=self.atualizar_texto).start()
    def add_entry(self, name:str, column:int, row:int, columnspan:int=1):
        self.entry_widget[name] = tk.Entry(self.root, bg="white", font=("Arial", 14))
        self.entry_widget[name].grid(row=row, column=column, columnspan=columnspan, pady=5, padx=5, sticky="ew")
    def add_label(self, name:str, text:str, column:int, row:int):
        self.label_widget[name] = ttk.Label(self.root, text=text, font=("Arial", 14))
        self.label_widget[name].grid(row=row, column=column, pady=5, padx=5)
    def add_button(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        self.button_widget[name] = (ttk.Button(self.root, text=text, command=self.click))
        self.button_widget[name].grid(row=row, column=column, columnspan=columnspan, pady=5, padx=5, sticky="ew")
    def add_checkbox(self, name:str, text:str, column:int, row:int, valor=False):
        self.checkbox_vars[name] = tk.BooleanVar(value=False)
        self.checkbox_widget[name] = ttk.Checkbutton(self.root, text=text, variable=self.checkbox_vars[name], command=lambda: self.atualizar(name))
        self.checkbox_widget[name].grid(row=row, column=column, pady=5, padx=5)
    def add_text(self, name:str, text:str, column:int, row:int, columnspan:int=1):
        frame = tk.Frame(self.root)  # Create a frame to hold the text widget and scrollbar
        frame.grid(row=row, column=column, columnspan=columnspan, rowspan=6, pady=10, padx=10, sticky="ew")
        self.text_widget[name] = tk.Text(frame, height=15, width=60, wrap="word", state="disabled", font=("Arial", 10))
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.text_widget[name].yview)
        self.text_widget[name].configure(yscrollcommand=scrollbar.set)
        self.text_widget[name].pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def click(self):
        if (variaveis.RUNNING == False):
            threading.Thread(target=self.iniciar).start()
        else:
            threading.Thread(target=self.parar).start()
    def iniciar(self):
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
            delay = int(self.entry_widget["delay"].get())
            gateway = self.entry_widget["gateway"].get()
            prefix = int(self.entry_widget["prefix"].get())
            speed = int(self.entry_widget["speed"].get())
            config = self.entry_widget["options"].get()
            scanner = scan.Scan(delay=delay, gateway=gateway, prefix=prefix, speed=speed, config=config)
            variaveis.RUNNING = True
            threading.Thread(target=scanner.run).start()
            self.button_widget["start"].config(text="Parar")
            for formulario in self.entry_widget:
                self.entry_widget[formulario].config(state="disabled")
            for chkbox in self.checkbox_widget:
                self.checkbox_widget[chkbox].config(state="disabled")

    def parar(self):
        self.button_widget["start"].config(state="disabled")
        self.button_widget["start"].config(text="Parando... Aguarde")
        variaveis.RUNNING = False
        variaveis.FINISHING.set()
        threading.Event.wait(variaveis.ABORTED)
        variaveis.ABORTED.clear()
        variaveis.FINISHING.clear()
        self.button_widget["start"].config(text="Iniciar")
        self.button_widget["start"].config(state="normal")
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
    def atualizar_texto(self):
        while True:
            threading.Event.wait(variaveis.READ)
            self.text_widget["text"].config(state="normal")
            self.text_widget["text"].insert(tk.END, variaveis.BOX_TEXT + "\n")
            variaveis.BOX_TEXT = ""
            self.text_widget["text"].see(tk.END)
            self.text_widget["text"].config(state="disabled")
            variaveis.READ.clear()