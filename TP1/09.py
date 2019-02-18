import os
import datetime

print('Nesse programa vamos mostrar a data de criação e a data da ultima mofificação dos arquivos que estão no diretório atual.')

atual=os.getcwd()

print()
print('O caminho absoluto o diretório atual é:', os.getcwd())
print()

arquivos=os.listdir()

qtd_arquivos=len(arquivos)

for i in range (0, qtd_arquivos):
    print('Nome do arquivo:', arquivos[i], 'Data de Criação:', datetime.datetime.fromtimestamp(os.stat(arquivos[i]).st_ctime).strftime('%Y-%m-%d %H:%M:%S'), 'Data da Ultima Modificação:', datetime.datetime.fromtimestamp(os.stat(arquivos[i]).st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
