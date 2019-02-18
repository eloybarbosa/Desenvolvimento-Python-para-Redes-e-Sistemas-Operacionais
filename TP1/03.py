#3. Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo e também seu GID (identificador de grupo) caso seja sistema do tipo Linux.

import os

print('O PID do processo atual é:', os.getpid())

print()
input('Pressione qualquer tecla para encerrar...')