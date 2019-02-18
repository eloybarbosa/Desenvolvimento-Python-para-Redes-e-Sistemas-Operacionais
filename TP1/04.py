import os

file = input('Insira o nome de um arquivo para saber o seu caminho absoluto:')

if os.path.exists(file):
    if os.path.isfile(file):
        print ('O caminho absoluto do arquivo citado é:', os.path.abspath(file))
    else:
        print ('O caminho absoluto da pasta citada é:', os.path.abspath(file))
    
else:
    print(file, 'não existe! Portanto não será exibido o caminho absoluto.')