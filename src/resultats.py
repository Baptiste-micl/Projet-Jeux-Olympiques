import tkinter as tk
from mysql.connector import connect

bdd = connect(host="localhost", user="root", password="auduse1306", database="Jeux_olympiques")

class resultat_pays():
    cursor = bdd.cursor()
    cursor.execute("SELECT id_pays, medaille_or, medaille_argent, medaille_bronze FROM Resultats")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire vide
    dico_resultat_pays = {}

    for resultat_pays in resultat:
        id_pays, medaille_or, medaille_argent, medaille_bronze = resultat_pays
        # Ajout des valeurs au dictionnaire avec les clés 
        dico_resultat_pays[id_pays] = {medaille_or, medaille_argent, medaille_bronze}

resultat_pays = resultat_pays()

class resultat_discipline():
    cursor = bdd.cursor()
    cursor.execute("SELECT id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze FROM Resultats")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire vide
    dico_resultat_disciplines = {}

    for resultat_disciplines in resultat:
        id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze = resultat_disciplines
        # Ajout des valeurs au dictionnaire avec les clés 
        dico_resultat_disciplines[id_pays] = {id_discipline, medaille_or, medaille_argent, medaille_bronze}

resultat_discipline = resultat_discipline()
