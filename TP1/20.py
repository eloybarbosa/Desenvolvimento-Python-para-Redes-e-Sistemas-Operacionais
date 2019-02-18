import psutil
import os

part_info=psutil.disk_partitions()
cwd=os.getcwd()
current_part=os.path.splitdrive(cwd)[0]+'\\'

print('Nessa ativdade vamos mostrar algumas informações da partição corrente:\n')

for i in range(0, len(part_info)):

    if part_info[i].device==current_part:
        print('Nome:', part_info[i].device)
        print('Sistema de Arquivos:', part_info[i].fstype)
        print('Tamanho total: ', round(psutil.disk_usage(current_part).total/1073741824, 2),'GB')
        print('Espaço livre: ', round(psutil.disk_usage(current_part).free/1073741824, 2),'GB')
