"""

Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.

"""
import os
arquivo=input("Entre com o nome do arquivo: ")
os.system('notepad.exe ' + arquivo)



 