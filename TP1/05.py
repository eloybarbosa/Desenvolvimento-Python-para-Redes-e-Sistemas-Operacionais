import os

file = input('Insira o nome do arquivo que gostaria de verificar a existência:')
if os.path.exists(file):
    if os.path.isfile(file):
        print(file, 'existe e é um arquivo!')
    else:
        print(file, 'existe mas não é um arquivo!')
    
else:
    print(file, 'não existe!')