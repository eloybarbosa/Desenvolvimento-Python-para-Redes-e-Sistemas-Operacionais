"""

Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.

"""
#Cliente
import socket
import time


print('Nesta atividade vamos nos conectar a um servidor via UDP, coletar as informações de quantidade total e disponivel de memória no servidor .\n')
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClient.settimeout(5)
ServerName = socket.gethostname()  
Port = 6666               

print('Solicitando dados... ')

tentativas = 0

for i in range(5):
    print("Tentativa ", (i+1), "...")
    tentativas += 1
    msg = 'y'
    UDPClient.sendto(msg.encode('utf-8'), (ServerName, Port))
    try:
        (msg, client) = UDPClient.recvfrom(1024)
        print(msg.decode('utf-8'))
        break
    except socket.timeout:
        continue
            
if tentativas == 5:
    print('Mesmo após 5 Tentativas não foi possivel obter resposta')


