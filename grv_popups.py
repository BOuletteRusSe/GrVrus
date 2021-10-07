from pyautogui import position
from autoit import win_move
from PIL import ImageTk, Image as Img
from time import sleep
from threading import Thread
from random import randint, choice
from tkinter import *

steps_cooldown = {1: 5, 2: 20, 3: 30, 4: 36}

class Popup:
    
    def __init__(self, window_type):
        
        self.popup = window_type
        self.images = list()
        
        for image in range(18):
            self.images.append(ImageTk.PhotoImage(Img.open(f"assets/img.{image}.png")))
            
        self.popup.geometry(f"{randint(0, position()[0])}x{randint(0, position()[1])}")
        self.popup.overrideredirect(1)
        self.popup.title("Popup")
        self.popup.configure(background='black')
        
        self.canvas = Canvas(self.popup, highlightthickness=0, bg="black")
        self.canvas.create_image(0, 0, image=choice(self.images))
        
        self.canvas.pack()
        self.popup.update()
        
        win_move("Popup", randint(0, position()[0]), randint(0, position()[1]))
        
    def MainLoop(self):
           
        while True:
            try: self.popup.update()
            except: continue

def PopupLoop():
    
    global popup
    
    while True:
        try: popup.MainLoop()
        except: continue

def PopupWhile():
    
    global popup
    
    popup = Popup(Tk())
    
    while True:
        
        sleep(2)
        del popup
        popup = Popup(Toplevel())
        
              

threads = list()
threads.append(Thread(target=PopupWhile))
for t in threads: t.start()
for t in threads: t.join()
