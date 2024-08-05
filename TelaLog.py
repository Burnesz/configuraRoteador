import tkinter as tk
from tkinter import Toplevel, Text, Scrollbar, END
from TelaLogin import TelaLogin

class Log:

    def __init__(self, root, roteadores):
        self.root = root
        self.log = Toplevel(self.root)
        self.log.title("Log")
        self.listaRoteadores = roteadores

        self.text_area = Text(self.log, wrap='word')
        self.scrollbar = Scrollbar(self.log, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)

        self.text_area.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')

        self.log.after(5000, self.autoDestroy)

    def carrega_log(self, mensagem):
        self.text_area.insert(END, mensagem)

    def autoDestroy(self):
        self.log.destroy
        telaLogin = TelaLogin(self.root, self.listaRoteadores)

