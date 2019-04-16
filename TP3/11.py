import socket
import os


def Servidor():
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host, port = socket.gethostname(), 8881

    try:
        socket_tcp.bind((host, port))
        socket_tcp.listen(5)
        print("Servidor de nome %s esperando conexão na porta %s" % (host, port))

        while True:
            (socket_cliente, addr) = socket_tcp.accept()
            print("Conectado a:", str(addr))
            file = socket_cliente.recv(2048)
            file = file.decode('utf-8')
            error = -1

            if os.path.isfile(file):

                size = os.stat(file).st_size
                socket_cliente.send(str(size).encode('utf-8'))

                socket_tcp = open(file, 'rb')
                bytes_count = socket_tcp.read(4096)

                while bytes_count:
                    socket_cliente.send(bytes_count)
                    bytes_count = socket_tcp.read(4096)
                     
            else:
                socket_cliente.send(str(error).encode('utf-8'))
                print('O arquivo não existe!')
            
    except Exception as error:
        print(error)
    socket_tcp.close()
    
Servidor()
