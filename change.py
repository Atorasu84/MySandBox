from Utilitaires.Utilitaires import *
from TP1.TP1_1 import tp1_1
from TP1.TP1_2 import tp1_2
from TP1.TP1_3 import tp1_3
from TP1.TP1_4 import tp1_4
from TP1.TP1_5 import tp1_5


def menu():
    while (True):
        print("Choisir le exercice a faire  1,2,3,4,5 (0 pour quitter ) ")
        print("1 - Surface Trapeze")
        print("2 - Somme")
        print("3 - Factorielle")
        print("4 - Table de Multiplication")
        print("5 - Calcul de Credit")
        print("0 - quitter\n\n")
        n = input("Numéro de l'exercices choisi: ")
        if n == "0":
            print("Bye, A bientot!")
            break;
        elif n == "1":
            tp1_1()
            pause()
        elif n == "2":
            tp1_2()
            pause()
        elif n == "3":
            tp1_3()
            pause()
        elif n == "4":
            tp1_4()
            pause()
        elif n == "5":
            tp1_5()
            pause()
        else :
            print("le choix rentrer n'existe pas")

Ceci est les un exemple
