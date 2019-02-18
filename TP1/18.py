import psutil

print('Nesta atividade vamos exibir informações sobre a memória principal e sobre a memória de paginação:\n')
print('Memória principal:\n')
print('Total:', round(psutil.virtual_memory().total/1073741824, ),'GB')
print('Usada:', round(psutil.virtual_memory().used/1073741824, ),'GB')
print('Livre:', round(psutil.virtual_memory().free/1073741824, ),'GB')
print('Percentual de uso:', psutil.virtual_memory().percent,'%\n')
print('Memória de paginação:\n')
print('Total:', round(psutil.swap_memory().total/1073741824, ),'GB')
print('Usada:', round(psutil.swap_memory().used/1073741824, ),'GB')
print('Livre:', round(psutil.swap_memory().free/1073741824, ),'GB')
print('Percentual de uso:', psutil.virtual_memory().percent, '%')