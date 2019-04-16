import socket
import pickle
import os

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 8881


def Cliente():
    socket_tcp.connect((host, port))

    file = "arquivo.txt"
    socket_tcp.send(file.encode('utf-8'))

    msg = socket_tcp.recv(8)

    size = int(msg.decode())

    if size >= 0:

        print(f"Tamanho do arquivo {size}")

        if os.path.isdir('transferidos') is not True:
            os.mkdir('transferidos')

        file = open('transferidos/' + file, 'wb')
        bytes_count = socket_tcp.recv(4096)

        count = 0

        while bytes_count:
            file.write(bytes_count)
            count += len(bytes_count)
            loading(count, size)
            if count == size:
                break
            bytes_count = socket_tcp.recv(4096)
        print("Transferência Concluida!")

    else:
        print("Arquivo não encontrado!")

    socket_tcp.close()


def loading(bytes, size):
    kbytes = bytes / 1024
    tam_bytes = size / 1024
    txt = 'Baixando... '
    txt += '{:<.2f}'.format(kbytes) + ' KB '
    txt += 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(txt)
    
Cliente()
