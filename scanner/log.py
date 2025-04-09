import variaveis
import datetime
import sys
import tkinter as tk
from tkinter import messagebox

def box_text(texto):
    now = datetime.datetime.now()
    variaveis.BOX_TEXT += f"{now.strftime("%H:%M:%S")}: {texto}"
    variaveis.READ.set()
def box_text_log(texto):
    if variaveis.LOG == True:
        now = datetime.datetime.now()
        variaveis.BOX_TEXT += f"{now.strftime("%H:%M:%S")}: {texto}"
        variaveis.READ.set()
def popup(titulo:str, texto:str, tipo:str):
    result  = messagebox.showinfo(title=titulo, message=texto, type=tipo)
    return result
def crash(texto):
    tk.messagebox.showerror("Erro", texto)
    sys.exit(1)