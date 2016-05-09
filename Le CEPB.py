""""
  ### Commentaire
  ### Commentaire
  ### Commentaire

Titre =  le compte est presque Bon !!

Date:  02/05/2016  -  14:03:00

    Fonctions :


Fonction Quitter():

    # Fonction boite de dialogue !
    #   fermeture du programme
    #

######################################################################################################
Fonction Message(message, contenu):

    # Fonction boite de dialogue !
    #   Recommencer la partie + Message fin de jeu
    #  Quitter le programme

######################################################################################################
Fonction recommencer():
    # Appel de la fonction Message
    # intialisation des variables
    # initialisation des labels d'affichage

######################################################################################################
Fonction aide():
    # Boite de dialogue pour afficher les rÃ¨gles du jeu

######################################################################################################
Fonction affichage(nombre):
    # Permet d'afficher le texte au clique (Label operation )
######################################################################################################
Fonctions num1 -> num10
    Appel la fonction Affichage !!

######################################################################################################

Fonction addition():

Fonction soustraction():

Fonction multiplication():

Fonction division():

######################################################################################################
Fonction egal():

        Calcul les nombres entrÃ©e et le rÃ©sultat et revoi le resultat totlal dans le label (Label Resultat )

######################################################################################################
Fonction game(resultat):

        Compare le nombre gÃ©nerer et le nombre calculÃ©

                si le nombre gÃ©nÃ©rÃ© == nombre calculÃ©
                    # Appel la fonction Message => Le jeu est gagnÃ©
                Sinon
                    # -1 dans le nombre de tentative

Varaibles :

Nbr1 => Variable qui contient la valeur de chaque clique de bouton

Nbr2 => Initialiser a 0 est le resultat temporaire de chaque operation

operateur = contient le signe des operations + - x /

resultat => Resultat definitive des operation

nbrTentative => Nombre de Tentative Restant initialiser a 10
                ArrivÃ© a 0 -> Le jeu est arrete

nbrgenerer => Nombre AlÃ©atoire gÃ©nÃ©rer entre 1 et 999 au commencement de chaque partie

     __       _
    / \      / \
    \__\    /__/
      ___XX___
       \wwww/

"""
from tkinter import *
from tkinter.messagebox import *
from random import randint

# Fenetre du jeu
main = Tk()
main.geometry("500x500+100+100")
main.title("Le compte est bon ")
main["bg"] = "#EA0C39"

Nbr2 = 0
nbrTentative = 7
nbrgenerer = randint(1, 999)


#####################################################################################################

def Quitter():
    if askyesno('Question', "Voulez vous quitter le jeu"):
        main.destroy()


######################################################################################################

def Message(message, contenu):
    if askyesno(message, contenu):
        recommencer()
    else:
        main.destroy()


######################################################################################################
def recommencer():
    global nbrTentative, nbrgenerer, Nbr2, Nbr1, operateur
    nbrTentative = 10
    nbrgenerer = randint(1, 999)
    Nbr2 = 0
    Nbr1 = ""
    operateur = ""
    LblResultat["text"] = "0"
    Lbloperation["text"] = ""
    LblNbrTentative["text"] = "Nombre de tentative restant : " + str(nbrTentative)
    LblNbrGenerer["text"] = nbrgenerer
    LblProcedure["text"] = ""


######################################################################################################

def aide():
    showinfo("A propos", "Comment Jouer :"
                         "\n RÃ¨les du jeu : "
                         "\n 0 inspiration "
                         "\n 0 inspiration "
                         "\n 0 inspiration "
                         "\n 0 inspiration "
                         "\n\n Copyright: -- 2016 -- "
                         "\n bln bla bla ")


######################################################################################################
def affichage(nombre):
    global Nbr1
    Lbloperation["text"] = str(nombre)
    Nbr1 = nombre


######################################################################################################
def num1():
    affichage("5")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=10, y=100)

def num2():
    affichage("1")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=60, y=100)

def num3():
    affichage("2")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=110, y=100)

def num4():
    affichage("3")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=160, y=100)

def num5():
    affichage("4")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=210, y=100)

def num6():
    affichage("10")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=10, y=150)

def num7():
    affichage("100")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=60, y=150)

def num8():
    affichage("50")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=110, y=150)
    
def num9():
    affichage("20")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=160, y=150)

def num10():
    affichage("7")
    btnNombre1 = Button(main, text="X", height=2, width=5, state=DISABLED, command=num1).place(x=210, y=150)

######################################################################################################

def addition():
    global operateur, Nbr1, Nbr2
    operateur = "+"
    Lbloperation["text"] = "+"


def soustraction():
    global operateur, Nbr1, Nbr2
    operateur = "-"
    Lbloperation["text"] = "-"


def multiplication():
    global operateur, Nbr1, Nbr2
    operateur = "x"
    Lbloperation["text"] = "x"


def division():
    global operateur, Nbr1, Nbr2
    operateur = "/"
    Lbloperation["text"] = "/"
    
