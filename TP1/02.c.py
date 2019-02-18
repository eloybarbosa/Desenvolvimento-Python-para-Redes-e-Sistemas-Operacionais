#c. Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?

import os

print('O Nome do caminho completo do diretório de usuário em Python é:', os.environ['HOMEDRIVE'], os.environ['HOMEPATH'])

print()
input('Pressione qualquer tecla para encerrar...')