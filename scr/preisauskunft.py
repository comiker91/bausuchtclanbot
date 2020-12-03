import pyautogui
import time
from datetime import datetime
import os
import string
import random
from tkinter import *
from scr import suche

werbe_stop = 0
sammler = []
erledigt = 0
ausgegeben = 0

class preisauskunft():
    def preise(welcome_label,bis,warten):
        counter = 0

        welcome_label.config(text="Preisauskunft Gestartet")
        time.sleep(warten)    

        while datetime.now().strftime('%H:%M') != bis:
            global datei, ausgegeben, erledigt
            datei =  open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            leser = datei.readlines()
            letters = string.ascii_lowercase
            spamschutz = ''.join(random.choice(letters) for i in range(3))
            if  "[SECOND CHAT]"in leser[-1]:
                if "-> Dir" in leser[-1]:
                    split = leser[-1].split("[")
                    spieler = split[6].split(" ")
                    name = spieler[0]
                    if "Info" in leser[-1]:
                        pyautogui.keyDown("Ctrl")
                        pyautogui.keyDown("a")
                        pyautogui.keyUp("a")
                        pyautogui.keyUp("Ctrl")
                        infomsgs = ("/msg "+name+" [BOT]Sende mir ein Itemname und ich antworte dir mit dem ca Preis!["+spamschutz+"]")
                        pyautogui.write(infomsgs)
                        pyautogui.keyDown("return")
                        pyautogui.keyUp("return")
                        pyautogui.keyDown("t")
                        pyautogui.keyUp("t")
                        time.sleep(1)
                    elif "!COMIKER91!" in leser[-1].upper():
                        pyautogui.keyDown("Ctrl")
                        pyautogui.keyDown("a")
                        pyautogui.keyUp("a")
                        pyautogui.keyUp("Ctrl")
                        infomsgs = ("/msg "+name+" [BOT]Ja ich bin von comiker91 Programmiert!["+spamschutz+"]")
                        pyautogui.write(infomsgs)
                        pyautogui.keyDown("return")
                        pyautogui.keyUp("return")
                        pyautogui.keyDown("t")
                        pyautogui.keyUp("t")
                        time.sleep(1)
                    elif "PSC" in leser[-1].upper():
                        print("Bot")
                    elif "PAYSAFE" in leser[-1].upper():
                        print("Bot")
                    else:
                        ausg = leser[-1]
                        teiler = ausg.split("]")
                        item = teiler[-1].strip()
                        if 2 < len(item) < 20:
                            ruck = suche.Votebot.start(item)
                            if ruck != 0:
                                pyautogui.keyDown("Ctrl")
                                pyautogui.keyDown("a")
                                pyautogui.keyUp("a")
                                pyautogui.keyUp("Ctrl")
                                pyautogui.write("/msg "+name+" [BOT] "+item+" Preis Lautet ca: "+ruck)
                                time.sleep(0.5)
                                pyautogui.keyDown("return")
                                pyautogui.keyUp("return")
                                pyautogui.keyDown("t")
                                pyautogui.keyUp("t")
                                time.sleep(1)
                                erledigt = 1
                            if erledigt == 0:
                                pyautogui.keyDown("Ctrl")
                                pyautogui.keyDown("a")
                                pyautogui.keyUp("a")
                                pyautogui.keyUp("Ctrl")        
                                pyautogui.write("/msg "+name+" [BOT]Solltest du keinen Preis erhalten haben Fehlt dieser!["+spamschutz+"]")
                                pyautogui.keyDown("return")
                                pyautogui.keyUp("return")
                                pyautogui.keyDown("t")
                                pyautogui.keyUp("t")
                                time.sleep(1)
                            else:
                                erledigt = 0                                


            datei.close()

        welcome_label.config(text="Preisauskunft Beendet!")