def carre() :
    global operateur,Nbr1, Nbr2
    operateur = "**"
    Lbloperation["text"] = "**"

######################################################################################################
def egal():
    global operateur, Nbr1, Nbr2
    Nbr1 = float(Nbr1)
    if operateur == "+":
        resultat = round(Nbr2 + Nbr1, 1)
        LblResultat["text"] = str(resultat)
        LblProcedure["text"] += str(Nbr2) + operateur + str(Nbr1)+ "=" + str(resultat) + "\n"
        Nbr2 = resultat
        game(resultat)
    elif operateur == "-":
        resultat = round(Nbr2 - Nbr1, 1)
        LblResultat["text"] = str(resultat)
        LblProcedure["text"] += str(Nbr2) + operateur + str(Nbr1)+ "=" + str(resultat) + "\n"
        Nbr2 = resultat
        game(resultat)
    elif operateur == "x":
        resultat = round(Nbr2 * Nbr1, 1)
        LblResultat["text"] = str(resultat)
        LblProcedure["text"] += str(Nbr2) + operateur + str(Nbr1)+ "=" + str(resultat) + "\n"
        Nbr2 = resultat
        game(resultat)
    elif operateur == "/":
        resultat = round(Nbr2 / Nbr1, 1)
        LblResultat["text"] = str(resultat)
        LblProcedure["text"] += str(Nbr2) + operateur + str(Nbr1)+ "=" + str(resultat) + "\n"
        Nbr2 = resultat
        game(resultat)
    elif operateur == "**":
        resultat= round(Nbr2 ** Nbr1, 1)
        LblResultat["text"] = str(resultat)
        LblProcedure["text"] += str(Nbr2) + operateur + str(Nbr1)+ "=" + str(resultat) +"\n"
        Nbr2 = resultat
        game(resultat)
    else:
        resultat = Nbr2
        LblResultat["text"] = str(resultat)

    Lbloperation["text"] = ""
    Nbr1 = ""
    operateur = ""


######################################################################################################
def game(resultat):
    global nbrTentative
    if resultat == nbrgenerer:
        Message("GagnÃ©", "Vous avez gagnÃ© \n Voulez vous recommencer")
    else:
        nbrTentative -= 1
        LblNbrTentative["text"] = "Nombre de tentative restant : " + str(nbrTentative)

    if nbrTentative == 0:
        Message("perdu", "Vous avez perdu \n Voulez vous recommencer")


############################   Boutons nombres  -   Boutons Addition - Soustraction - Multiplication - Division   #####################################

btnNombre1 = Button(main, text="5", height=2, width=5, command=num1).place(x=10, y=100)
btnNombre2 = Button(main, text="1", height=2, width=5, command=num2).place(x=60, y=100)
btnNombre3 = Button(main, text="2", height=2, width=5, command=num3).place(x=110, y=100)
btnNombre4 = Button(main, text="3", height=2, width=5, command=num4).place(x=160, y=100)
btnNombre5 = Button(main, text="4", height=2, width=5, command=num5).place(x=210, y=100)

btnNombre6 = Button(main, text="10", height=2, width=5, command=num6).place(x=10, y=150)
btnNombre7 = Button(main, text="100", height=2, width=5, command=num7).place(x=60, y=150)
btnNombre8 = Button(main, text="50", height=2, width=5, command=num8).place(x=110, y=150)
btnNombre9 = Button(main, text="20", height=2, width=5, command=num9).place(x=160, y=150)
btnNombre10 = Button(main, text="7", height=2, width=5, command=num10).place(x=210, y=150)

btnOperation1 = Button(main, text="+", height=2, width=5, command=addition).place(x=300, y=100)
btnOperation2 = Button(main, text="-", height=2, width=5, command=soustraction).place(x=350, y=100)
btnOperation3 = Button(main, text="x", height=2, width=5, command=multiplication).place(x=300, y=150)
btnOperation4 = Button(main, text="/", height=2, width=5, command=division).place(x=350, y=150)
btnOperation5 = Button(main, text="**",height=2, width=5, command=carre).place(x=400, y=100)
btnEgal = Button(main, text="=", height=3, width=12, command=egal).place(x=300, y=200)

LblNbrGenerer = Label(main, text=nbrgenerer)
LblNbrGenerer.place(x=250, y=300)

LblNbrTentative = Label(main, text="Nombre de tentative restant : " + str(nbrTentative))
LblNbrTentative.place(x=10, y=30)
LblNbrTentative["bg"] = "#EA0C39"
LblNbrTentative["fg"] = "#FFF"

Lbloperation = Label(main, text="0")
Lbloperation.place(x=50, y=250)

LblResultat = Label(main, text="0")
LblResultat.place(x=50, y=300)

btnAide = Button(main, text="A propos", command=aide).place(x=5, y=5)
btnQuitter = Button(main, text="Quitter", command=Quitter).place(x=440, y=460)
LblProcedure = Label(main, text="")
LblProcedure.place(x=50, y=350)

main.mainloop()
