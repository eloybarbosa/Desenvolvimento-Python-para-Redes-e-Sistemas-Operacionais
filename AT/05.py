"""

Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:

a.txt
1 15 -42 33 -7 -2 39 8

b.txt	
19 56 -43 23 -7 -11 33 21 61 9

Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente.
Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.

"""

try:
    a = open("a.txt", "r")
    b = open("b.txt", "r")
    lista_a = []
    lista_b = []
    resultado = []
    for x in a:
        lista_a = x.split(" ")
    for y in b:
        lista_b = y.split(" ")

    print('a.txt : ', ' '.join(map(str, lista_a)))
    print('b.txt : ', ' '.join(map(str, lista_b)))

    A=len(lista_a)
    B=len(lista_b)

    if A < B:
        ab= B-A
        for x in range (ab):
            lista_a.append('0')
    else:
        ba=A-B
        for y in range (ba):
            lista_b.append('0')
            
    for i in range (len(lista_a)):
        r = int(lista_a[i]) + int(lista_b[i])
        resultado.append(r)
        
    print('\nA soma dos dois arquivos é: ', resultado )
    
except Exception as erro:
    print(str(erro))
        
    
        

    