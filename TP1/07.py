import os

file = input('Insira o nome do arquivo que gostaria de verificar o seu caminho absoluto:')
if os.path.exists(file):
    if os.path.isfile(file):
        ext=os.path.abspath(file)
        caminho=os.path.split(ext)
        print('O caminho absoluto arquivo informado é:', caminho[0])
    else:
        print(file, 'existe mas não é um arquivo!')
    
else:
    print(file, 'não existe!')