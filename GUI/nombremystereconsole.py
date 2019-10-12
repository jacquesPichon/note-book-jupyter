import time
from random import randint

############################
## variables              ##
############################

min = 0
max = 100
essais = 0
reponse = ''

############################
## PROGRAMME PRINCIPAL    ##
############################

print("Mémorisez un nombre entre 0 et 100")
print("Je vais essayer de le retrouver ")
time.sleep(3)

print("je commence à chercher votre nombre mystère.")
while (essais <=10) and reponse !="=":
    proposition = randint (min, max)
    print (proposition)
    message = str(proposition) + "est-il- plus grand (+) ou plus petit(-) ou égale au nombre à deviner (=) ?"
    reponse = input (message)
    if reponse =="+":
        min=proposition
        essais =essais + 1
    if reponse == "-":
        max = proposition
        essais =essais + 1


if essais >=10:
    print ("l'ordinateur n'a pas trouvé le nombre en 10 essais...")
else:
    print ("le nombre est : ", proposition," j'ai trouvé en ", essais, "tentatives.")