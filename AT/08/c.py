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

import multiprocessing
import random
import time


def Factorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def Main():
    N = 1000000

    t_inicio = float(time.time())
    
    aLista = []
    bLista = []

    for i in range(N):
        aLista.append(random.randint(0, 10))

    NProc = 4

    q_entrada = multiprocessing.Queue()
    q_saida = multiprocessing.Queue()

    lista_proc = []
    for i in range(NProc):
        ini = i * int(N / NProc)  
        fim = (i + 1) * int(N / NProc) 
        q_entrada.put(aLista[ini:fim])
        p = multiprocessing.Process(target=ListFat, args=(q_entrada, q_saida))
        p.start()  
        lista_proc.append(p)  


    for i in range(0, NProc):
        bLista = q_saida.get(timeout=10)

    for p in lista_proc:
        p.join() 

    t_fim = float(time.time())
    
    print('Inicio:',t_inicio)
    print('Fim:',t_fim)
    print('\n', 'Tempo :', round(t_fim - t_inicio, 2))
    input('Digite enter para sair...')



def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return (fat)


def ListFat(q1, q2):
    l1 = q1.get()
    l2 = []
    for i in l1:
        l2.append(fatorial(l1[i]))
    q2.put(l2)



if __name__ == '__main__':
    Main()
