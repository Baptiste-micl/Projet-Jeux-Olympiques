import tkinter as tk
from mysql.connector import connect

bdd = connect(host="localhost", user="root", password="auduse1306", database="Jeux_olympiques")

class liste_sportifs():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_sportif, prenom_sportif, id_pays FROM Sportifs")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire vide
    dico_sportifs = {}

    for sportifs in resultat:
        nom, prenom, pays = sportifs
        dico_sportifs.setdefault(pays, []).append((prenom, nom)) # changements

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
        dico_disciplines[nom_discipline] = description_discipline

liste_disciplines = liste_disciplines() # ne sert à rien ?
# Ici on ajoute sportif
def ajouter_sportif(nom_sportif, prenom_sportif, id_pays, id_discipline):
    cursor = bdd.cursor()
    sql = "INSERT INTO Sportifs(nom_sportif, prenom_sportif, id_pays, id_discipline) VALUES (%s, %s, %s, %s)"
    valeurs = (nom_sportif, prenom_sportif, id_pays, id_discipline)
    cursor.execute(sql, (valeurs))
    bdd.commit()


# Ici on supprime un sportif
def supprimer_sportif(nom_sportif, prenom_sportif):
    cursor = bdd.cursor()
    sql = "DELETE FROM Sportifs WHERE nom_sportif = %s AND prenom_sportif = %s"
    valeurs = (nom_sportif, prenom_sportif)
    cursor.execute(sql, (valeurs))
    bdd.commit()
