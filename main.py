from os import symlink
from sys import audit
import time
from scr import auslesen,scammpreiskombi, scammer, preisauskunft
from datetime import datetime
from tkinter import *
import threading

warten = 0.0


def init():
    
    global warten
    lesen = auslesen.auslesen.config()  
    warten = lesen[0]
 
def preiseauskunfts(*event):
    global welcome_label, warten
    bis = zeit_eingabe.get()
    if bis == "":
        welcome_label.config(text="Wir konnten keine Zeit erkennen! Programm erneut starten!")
    else:
        preisauskunft.preise(welcome_label,bis,warten)

def scammabfrages(*event):
    global welcome_label, warten
    bis = zeit_eingabe.get()
    if bis == "":
        welcome_label.config(text="Wir konnten keine Zeit erkennen! Programm erneut starten!")
    else:
        scammer.scammabfrage.scammer(welcome_label,bis,warten)

def kombi(*event):
    global welcome_label, warten
    bis = zeit_eingabe.get()
    if bis == "":
        welcome_label.config(text="Wir konnten keine Zeit erkennen! Programm erneut starten!")
    else:
        scammpreiskombi.scammabfrage.scammer(welcome_label,bis,warten)
    


init()

fenster = Tk()
fenster.title("Bot Steuerung")


# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menüleisten
datei_menu = Menu(menuleiste, tearoff=0)

#Menüleisten Inhalte
datei_menu.add_command(label="Preisauskunft", command=threading.Thread(target=preisauskunft).start)
datei_menu.add_command(label="Scammabfrage", command=threading.Thread(target=scammabfrages).start)
datei_menu.add_command(label="Scamm/Preis", command=threading.Thread(target=kombi).start)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Beenden", command=exit)



# "Drop-Down-Menü"
menuleiste.add_cascade(label="Datei", menu=datei_menu)


my_label1 = Label(fenster, text="Zeit Bis wann:")
# In diesem Label wird nach dem Klick auf den Button der Benutzer
# mit seinem eingegebenen Namen begrüsst.
welcome_label = Label(fenster)
welcome_label.config(text="Willkommen!")

# Hier kann der Benutzer eine Eingabe machen
zeit_eingabe = Entry(fenster, bd=5, width=40)


#Buttons
preis_button = Button(fenster, text="Preisauskunft", command=threading.Thread(target=preiseauskunfts).start)
scamm_button = Button(fenster, text="Scammabfrage", command=threading.Thread(target=scammabfrages).start)
kombi_button = Button(fenster, text="Scamm/Preis", command=threading.Thread(target=kombi).start)
exit_button = Button(fenster, text="Exit", command=exit)


#Fensterlayout
fenster.config(menu=menuleiste)
my_label1.grid(row = 0, column = 0)
zeit_eingabe.grid(row = 0, column = 1)
preis_button.grid(row=2, column=0)
scamm_button.grid(row=2, column=1)
kombi_button.grid(row=2, column=2)
exit_button.grid(row = 2, column = 3)
welcome_label.grid(row = 3, column = 0, columnspan = 2)



fenster.mainloop()
