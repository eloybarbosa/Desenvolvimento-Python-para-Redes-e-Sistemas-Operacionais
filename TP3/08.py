import socket

print('Nesta atividade vamos nos conectar a um servidor via UDP, coletar as informações de quantidade total e disponivel\nde armazenamento do disco na qual o processo do servidor está rodando.\n')
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerName = socket.gethostname()  
Port = 9991                

msg = input("Deseja receber as informações(y/n):")

try:
    UDPClient.sendto (msg.encode('utf-8'), (ServerName, Port))

    (msg, client) = UDPClient.recvfrom(1024)
    print(msg.decode('utf-8'))

    input('\nPressione enter para sair...')
    UDPClient.close()
    
except Exception as error:
    print(error)
