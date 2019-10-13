
import tkinter as tk
import time
from random import randint
min = 0
max = 100

essais = 0
nmystere=0
##########################################
#  Les fonctions  à associer aux boutons #
##########################################
def changetext(txt):
    message['text'] = txt


def jouer():
    
    global min
    global max
    global nmystere
    nmystere = randint(min, max)
    proplb['text'] = str(nmystere)
    message['text']="je propose :"
    

def plus():
    global min
    global essais
    global nmystere
    min = nmystere
    essais =essais+1
    jouer()
    

    
def moins():
    global max
    global nmystere
    global essais
    max = nmystere
    essais = essais+1
    jouer()
    
    
def egal():
    global nmystere
    message['text'] = "le nombre mystère est :", nmystere
    
####################
###  La fenetre  ###
####################
mes ="memorisez un nombre entre 0 et 100."

fen = tk.Tk()
fen.geometry('500x200')
message = tk.Label(fen , text = mes )
message.pack()
boutoncommencer = tk.Button(fen, text = 'commencer', command = jouer)
boutonplus = tk.Button(fen , text = "c'est plus" ,width = 10 , command = plus)
boutonmoins =tk.Button (fen, text = " c'est moins" ,width = 10 , command =  moins)
boutonegal = tk.Button ( fen , text = " C'est trouvé !" , width = 10 , command = egal)
boutoncommencer.place(x=50, y = 150)
boutonplus.place(x=5, y= 30)
boutonmoins.place(x=100, y= 30)
boutonegal.place(x=200, y= 30)
proplb = tk.Label(fen, text = 'proposition:')
proplb.place(x=300 , y= 30)
label.place(x=10, y=90, width=120, height=30)
fen.mainloop()



