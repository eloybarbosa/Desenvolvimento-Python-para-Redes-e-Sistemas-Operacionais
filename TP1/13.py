import subprocess

processo = subprocess.Popen("notepad")
print("O PID do processo criado é:", processo.pid)
