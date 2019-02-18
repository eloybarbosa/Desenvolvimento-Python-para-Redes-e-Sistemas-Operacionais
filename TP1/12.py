#exemplo de criação de um processo externo com o modulo os.

import os

processo = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
os.startfile(processo)

#exemplo de criação de um processo  externocom o modulo subprocess.

import subprocess

subprocess.run("calc")