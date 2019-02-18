import psutil

cpu=(psutil.cpu_times(percpu=True))

num_core=len(cpu)

print('Nessa atividade vamos ver as principais informações sobre o tempo da CPU em segundos por núcleo:')

for n in range (0, num_core):
    print('\nNúcleo', n+1, ':', '\nModo Usuário:', round(cpu[n][0]/1000, 1,),'segundos',
          '\nModo Sistema: ', round(cpu[n][1]/1000, 1,),'segundos',
          '\nTempo de Inatividade: ', round(cpu[n][2]/1000, 1,),'segundos',)