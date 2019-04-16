"""

Escreva 3 programas em Python que resolva o seguinte problema:
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.

Para calcular o fatorial, utilize a seguinte função:

  

  def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)
  

Os modos de desenvolver seu programa devem ser:

a. sequencialmente (sem concorrência);
b. usando o módulo threading com 4 threads;
c. usando o módulo multiprocessing com 4 processos.

"""

import time
import random
import threading

def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return (fat)


def listaFatorial(lista, inicio, fim):
    for i in range(inicio, fim):
        bLista.append(fatorial(lista[i]))


t_inicio = float(time.time())
N = 1000000

aLista = []
bLista = []
for i in range(N):
    aLista.append(random.randint(0, 10))

Nthreads = 4
lista_threads = []
for i in range(Nthreads):
    ini = i * int(N / Nthreads)
    fim = (i + 1) * int(N / Nthreads)
    t = threading.Thread(target=listaFatorial, args=(aLista, ini, fim))
    t.start()
    lista_threads.append(t)

for t in lista_threads:
    t.join()

t_fim = float(time.time())
print('Inicio:',t_inicio)
print('Fim:',t_fim)
print('\n','Tempo:', round(t_fim - t_inicio,2))
