
"""

Escreva um programa em Python que:
gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
gere um arquivo texto com os valores desta estrutura ordenados.

"""

import os
import time


arquivos =[]

caminho = input('Informe o caminho de um diretório: ')
print()

try:
    for nome in (os.listdir(caminho)):
        arquivo =[ nome, int(os.stat(caminho + nome).st_size)]
        arquivos.append(arquivo)
    arquivos.sort(key=lambda o: o[1], reverse=True)
    print('A relação do dos arquivos desse diretório em ordem decrescente pelo tamanho em bytes é a seguinte: \n\n')
    print('{:<30}'.format('Nome'), end='')
    print('{:<30}'.format('Tamanho em bytes'), end='\n\n')
    for x in range (len(arquivos)):
        print('{:<30}'.format(arquivos[x][0]), end='')
        print('{:<30}'.format(arquivos[x][1]), end='\n')
        
        
except (FileNotFoundError):
    print('O caminho informado não existe!')
    
now = ('Questão 03 - ' + time.strftime('%y%d%m%H%m%S') + ".txt")
    
txt = open(now, "w")
txt.write('{:<30}'.format('Nome'))
txt.write('{:<30}'.format('Tamanho em bytes'))
txt.write('\n')

for x in range (len(arquivos)):
    txt.write('{:<30}'.format(arquivos[x][0]))
    txt.write('{:<30}'.format(arquivos[x][1]))
    txt.write('\n')
    
txt.close()

print('\nFoi gerado o seguinte arquivo contendo essas informações: {} '.format(now))