import pyautogui
import time
from datetime import datetime
import os
import string
import random
from tkinter import *

werbe_stop = 0
sammler = []
erledigt = 0
ausgegeben = 0

class scammabfrage():
    def scammer(welcome_label,bis,warten):
        counter = 0

        welcome_label.config(text="Scammabfrage Gestartet")
        time.sleep(warten)
        gestartet = int(datetime.now().strftime('%M'))
        rechner = (20)
        ausgabe = []
        hinzu = gestartet+rechner
        if hinzu > 60:
            hinzu = hinzu-60
        ausgabe.append(hinzu)     

        while datetime.now().strftime('%H:%M') != bis:
            global datei, ausgegeben, werbe_stop, erledigt
            datei =  open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            leser = datei.readlines()
            letters = string.ascii_lowercase
            spamschutz = ''.join(random.choice(letters) for i in range(3))

            if  "[SECOND CHAT]"in leser[-1]:
                if "-> Dir" in leser[-1]:

                    if "INFO" in leser[-1].upper():
                        pyautogui.keyDown("Ctrl")
                        pyautogui.keyDown("a")
                        pyautogui.keyUp("a")
                        pyautogui.keyUp("Ctrl")
                        infomsgs = ("/r [BOT]Sende mir ein Itemname und ich antworte dir mit dem ca Preis!["+spamschutz+"]")
                        pyautogui.write(infomsgs)
                        pyautogui.keyDown("return")
                        pyautogui.keyUp("return")
                        pyautogui.keyDown("t")
                        pyautogui.keyUp("t")
                        time.sleep(1)
                    elif "ADD" in leser[-1].upper():
                        with open('scammer.txt','a', encoding="utf-8") as scammerliste:
                            ausg = leser[-1]
                            teiler = ausg.split(" ")
                            spieler = teiler[-4].strip().upper()
                            scammerliste.write(spieler+" = "+teiler[-1]+"\n")
                            scammerliste.close()
                            pyautogui.keyDown("Ctrl")
                            pyautogui.keyDown("a")
                            pyautogui.keyUp("a")
                            pyautogui.keyUp("Ctrl")
                            pyautogui.write("/r [BOT]Du hast "+spieler+" mit: "+leser[-1]+" eingetragen!")
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
                        infomsgs = ("/r [BOT]Ja ich bin von comiker91 Programmiert!["+spamschutz+"]")
                        pyautogui.write(infomsgs)
                        pyautogui.keyDown("return")
                        pyautogui.keyUp("return")
                        pyautogui.keyDown("t")
                        pyautogui.keyUp("t")
                        time.sleep(1)                              
                    else:
                        ausg = leser[-1]
                        teiler = ausg.split(" ")
                        spieler = teiler[-2].strip().upper()
                        with open('scammer.txt','r', encoding="utf-8") as scammerliste:
                            alle = scammerliste.readlines()
                            sammler.append(alle)
                        for i in alle:
                            such = i.strip().split("=")
                            if spieler == such[0].strip():
                                pyautogui.keyDown("Ctrl")
                                pyautogui.keyDown("a")
                                pyautogui.keyUp("a")
                                pyautogui.keyUp("Ctrl")
                                pyautogui.write("/r [BOT]Der Spielereintrag von "+spieler+" Lautet: "+such[1])
                                pyautogui.keyDown("return")
                                pyautogui.keyUp("return")
                                pyautogui.keyDown("t")
                                pyautogui.keyUp("t")
                                time.sleep(1)
                                erledigt = 1
                                break
                        if erledigt == 0:
                            scammerliste.close()
                            pyautogui.keyDown("Ctrl")
                            pyautogui.keyDown("a")
                            pyautogui.keyUp("a")
                            pyautogui.keyUp("Ctrl")        
                            pyautogui.write("/r [BOT]Es liegen keine Eintreage vor von "+spieler+" !["+spamschutz+"]")
                            pyautogui.keyDown("return")
                            pyautogui.keyUp("return")
                            pyautogui.keyDown("t")
                            pyautogui.keyUp("t")
                            time.sleep(1)
                        else:
                            scammerliste.close()
                            erledigt = 0                                


            datei.close()

        welcome_label.config(text="Scammabfrage Beendet!")

