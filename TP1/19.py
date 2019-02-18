import psutil
part_sys='c:'
print('O espaço livre na partição do sistema é : ', round(psutil.disk_usage(part_sys).free/1073741824, 2),'GB')
