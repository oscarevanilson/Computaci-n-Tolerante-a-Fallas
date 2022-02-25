import psutil
import os
vivo = False
estatus = 1

while estatus == 1:
    for proc in psutil.process_iter():
        if proc.name().lower() == "pickle.py":
            vivo = True
        if vivo == False:
            os.system('pickle.py')