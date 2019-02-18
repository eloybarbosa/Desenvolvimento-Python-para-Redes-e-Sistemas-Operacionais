import os

file = input('Insira o nome do arquivo que gostaria de verificar a extenção:')
if os.path.exists(file):
    if os.path.isfile(file):
        ext=os.path.splitext(file)
        print('A exetenção do arquivo informado é:', ext[-1])
    else:
        print(file, 'existe mas não é um arquivo!')
    
else:
    print(file, 'não existe!')