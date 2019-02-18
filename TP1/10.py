import os
executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe'
os.spawnl(os.P_NOWAIT, executavel_com_path, " ")