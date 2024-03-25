import tkinter as tk
from mysql.connector import connect

bdd = connect(host="localhost", user="root", password="auduse1306", database="Jeux_olympiques")

class liste_sportifs():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_sportif, prenom_sportif FROM Sportifs")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire vide
    dico_sportifs = {}

    for sportifs in resultat:
        nom, prenom = sportifs
        # Ajout des valeurs au dictionnaire avec les clés "nom" et "prenom"
        dico_sportifs[nom] = {prenom}

    print(dico_sportifs)

liste_sportifs = liste_sportifs()

class liste_disciplines():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_discipline, description_discipline FROM Disciplines")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire vide
    dico_disciplines = {}

    for disciplines in resultat:
        nom_discipline, description_discipline = disciplines
        # Ajout des valeurs au dictionnaire avec les clés "nom_discipline" et "description_discipline"
        dico_disciplines[nom_discipline] = {description_discipline}

    print(dico_disciplines)

liste_disciplines = liste_disciplines()
