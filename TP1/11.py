import os

file = input('Insira o nome do arquivo de texto (com a extenção) que deseja abrir:')

if os.path.exists(file):
    if os.path.isfile(file):
        ext=os.path.splitext(file)
        if ext[-1] >= '.txt':
            os.startfile(file)
        else:
            print(file, 'existe mas não é um arquivo de texto!')
    else:
        print(file, 'existe mas não é um arquivo.')
    
else:
    print(file, 'não existe!')
#os.startfile('tp1.txt')
