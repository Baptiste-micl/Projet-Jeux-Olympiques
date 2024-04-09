from main import *


def fenetre_ajouter_resultat():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    # On crée les variables pour stocker
    nom_pays_var = tk.StringVar()
    nom_discipline_var = tk.StringVar()
    choix_medaille_var = tk.StringVar()
    # On crée les listes
    pays = ["France", "États-Unis", "Canada", "Angleterre", "Italie"]
    discipline = ["Athlétisme", "Argent", "Bronze"]
    medaille = ["Or", "Argent", "Bronze"]
    # On crée les différents boutons
    bouton_pays = tk.OptionMenu(cadre3, nom_pays_var, *pays)
    bouton_pays.pack()
    bouton_discipline = tk.OptionMenu(cadre3, nom_discipline_var, *discipline)
    bouton_discipline.pack()
    bouton_medaille = tk.OptionMenu(cadre3, choix_medaille_var, *medaille)
    bouton_medaille.pack()
    bouton_ajouter_resultat = tk.Button(cadre3, text="Ajouter un resultat", font=(police, 12), 
        width=20,
        bg='green', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#b0eab6', 
        command=lambda: recuperer_valeurs3(),
        )
    bouton_ajouter_resultat.pack()
    def recuperer_valeurs3():
       if nom_pays_var.get() == "France":
           id_pays = "1"
       elif nom_pays_var.get() == "États-unis":
           id_pays = "2"
       elif nom_pays_var.get() == "Canada":
           id_pays = "3"
       elif nom_pays_var.get() == "Angleterre":
           id_pays = "4"
       elif nom_pays_var.get() == "Italie":
           id_pays = "5"
       if nom_discipline_var.get() == "Athlétisme":
           id_discipline = "1"
       elif nom_discipline_var.get() == "Natation":
           id_discipline = "2"
       elif nom_discipline_var.get() == "Judo":
           id_discipline = "3"

       if choix_medaille_var.get() == "Or":
           ajouter_resultat(id_pays, id_discipline, "1", "0", "0")
       elif choix_medaille_var.get() == "Argent":
           ajouter_resultat(id_pays, id_discipline, "0", "1", "0")
       elif choix_medaille_var.get() == "Bronze":
           ajouter_resultat(id_pays, id_discipline, "0", "0", "1")