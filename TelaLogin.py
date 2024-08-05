import tkinter as tk
from Roteador import Napalm
import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

class TelaLogin:
    def __init__(self, unroot, listaRoteadores):
        self.unroot = unroot
        self.listaRoteadores = listaRoteadores
        self.unroot.destroy()

        self.root = tk.Tk()
        self.root.title("Conexão SSH")
        self.center_window(600,300)

        self.label1 = tk.Label(self.root, text="Usuario:")
        self.label1.grid(row=0, column=0, padx=10, pady=5)
        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)

        self.label2 = tk.Label(self.root, text="Senha:")
        self.label2.grid(row=1, column=0, padx=10, pady=5)
        self.entry2 = tk.Entry(self.root)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)

        self.script = tk.StringVar(self.root)
        self.script.set("Escolha uma opção")

        opcoes = ["Script 1", "Script 2"]

        self.selecao = tk.OptionMenu(self.root, self.script, *opcoes)
        self.selecao.grid(row=2, column=1, columnspan=2, pady=10)

        self.script.trace_add("write", self.update_fields)

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.label3 = tk.Label(self.frame, text="Hostname:")
        self.entry3 = tk.Entry(self.frame)

        self.label4 = tk.Label(self.frame, text="Ip Wan")
        self.entry4 = tk.Entry(self.frame)

        self.label5 = tk.Label(self.frame, text="Ip Rota:")
        self.entry5 = tk.Entry(self.frame)

        self.button1 = tk.Button(self.frame, text="Entrar", command=self.conexaoSSH)

        self.root.mainloop()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def conexaoSSH(self):

        for host in self.listaRoteadores:

            roteador = Napalm(
                host, 
                self.entry1.get(), 
                self.entry2.get(), 
                self.entry3.get(), 
                self.entry4.get(),
                self.entry5.get()
            )

            roteador.conexao_ssh()
            
    def update_fields(self, *args):

        selected_option = self.script.get()
        
        if selected_option == "Script 1":
            self.label3.grid(row=0, column=0, padx=10, pady=5)
            self.entry3.grid(row=0, column=1, padx=10, pady=5)

            self.label4.grid(row=1, column=0, padx=10, pady=5)
            self.entry4.grid(row=1, column=1, padx=10, pady=5)

            self.label5.grid(row=2, column=0, padx=10, pady=5)
            self.entry5.grid(row=2, column=1, padx=10, pady=5)

            self.button1.grid(row=3, column=1, columnspan=2, pady=10)

        else:
            self.label3.grid_forget()
            self.entry3.grid_forget()

            self.label4.grid_forget()
            self.entry4.grid_forget()

            self.label5.grid_forget()
            self.entry5.grid_forget()

            self.button1.grid_forget()
