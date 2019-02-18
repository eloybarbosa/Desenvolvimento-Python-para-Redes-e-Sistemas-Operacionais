import psutil
import time

processador = psutil.cpu_times_percent(percpu=True)

print('Nessa atividade vamos mostrar de segundo a segundo por 20 vezes o percentual de uso da CPU:\n')

for n in range (20):
    time.sleep(1)
    print('\nRepetição:', n+1)
    for i in range (4):
        print('Núcleo', i+1, time.sleep(0.1), 'Modo Usuário:', psutil.cpu_times_percent(percpu=True)[i][0],'%', time.sleep(0.1), 'Modo Sistema: ', psutil.cpu_times_percent(percpu=True)[i][1], time.sleep(0.1), 'Tempo de Inatividade:', psutil.cpu_times_percent(percpu=True)[i][2])
        
        
 