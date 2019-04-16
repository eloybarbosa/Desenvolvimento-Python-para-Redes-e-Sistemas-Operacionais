"""

Escreva um programa cliente e servidor sobre TCP em Python em que:
O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

"""
#Cliente
import socket
import os
import pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
arquivo = input('Informe o diretório: ')
print()


socket_cliente.connect((socket.gethostname(), 6666))
socket_cliente.send(arquivo.encode('utf-8'))

mensagem = socket_cliente.recv(10000)

arquivos = pickle.loads(mensagem)


print('No diretório informado contem os seguintes arquivos: \n')
for x in range (len(arquivos)):
    print(arquivos[x])

socket_cliente.close()