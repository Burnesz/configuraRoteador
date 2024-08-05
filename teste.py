script = """
hostname {hostname}
interface GigabitEthernet0/0
 ip address {ip_wan} 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 {ip_rota}
end
write memory
"""

scriptFormatado = script.format(hostname = 'rubens', ip_wan = 'sorares',ip_rota = 'pereira')
print(scriptFormatado)