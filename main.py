#  /$$$$$$  /$$
# /$$__  $$| $$
#| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$
#|  $$$$$$ | $$__  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$__  $$
# \____  $$| $$  \ $$| $$$$$$$$| $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$
# /$$  \ $$| $$  | $$| $$_____/| $$  | $$| $$      | $$  | $$| $$  | $$
#|  $$$$$$/| $$  | $$|  $$$$$$$| $$  | $$| $$      |  $$$$$$/| $$  | $$
# \______/ |__/  |__/ \_______/|__/  |__/|__/       \______/ |__/  |__/

######################################
# Importation et gestion des modules #
######################################

import os  # Importation du module "os"
import turtle  # Importation du module "turtle"
import random #Importation du module "random"

turtle.title("Shenron et les 7 boules de crystals") # Donne un titre au dessin

file = "music.mp3"  # Création de variable contenant le fichier musique à lancer
os.system(file)  # Lancer le fichier musique
t = turtle.Turtle()  # Affectation "t" à la tortue

########################################
# Configuration des paramètres de base #
########################################

turtle.bgcolor("light blue") # Choisis la couleur de l'arrière plan 
t.speed(999999)  # Configuration de la vitesse de la tortue
t.pensize(1.5)  # Configuration de l'épaisseur du crayon

color_ball = ["#ffffdd", "#fbda5a", "#ffde5f", "#fb9a17", "#fb9a17", "#ff7101"]
color_head = ["#3d8c12", "#fbc559"]

############################################################################
# Fonction permettant la consutruction de la boule aux coordonnées données #
############################################################################


def ball(x, y):  # Création de la fonction "ball(x, y)"
  """
  Permet de construire une boule aux coordonnées demandées, doivent être renseignés: la 
  coordonnée de construction "x" et la coordonnée "y" de la construction.
  """
  ########################################################
  # Téléportation de la tortue vers les coordonnées données #
  ########################################################

  t.penup()  # Arrêt de l'écriture
  t.goto(x, y)  # Téléportation vers les coordonnées souhaités
  t.pendown()  # Commencement de l'écriture

  #####################################
  # Construction du cercle par boucle #
  #####################################

  tour = 38  # Création de compteur pour créer le cercle
  while tour != 0:  # Boucle permettant la création de plusieurs cerlces
    t.color(color_ball[2])  # Selection de la couleur du cercle "orange clair"
    t.circle(tour, 360, 100)  # Construction du cercle
    tour = tour - 0.5  # Retire 0.5 au compteur "tour"

  t.goto(x, y)  # Retour aux coordonnées données au début de la fonction

  #######################################
  # Construction du reflet de la boucle #
  #######################################

  circle = 36  # Création de compteur pour créer le reflet
  while circle >= 34:  # Boucle permettant la création de multiples reflets
    t.color(color_ball[3])  # Selection de la couleur du reflet "orange"
    t.circle(circle, 125,
             100)  # Construction du demi-cercle en couleur "orange"
    t.color(color_ball[2])  # Selection de la couleur du cercle "orange clair"
    t.circle(circle, 105, 100)  # Construction de la partie invisible du cercle
    t.color(color_ball[3])  # Selectionde la couleur du reflet "orange"
    t.circle(circle, 130, 100)  # Construction de la suite du cercle "orange"
    circle = circle - 0.5  # Compteur retirant 0.5 à "circle"

  t.penup()  # Stop l'écriture


############################################################################
# Fonction permettant la consutruction de l'étoile aux coordonnées données #
############################################################################


