from mysql.connector import connect

# Connexion à la base de données MySQL
bdd = connect(host="localhost", user="root", password="root", database="Jeux_olympiques")

# Classe pour récupérer les résultats par pays
class resultat_pays():
    cursor = bdd.cursor()
    cursor.execute("""SELECT nom_pays AS Pays,
                   FORMAT(SUM(medaille_or), 0) AS "Or",
                   FORMAT(SUM(medaille_argent), 0) AS "Argent",
                   FORMAT(SUM(medaille_bronze), 0) AS "Bronze"
                   FROM Resultats
                   JOIN Pays ON Pays.id_pays = Resultats.id_pays
                   GROUP BY Pays.nom_pays
                   ORDER BY Pays.nom_pays;
                   """)
    resultat = cursor.fetchall()

    # Création d'un dictionnaire pour stocker les résultats par pays
    dico_resultat_pays = {}
    for resultat_pays in resultat:
        Pays, Or, Argent, Bronze = resultat_pays 
        dico_resultat_pays.setdefault(Pays, []).append((Or, Argent, Bronze))

# Classe pour récupérer les résultats des pays par discipline
class resultat_discipline():
    cursor = bdd.cursor()
    cursor.execute(""" SELECT nom_discipline AS Discipline,
                   nom_pays AS Pays,
                   FORMAT(SUM(medaille_or), 0) AS "Or",
                   FORMAT(SUM(medaille_argent), 0) AS "Argent",
                   FORMAT(SUM(medaille_bronze), 0) AS "Bronze"
                   FROM Resultats
                   JOIN Pays ON Pays.id_pays = Resultats.id_pays
                   JOIN Disciplines ON Disciplines.id_discipline = Resultats.id_discipline
                   GROUP BY Disciplines.nom_discipline, Pays.nom_pays
                   ORDER BY Disciplines.nom_discipline, Pays.nom_pays;
                   """)
    resultat = cursor.fetchall()

    # Création d'un dictionnaire pour stocker les résultats
    dico_resultat_disciplines = {}
    for resultat_disciplines in resultat:
        Discipline, Pays, Or, Argent, Bronze = resultat_disciplines
        dico_resultat_disciplines.setdefault(Discipline, []).append(
            (Pays, Or, Argent, Bronze)
        )

# Fonction pour ajouter un résultat à la base de données
def ajouter_resultat(id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze):
    cursor = bdd.cursor()
    sql = "INSERT INTO Resultats(id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze) VALUES (%s, %s, %s, %s, %s)"
    valeurs = (id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze)
    cursor.execute(sql, (valeurs))
    bdd.commit()
