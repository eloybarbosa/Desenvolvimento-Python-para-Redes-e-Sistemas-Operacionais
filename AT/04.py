"""

Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
arquivo.txt

Bom dia
Você pode falar agora?

Resultado na tela:

?aroga ralaf edop êcoV
aid moB

"""


try:
    arq = open("arquivo.txt", "r")
    lista = []
    for linha in arq:
        lista.append(linha[::-1])
    print('\n'.join(map(str, lista[::-1]))) 
    arq.close()
except Exception as erro:
    print(str(erro))