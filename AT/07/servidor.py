"""

Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.

"""
#Servidor
import socket
import psutil

UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerName = socket.gethostname() 
Port = 6666
UDPServer.bind((ServerName, Port))

memoria_total = round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 1)
memoria_disponivel = round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 1)



try:
    print('Aguardando requisição na porta', Port, '...')
    (msg, client) = UDPServer.recvfrom(1024)
    print('Requisição aceita')
    if msg.decode() == 'y':
        UDPServer.sendto('\nNome do Servidor: {} \nMemória total: {}GB \nMemória Disponivel: {}GB'.format(ServerName, memoria_total, memoria_disponivel).encode('utf-8'), client)
        print('Informações enviadas com sucesso')
    
    else:
        UDPServer.sendto('Erro: Digite "y".'.encode('utf-8'), client)
        print('Informações não foram enviadas.')


except Exception as error:
    print(error)

 