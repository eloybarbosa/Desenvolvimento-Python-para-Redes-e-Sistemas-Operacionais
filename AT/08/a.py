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

resultado = []
def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  #return fat
  resultado.append(fat)

t_inicio = float(time.time())

listaFatorial = []

def criaLista(n):
    for i in range(n):
        k = random.randint(1,10)
        listaFatorial.append(k)

criaLista(1000000)



for i in listaFatorial:
    fatorial(i)


t_fim = float(time.time())


print('Inicio:',t_inicio)
print('Fim:',t_fim)
t_total = t_fim - t_inicio
print('\n','Tempo:',round(t_total,2),'segundos.')