def star(x, y):  # Création de la fonction "star(x, y)"
  """
  Permet de construire une étoile aux coordonnées demandées, doivent être renseignés: la   
  coordonnée de construction "x" et la coordonnée "y" de la construction.
  """
  ########################################################
  # Téléportation de la tortue vers les coordonnées données #
  ########################################################

  t.penup()  # Arrêt de l'écriture
  t.goto(x, y)  # Téléportation vers les coordonnées souhaités
  t.pendown()  # Commencement de l'écriture
  t.color(color_ball[3])  # Selection de la couleur du cercle "orange"

  etoile = 0  # Création de compteur pour créer l'étoile
  for i in range(13):  # Reproducion du programme dessous 13x
    t.forward(17 + etoile)  # La tortue avance de 17 + étoile dans le direction
    t.right(144)  # Change d'angle (144°)
    etoile = etoile - 1  # Retire 1 au compteur "etoile"

  t.penup()  # Arrêt de l'écriture


def body(x, y):
  """
  Permet de construir la tête aux coordonnées demandées, doivent être renseignés: la coordonnée de construction "x" et la coordonnée "y" de la construction.
  """
  t.penup()  # Arrêt de l'écriture
  t.goto(x, y)  # Téléportation vers les coordonnées souhaités
  t.pendown()  # Commencement de l'écriture
  t.color(color_head[0])  # Selection de la couleur du cercle "vert"
  t.pensize(10)  # Configuration de l'épaisseur du crayon

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(310)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(320)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(330)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(340)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(340)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(365)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(380)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(400)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(420)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(440)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(460)  # Incline la tortue pour former les différents cercles
    t.circle(40, 105, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 250, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(470)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(480)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(490)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(510)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 40  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(525)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(530)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(540)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 20  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(545)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(565)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(585)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(600)  # Incline la tortue pour former les différents cercles
    t.circle(40, 160, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 195, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(620)  # Incline la tortue pour former les différents cercles
    t.circle(40, 155, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    t.circle(40, 200, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 10  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(630)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(640)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(650)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(660)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(670)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(680)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(690)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(700)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(720)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 5  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(740)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"

  compte = 200  # Création de compteur pour créer le corps
  tour = 0  # Création de compteur pour créer le corps
  while compte > 0:  # Boucle permettant la création de multiples cercles formants le corps
    t.setheading(760 +
                 tour)  # Incline la tortue pour former les différents cercles
    t.circle(40, 250, 100)  # Construction de la suite du cercle "vert"
    t.color(color_head[1])  # Selection de la couleur du cercle "vert"
    t.circle(40, 105, 100)  # Construction de la suite du cercle "jaune"
    t.color(color_head[0])  # Selection de la couleur du cercle "jaune"
    compte = compte - 1  # Retire 1 au compteur "compte"
    tour = tour + 0.1  # Retire 1 au compteur "tour"

  t.pensize(1.5)  # Configuration de l'épaisseur du crayon

########################################
# Fonction créant la Joue du dragon    #
########################################
def Joue_Shenron(side,x,y):
  #documentation de la foncton
    """
    Fonction créant la Joue du dragon    
    :param side: str
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    CU : side == "g" or side == "r"
    """
    t.up() #lève le stylo
    t.color("#fbc559") #choisis la couleur 
    t.goto(x,y) #va au coordonnées (x,y)
    t.down() #baisse le stylo
    t.begin_fill() # début de la zone de remplissage
    t.fillcolor("#fbc559") #couleur du remplissage
    if side == "g" : #condition en fonction de side
        t.seth(-120) #choisis l'angle du stylo
        t.circle(50,80)#trace un cercle de rayon 50 et d'angle 80
        t.fd(30)#avance de 30 pixels
        t.up()
        t.goto(x,y)
        t.down()
        t.seth(255)
        t.circle(50,80)
        t.rt(50)#rotation vers la droite de 50°
        t.goto(-18.13,-57.15)
        t.end_fill()# fin du remplissage
        t.up()
        t.goto(-9.58,-90.77)
        t.down()
        t.begin_fill()
        t.fillcolor("#fbc559")
        t.seth(-85)
        t.fd(30)
        t.circle(25,80)
        t.fd(5)
        t.seth(90)
        t.fd(50)
        t.goto(-9.58,-90.77)
        t.end_fill()
    else : #condition en fonction de side 
        t.seth(-60)
        t.circle(-50,80)
        t.fd(30)
        t.up()
        t.goto(x,y)
        t.down()
        t.seth(285)
        t.circle(-50,80)
        t.lt(50)#rotation vers la gauche de 50°
        t.goto(58.13,-57.15)
        t.end_fill()
        t.up()
        t.goto(49.58,-90.77)
        t.down()
        t.begin_fill()
        t.fillcolor("#fbc559")
        t.seth(-95)
        t.fd(30)
        t.circle(-25,80)
        t.fd(5)
        t.seth(90)
        t.fd(50)
        t.goto(49.58,-90.77)
        t.end_fill()
    t.seth(0)
    
########################################
# Fonction créant le visage du dragon  #
########################################

def visage(side,x,y):
    """
    Fonction créant le visage du dragon
    :param side: str
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    CU : side == "g" or side == "r"
    """
    t.up()
    t.color("green")
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor("green")
    if side == "g" :
        t.fd(10)
        t.rt(45)
        t.fd(40)
        t.lt(50)
        t.fd(20)
        t.lt(85)
        t.fd(40)
        t.rt(45)
        t.circle(10,80)
        t.rt(50)
        t.fd(50)
        t.circle(50,80)
        t.rt(50)
        t.fd(60)
        t.circle(25,80)
        t.rt(5)
        t.fd(10)
    else :
        t.fd(10)
        t.lt(45)
        t.fd(40)
        t.rt(50)
        t.fd(20)
        t.rt(85)
        t.fd(40)
        t.lt(45)
        t.circle(-10,80)
        t.lt(50)
        t.fd(50)
        t.circle(-50,80)
        t.lt(50)
        t.fd(60)
        t.circle(-25,80)
        t.lt(5)
        t.fd(10)
    t.end_fill()
    t.up()

########################################
# Fonction créant l'oeil du dragon     #
########################################

def Oeil_Shenron(side,x,y):
    """
    Fonction créant l'oeil du dragon
    :param side: str
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    CU : side == "g" or side == "r"
    """
    t.color("red")
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor("red")
    if side == "g":
        t.lt(135)
        t.fd(50)
        t.lt(90)
        t.fd(10)
        t.circle(20,145)
        t.fd(25)
        t.rt(10)
    else :
        t.lt(180)
        t.rt(135)
        t.fd(50)
        t.rt(90)
        t.fd(10)
        t.circle(-20,145)
        t.fd(25)
        t.lt(10)
    t.end_fill()
    t.up()

########################################
# Fonction créant la corne du dragon   #
########################################

def Corne_Shenron(side,x,y):
    """
    Fonction créant la corne du dragon
    :param side: str
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    CU : side == "g" or side == "r"
    """
    t.up()
    t.color(0.78,0.53,0.36)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(0.78,0.53,0.36)
    if side == "g" :
        t.rt(45)
        t.fd(50)
        t.rt(90)
        t.fd(40)
        t.lt(90)
        t.fd(20)
        t.lt(90)
        t.fd(40)
        t.rt(90)
        t.fd(50)
        t.lt(90)
        t.fd(20)
        t.lt(90)
        t.fd(30)
        t.rt(90)
        t.fd(25)
        t.lt(90)
        t.fd(20)
        t.lt(90)
        t.fd(25)
        t.rt(90)
        t.fd(60)
    else :
        t.lt(90)
        t.fd(50)
        t.lt(90)
        t.fd(40)
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(40)
        t.lt(90)
        t.fd(50)
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(30)
        t.lt(90)
        t.fd(25)
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(25)
        t.lt(90)
        t.fd(60)
    t.end_fill()
    t.up()

########################################
# Fonction créant la bouche du dragon  #
########################################

def Bouche_Shenron ():
    """
    Fonction créant la bouche du dragon
    :return : TurtleScreen
    """
    t.color("purple")
    t.begin_fill()
    t.fillcolor("purple")
    t.goto(-9.58,-90.77)
    t.down()
    t.seth(-70)
    t.fd(20)
    t.circle(25,80)
    t.circle(25,80)
    t.end_fill()
    t.seth(0)
    t.up()

########################################
# Fonction créant la dent du dragon    #
########################################

def Dent_Shenron (x,y) :
    """
    Fonction créant la dent du dragon
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    """
    t.color("white")
    t.begin_fill()
    t.fillcolor("white")
    t.goto(x,y)
    t.down()
    t.seth(45)
    t.fd(5)
    t.seth(-45)
    t.fd(5)
    t.goto(x,y)
    t.end_fill()
    t.seth(0)

########################################
# Fonction créant l'écaille du dragon    #
########################################

def écaille(x,y):
    """
    Fonction créant l'écaille du dragon
    :param x: int or float
    :param y: int or float
    :return : TurtleScreen
    """
    t.goto(x,y)
    t.down()
    t.color("black")
    t.seth(45)
    t.circle(-5,180)
    t.up()

########################################
# Fonction créant la cerne du dragon    #
########################################

def Cerne(side):
    """
    Fonction créant la cerne du dragon
    :param side: str
    :return : TurtleScreen
    CU : side == "g" or side == "r"
    """
    t.seth(180)
    t.color("black")
    t.pensize(2)
    if side=="g":
        t.goto(-10,-10)
        t.down()
        t.fd(30)
        t.circle(-10,80)
    else:
        t.goto(50,-10)
        t.down()
        t.bk(30)
        t.circle(-10,-80)
    t.up()

########################################
# Fonction créant le nez du dragon     #
########################################

def Nez():
    """
    Fonction créant le nez du dragon
    :return : TurtleScreen
    """
    t.pensize(3)
    t.goto(10,-80)
    t.seth(135)
    t.color("black")
    t.down()
    t.fd(20)
    t.up()
    t.goto(30,-80)
    t.down()
    t.seth(45)
    t.fd(20)
    t.up()

def moustache(side):
    t.pensize(7)
    t.color("green")
    if side =="g":
        t.goto(-9.58,-90.77)
        t.seth(180)
        t.down()
        for i in range(3): #boucle se répétant 3 fois 
            t.fd(20)
            t.circle(100,60)
            t.fd(30)
            t.circle(-100,60)
    else :
        t.goto(49.58,-90.77)
        t.seth(0)
        t.down()
        for i in range(3):
            t.fd(20)
            t.circle(-100,60)
            t.fd(30)
            t.circle(100,60)
    t.up()
        
            
########################################
# Fonction créant le dragon            #
########################################

def SHENRON ():
    """
    Fonction créant le dragon
    :return : TurtleScreen
    """
    Joue_Shenron("g",-52.27,25.44) #appelle la fonction Joue_Shenron(side,x,y)
    Joue_Shenron("r",92.27,25.44)
    Bouche_Shenron ()
    x=5 #définie x = 5
    y=-120 #définie y = -120
    for i in range (6):
        Dent_Shenron (x,y)
        x+=5 #ajoute 5 à la valeur de x
    visage("r",20,100)
    visage("g",20,100)
    Oeil_Shenron("g",0,0)
    Oeil_Shenron("d",40,0)
    Corne_Shenron("g",-18.28,128.28)
    Corne_Shenron("r",58.28,128.28)
    for i in range(30):
        écaille((random.randint(-30,70)),(random.randint(40,80))) #la cordonnées x sera comprise entre -30 et 70 quant à la coordonnées y elle sera comprise entre 40 et 80 
    for i in range(30):
        écaille((random.randint(-20,55)),(random.randint(-50,-10)))
    Cerne("g")
    Cerne("r")
    Nez()
    moustache("g")
    moustache("r")

##################################################
# Fonction créant toutes les boules de crystals  #
##################################################

def création_des_boules_de_crystals ():
  """
  Fonction créant les différentes boules de crystals
  :return : TurtleScreen
  """
  ball(-90, -70)  # Construction de la première boule
  star(-90, -35)  # Construction de l'étoire de la première boule
  ball(200, -270)  # Construction de la deuxième boule
  star(225, -235)  # Consutrction de l'étoile N°1 de la deuxième boule
  star(255, -275)  # Construction de l'étoile N°2 de la deuxième boule
  star(223, -285)  # Construction de l'étoile N°3 de la deuxième boule
  ball(-320, -270)  # Construction de la troisième boule
  star(-360, -250)  # Construction de l'étoile N°1 de la troisième boule
  star(-345, -275)  # Consutrction de l'étoile N°2 de la troisième boule
  ball(230, -65)  # Consutrction de la quatrième boule
  star(250, -65)  # Consutrction de l'étoile N°1 de la quatrième boule
  star(290, -60)  # Consutrction de l'étoile N°2 de la quatrième boule
  star(290, -40)  # Consutrction de l'étoile N°3 de la quatrième boule
  star(250, -65)  # Consutrction de l'étoile N°4 de la quatrième boule
  star(250, -30)  # Consutrction de l'étoile N°5 de la quatrième boule
  ball(100, 100)  # Construction de la cinquième boule
  star(110, 130)  # Construction de l'étoire de la cinquième boule
  star(150, 130)  # Construction de l'étoire de la cinquième boule
  star(150, 90)  # Construction de l'étoire de la cinquième boule
  star(120, 90)  # Construction de l'étoire de la cinquième boule
  ball(-300, 100)  # Construction de la sixième boule
  star(-290, 120)  # Construction de l'étoire de la sixième boule
  star(-310, 130)  # Construction de l'étoire de la sixième boule
  star(-300, 150)  # Construction de l'étoire de la sixième boule
  ball(-50, -150)  # Construction de la septième boule
  star(-55, -170)  # Construction de l'étoire de la septième boule
  star(-70, -200)  # Construction de l'étoire de la septième boule*

  
  
##################################################
# Fonction permettant de réaliser tout le script #
##################################################

def invocation():
  """
  Fonction réalisant tout le script
  """
  création_des_boules_de_crystals ()
  invocation = str(input("Pressez 'o' et invoquez Shenron ou pressez 'x' et abandonnez : "))# demande à l'ulisateur d'appuyer sur une touche pour lancer un des deux scénarios
  if invocation == "o" :
    t.reset() #efface la totalité du dessin et réinisialise la tortue 
    turtle.bgcolor(0.3, 0.3, 0.3)#choisis la couleur de l'arrière plan
    t.speed(9999)
    body(0,0)
    SHENRON()
  else :
    t.reset()
    

invocation() # Construction du corps du dragon

t.penup()  # Arrêt de l'écriture

t.hideturtle()  # Cacher la tortue
try:  # Essaie de fermer le logiciel de lecture et print un message en cas d'erreur
  os.system("TASKKILL /F /IM Microsoft.Media.Player.exe")  # Fermer le logiciel musique du nom de "Microsoft.Media.Player.exe"
except:  # Action se produisant au cas ou une erreur a lieu
  print("La musique na pas pu être mise sur pause car le logiciel utilisé n'est pas \"Media Player\"")  # Print l'erreur dans le cas ou la musique n'est pas ouvert par l'application "Microsoft.Medi.Player.exe"

"""     
t.pos() #permet de connaître la position de la tortue
t.heading() #permet de connaître l'angle de la tortue
"""
##################################################
# Amélioration                                   #
##################################################

#déplacer les différentes fonctions dans des fichiers à part
#améliorer le corps du dragon
#recadrer les étoiles
#ajouter un arrière-plan (nuages , montagnes , planètes )
