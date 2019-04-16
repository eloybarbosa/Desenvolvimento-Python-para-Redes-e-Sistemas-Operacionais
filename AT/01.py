"""

Escreva um programa em Python que:
obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
imprima o nome do processo e seu PID;
imprima também o percentual de uso de CPU e de uso de memória.

"""

import psutil

print("{:10} {:30} {:10} {:10}".format("PID", "Nome", "Memoria", "Cpu"))

for pid in psutil.pids():
    try:
        processo = {}
        p = psutil.Process(pid)
        pid = pid
        nome = p.name()
        mem = round(p.memory_percent(), 2)
        cpu = p.cpu_percent(interval=0.01)
        print("{:<10} {:30} {:<10} {:<10}".format(pid, nome, mem, cpu))
    except:
        pass
