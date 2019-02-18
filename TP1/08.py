import os

print('Nesse programa vamos mostrar o tamanho de cada arquivo existente na pasta atual em KB.')

atual=os.getcwd()

print()
print('O caminho absoluto da past atual é:', os.getcwd())
print()

arquivos=os.listdir()

qtd_arquivos=len(arquivos)

for i in range (0, qtd_arquivos):
    print('Nome do arquivo:', arquivos[i], 'Tamanho:', round(os.stat(arquivos[i]).st_size/1024, 2), 'KB')

    
