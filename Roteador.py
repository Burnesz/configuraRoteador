from napalm import get_network_driver
from tkinter import messagebox

script = """
hostname {hostname}
interface GigabitEthernet0/0
 ip address {ip_wan} 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 {ip_rota}
end
write memory
"""

driver = get_network_driver("ios")

class Napalm:

    def __init__(self, host, usuario, senha, hostname, ip_wan, ip_rota):
        
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.script = script.format(
            hostname = hostname, 
            ip_wan = ip_wan, 
            ip_rota = ip_rota
        )

    def conexao_ssh(self):

        try:
            
            device = driver(
                hostname = self.host,
                username = self.usuario,
                password = self.senha,
                timeout= 5000,
                optional_args = {"port": 22}
            )

            device.open()
            device.load_merge_candidate(config = self.script)
            device.commit_config()

        except Exception as e:
            print(e)

        finally:
            device.close()
            messagebox.showinfo("Informação", "Configuração do host: "+ self.host+ " bem sucedida")