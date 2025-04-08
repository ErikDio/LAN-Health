import variaveis
import datetime
import sys
import tkinter as tk

def box_text(texto):
    now = datetime.datetime.now()
    variaveis.BOX_TEXT += f"{now.strftime("%H:%M:%S")}: {texto}"
    variaveis.READ.set()
def box_text_log(texto):
    if variaveis.LOG == True:
        now = datetime.datetime.now()
        variaveis.BOX_TEXT += f"{now.strftime("%H:%M:%S")}: {texto}"
        variaveis.READ.set()
def popup(texto):
    tk.messagebox.showinfo("Informação", texto)
def crash(texto):
    tk.messagebox.showerror("Erro", texto)
    sys.exit(1)