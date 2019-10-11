# Chargement du module tkinter
from tkinter import * # pour Python2 se serait Tkinter


##################
#  Les constantes
###################

message  = 'hello'
compteur = 0

############################
#les fonctions
############################



def augmenter(var):
    var = var+1
    etiquette.set(str(var))
    return var


# Construction de la fenêtre principale «root»
root = Tk()
root.title('Simple exemple')
root.geometry('400x400')
# Configuration du gestionnaire de grille
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
etiquette  = Label(root, texte = 'message' )
etiquette.pack()
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=print('hello'))
startb  =Button(root, text='debut', command = augmenter)

# Placement du bouton dans «root»
qb.pack()
startb.pack()
# Lancement de la «boucle principale»
root.mainloop()