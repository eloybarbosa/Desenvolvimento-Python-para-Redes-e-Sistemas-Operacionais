import psutil
import datetime

print('Esta aplicação tem como função exibir as informações de um determinado PID escolhido pelo usuário, para facilitar será exibida a relação de todos os PIDs ativos no momento\n')
      
print('Segue relação dos PIDs ativos no momento:\n\n', psutil.pids())

pid = int(input('\nInsira um PID válido no qual deseja obter informações:'))

if psutil.pid_exists(pid):
    print()
    print('Nome do usuário Proprietário:', psutil.Process(pid).username())
    print('Data de Criação: ', datetime.datetime.fromtimestamp(psutil.Process(5012).create_time()).strftime('%Y-%m-%d %H:%M:%S'))
    print('Uso de memoria: ', psutil.Process(pid).memory_info().rss/1024, 'KB')
    
else:
    print()
    print('O PID informado não é válido no momento, ele não existe na relação passada ou já pode ter sido encerrado.')