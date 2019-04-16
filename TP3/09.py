import socket
import psutil

UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerName = socket.gethostname() 
Port = 9991
UDPServer.bind((ServerName, Port))

principal_total = round(psutil.disk_usage('.').total / (1024 * 1024 * 1024), 2)
principal_disponivel = round(psutil.disk_usage('c:').free / (1024 * 1024 * 1024), 2)

try:
    print('Aguardando requisição na porta', Port, '...')
    (msg, client) = UDPServer.recvfrom(1024)
    print('Requisição aceita')
    if msg.decode() == 'y':
        UDPServer.sendto('\nNome do Servidor: {} \nEspaço total: {}GB \nDisponivel: {}GB'.format(ServerName, principal_total, principal_disponivel).encode('utf-8'), client)
        print('Informações enviadas com sucesso')

    else:
        UDPServer.sendto('Erro: Digite "y".'.encode('utf-8'), client)
        print('Informações não foram enviadas.')

except Exception as error:
    print(error)

 