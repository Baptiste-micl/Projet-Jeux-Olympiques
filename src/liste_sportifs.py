from mysql.connector import connect

bdd = connect(host="localhost", user="root", password="auduse1306", database="Jeux_olympiques")

class liste_sportifs():
    cursor = bdd.cursor()
    cursor.execute("SELECT nom_sportif, prenom_sportif FROM Sportifs")
    resultat = cursor.fetchall()

    for sportifs in resultat:
        nom, prenom = sportifs
        print(nom, prenom)
    
