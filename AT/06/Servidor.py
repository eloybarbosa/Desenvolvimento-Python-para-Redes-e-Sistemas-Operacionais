"""

Escreva um programa cliente e servidor sobre TCP em Python em que:
O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

"""
#Servidor
import socket
import os
import pickle


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 6666
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    print()
    arquivo = socket_cliente.recv(1024)
    print ('O cliente informou que quer a lista de arquivos (somente arquivos) do seguinte diretório: ', arquivo.decode('utf-8'))
    print()
    files=[]
    if os.path.exists(arquivo):
        arquivos = os.listdir(arquivo)
        for i in range (len(arquivos)):
           if os.path.isfile(arquivo + arquivos[i]) == True:
               files.append(arquivos[i].decode('utf-8'))
        print('No diretório informado contem os seguintes arquivos: ', files)
        print()
            
                
        resposta = pickle.dumps(files)
        socket_cliente.send(resposta)
        print('Lista de arquivos enviada para o cliente.')
    else:
        pass
    

    socket_cliente.close()
