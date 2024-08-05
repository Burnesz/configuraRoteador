import tkinter as tk
from tkinter import messagebox
import os
from TelaLog import Log


class TelaInicial:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configura Roteador")
        self.center_window(600, 300)
        self.listaRoteadores = []

        self.label1 = tk.Label(self.root, text="Digite os ip's dos roteadores:")
        self.label1.grid(row=0, column=0, padx=10, pady=5)
        self.text1 = tk.Text(self.root, height=5, width=40)  
        self.text1.grid(row=0, column=1, padx=10, pady=5)

        self.button = tk.Button(self.root, text="Testar Conexão", command=self.bnt_testarConexao)
        self.button.grid(row=3, column=1, columnspan=2, pady=10)
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def bnt_testarConexao(self):
        if self.text1.get('1.0', 'end').strip() == '':
            messagebox.showinfo("Informação", "Insira ao menos um ip")
        else:
            self.listaRoteadores = self.text1.get('1.0', 'end').split()
            log = Log(self.root, self.listaRoteadores)
            for roteador in self.listaRoteadores:
                ping = os.system(f"ping -c 1 {roteador}")
                if ping == 0:
                    log.carrega_log(f"Roteador {roteador} está no alcançe da rede ✅\n")
                else:
                    log.carrega_log(f"Roteador {roteador} está inalcançavel 🚫\n")

    def getListaRoteadores(self):
        return self.listaRoteadores

if __name__ == "__main__":
    
    interface = TelaInicial()
    interface.root.mainloop()