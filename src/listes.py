import tkinter as tk
from mysql.connector import connect

# Connexion à la base de données MySQL
bdd = connect(host="localhost", user="root", password="root", database="Jeux_olympiques")

# Classe pour récupérer la liste des sportifs
class liste_sportifs():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_sportif, prenom_sportif, id_pays FROM Sportifs")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire pour stocker les sportifs
    dico_sportifs = {}
    for sportifs in resultat:
        nom, prenom, pays = sportifs
        dico_sportifs.setdefault(pays, []).append((prenom, nom))

# Classe pour récupérer la liste des sportifs
class liste_disciplines():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_discipline, description_discipline FROM Disciplines")
    resultat = cursor.fetchall()

    # Création d'un dictionnaire pour stocker les disciplines et leurs descriptions
    dico_disciplines = {}
    for disciplines in resultat:
        nom_discipline, description_discipline = disciplines
        dico_disciplines[nom_discipline] = description_discipline

# Ici on ajoute le sportif à la base de données
def ajouter_sportif(nom_sportif, prenom_sportif, id_pays, id_discipline):
    cursor = bdd.cursor()
    sql = "INSERT INTO Sportifs(nom_sportif, prenom_sportif, id_pays, id_discipline) VALUES (%s, %s, %s, %s)"
    valeurs = (nom_sportif, prenom_sportif, id_pays, id_discipline)
    cursor.execute(sql, (valeurs))
    bdd.commit()


# Ici on supprime un sportif de la base de données
def supprimer_sportif(nom_sportif, prenom_sportif):
    cursor = bdd.cursor()
    sql = "DELETE FROM Sportifs WHERE nom_sportif = %s AND prenom_sportif = %s"
    valeurs = (nom_sportif, prenom_sportif)
    cursor.execute(sql, (valeurs))
    bdd.commit()
