import tkinter as tk
from tkinter import font
from listes import *
from resultats import *
import customtkinter as ctk # module permettant de faire des cadres avec une barre de défilement

# Fenêtre, titre et icone
fenetre = tk.Tk()
fenetre.title("Jeux-Olympique")
fenetre.geometry("720x420")
fenetre.minsize(565, 330)
fenetre.config(background='lightgray')
fenetre.iconbitmap("images/logo-jo.ico")

# Ici on charge les images
anneaux = tk.PhotoImage(file="images/anneaux_olympiques.png")
pixel_gris = tk.PhotoImage(file="images/pixel-gris.png") # image permettant de résoudre des dysfonctionnements graphiques
# icônes de flèches à côté des boutons des menus déroulants
img_up = tk.PhotoImage(file="images/up.png")  
img_down = tk.PhotoImage(file="images/down.png")
img_parametre = tk.PhotoImage(file="images/parametre.png")
# drapeaux
gb = tk.PhotoImage(file="images/gb.png")
fr = tk.PhotoImage(file="images/fr.png")
us = tk.PhotoImage(file="images/us.png")
it = tk.PhotoImage(file="images/it.png")
ca = tk.PhotoImage(file="images/ca.png")
# médailles
img_gold = tk.PhotoImage(file="images/gold.png")
img_silver = tk.PhotoImage(file="images/silver.png")
img_bronze = tk.PhotoImage(file="images/bronze.png")

# Ici on définit une police pour toute la fenetre
police = font.Font(family="Arial", size=15)

#Cette fonction créer un rectangle avec des coins arrondis (radius) dans un Canvas
def arrondis(canvas, x1, y1, x2, y2, radius, **kwargs):
    # (x1, y1) : coordonnées du coin supérieur gauche
    # (x2, y2) : coordonnées du coin inférieur droit
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    # Les coins arrondis sont calculés en ajoutant ou soustrayant le rayon (radius) aux coordonnées des coins du rectangle.

    # Création du polygone avec des coins arrondis
    canvas.create_polygon(points, 
                          **kwargs, # permet de faire passer des options supplémentaires, comme fill et outline
                          smooth=True) # bords du polygone lisses (utile pour l'effet visuel arrondis)

# Fonction pour afficher le menu de droite
def menu_liste():
    bouton_deroulant2.config(image=img_down) # ouverture du menu : flèche vers le bas
    def menu_sportifs():
        vider_cadre3() 
        fond.configure(image=pixel_gris, bg="lightgray") # l'image des anneaux des JO devient l'image d'un pixel gris invisible
        # création de la barre de défilement 
        cadre_scrollbar = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Liste des sportifs", # titre du cadre
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 )
        cadre_scrollbar.pack(expand=tk.YES, fill=tk.BOTH)
        for pays, valeur in liste_sportifs.dico_sportifs.items():
            # on associe chaque pays à son image
            if pays == 1:
                img = fr
            elif pays == 2:
                img = us
            elif pays == 3:
                img = ca
            elif pays == 4:
                img = gb
            elif pays == 5:
                img = it
            
            for i in valeur:
                # Le 1er élément du tuple "valeur" est le prénom, le 2e est le nom
                prenom_sportif = i[0]
                nom_sportif = i[1]
                sportif = f"{prenom_sportif}  {nom_sportif}"
                
                # Création d'un cadre pour chaque paire de labels
                cadre_label = tk.Frame(cadre_scrollbar, bg="lightgray")  
                cadre_label.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
                # Ligne de séparation
                underscore = "___________________________________________________________________________________________________________________"
                ligne = tk.Label(cadre_label, text=underscore, font=(police, 12), bg="lightgray")
                ligne.pack()

                contenu_txt = tk.Label(cadre_label, text=sportif, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                contenu_img = tk.Label(cadre_label, image=img, font=police, bg="lightgray")
                contenu_img.pack(side=tk.RIGHT)
    
    def menu_disciplines():
        vider_cadre3() 
        fond.configure(image=pixel_gris, bg="lightgray")
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des disciplines",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    orientation="horizontal") # barre de défilement horizontale : MAJ+molette  pour l'utiliser
        cadre_ctk.pack(expand=tk.YES, fill=tk.BOTH)
        # Discipline : Description de la discipline
        for discipline, description in liste_disciplines.dico_disciplines.items():
            texte = f"{discipline} : {description}\n"
            # création d'un cadre pour chaque couple "discpline + description"
            cadre_label = tk.Frame(cadre_ctk, bg="lightgray")  
            cadre_label.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
            # zone de texte 
            contenu = tk.Label(cadre_label, text=texte, font=police, bg="lightgray")
            contenu.pack(side=tk.LEFT)

    bouton_sportifs = tk.Button(cadre2,
                             cursor='hand2', # la flèche de la souris devient une main pour indiquer que l'on peut cliquer
                             text="Sportifs", 
                             font=(police, 12), 
                             width=13,
                             bg='gray', 
                             fg='black', 
                             command=menu_sportifs,
                             activebackground = '#ACCDD8')
    
    bouton_sportifs.pack()
    bouton_disciplines = tk.Button(cadre2,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=(police, 12),
                                   width=13, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_sportif = tk.Button(cadre2, text="Gérer les sportifs", font=(police, 11), 
                    width=13,
                    bg='lightpink', 
                    fg='black', 
                    command=fenetre_ajouter_sportif,
                    activebackground = 'lightpink') 
    bouton_ajouter_sportif.pack()
    bouton_deroulant2.config(command=appel_fonction_fermer_liste)
    fond.config(command=fermeture_menus)

def fenetre_ajouter_sportif():
    vider_cadre3() 
    fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    def entry_click(event): # lorsque l'utilisateur clique dans les champs d'écriture
        # l'affichage "Prénom" et "Nom" en gris s'efface
        if prenom_entry.get() == "Prénom" and nom_entry.get() == "Nom":
            prenom_entry.delete(0, tk.END)
            nom_entry.delete(0, tk.END) 
            # la couleur de la police d'écriture change de gris à bleu foncé
            prenom_entry.config(fg="#184A73") 
            nom_entry.config(fg="#184A73")
    prenom_txt = "Prénom"
    nom_txt = "Nom"
    pays = ["France", "États-Unis", "Canada", "Angleterre", "Italie"]
    discipline = ["Athlétisme", "Natation", "Judo"]
    # On crée les variables pour stocker
    nom_var = tk.StringVar() 
    prenom_var = tk.StringVar()
    nom_pays_var = tk.StringVar()
    nom_pays_var.set('Pays ') 
    nom_discipline_var = tk.StringVar()
    nom_discipline_var.set('Discipline ')
    # Champs d'écriture
    nom_entry = tk.Entry(cadre3, textvariable=nom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry = tk.Entry(cadre3, textvariable=prenom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry.insert(0, prenom_txt)
    nom_entry.insert(0, nom_txt)
    prenom_entry.bind("<FocusIn>", entry_click) # lorsque l'utilisateur clique dans les champs d'écriture
    nom_entry.bind("<FocusIn>", entry_click)
    prenom_entry.pack()
    nom_entry.pack()
    # Boutons de menus déroulants
    bouton_pays = tk.OptionMenu(cadre3, nom_pays_var, *pays) 
    bouton_pays.pack(pady=3)
    bouton_discipline = tk.OptionMenu(cadre3, nom_discipline_var, *discipline)
    bouton_discipline.pack(pady=3)
    bouton_ajouter_sportif = tk.Button(cadre3, text="Ajouter un sportif", font=(police, 12), 
        width=20,
        bg='#51AA3A', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#51AA3A', 
        command=lambda: recuperer_valeurs_ajout(),
        )
    bouton_ajouter_sportif.pack()
    bouton_supprimer_sportif = tk.Button(cadre3, text="Supprimer un sportif", font=(police, 12), 
        width=20,
        bg='#C3423D', 
        fg='white',
        activeforeground= 'black', 
        activebackground = '#C3423D', 
        command=lambda: recuperer_valeurs_suppr(),
        )
    bouton_supprimer_sportif.pack()
    bouton_config(bouton_pays)
    bouton_config(bouton_discipline)
    # futur message d'avertissement (pour l'instant invisible)
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray')
    label_avertissement.pack(pady=0)
    # Zone pour message d'avertissement qui indiquera qu'il faut relancer le programme
    canvas_avertissement = tk.Canvas(cadre3, width=30, height=20, bg="lightgray",highlightthickness=0)
    canvas_avertissement.pack()
    
    # Fonction pour ajouter un sportif
    def recuperer_valeurs_ajout():
        # On rend les messages d'avertissement invisibles (utile uniquement dans des cas précis)
        label_avertissement.config(text="", bg="lightgray")
        canvas_avertissement.config(bg="lightgray", width=0, height=0)
        label_avertissement.pack_configure(pady=0) # réduction de l'espace entre les messages d'avertissement
        
        champs = (nom_var.get(), prenom_var.get(), nom_pays_var.get(), nom_discipline_var.get())
        # Vérifie si tous les champs sont non-vides
        if all(champs) and nom_var.get() != "Nom" and prenom_var.get() != "Prénom": 
            try:# test si chaque champs est remplis
                id_pays = {
                    "France": "1",
                    "États-Unis": "2",
                    "Canada": "3",
                    "Angleterre": "4",
                    "Italie": "5",
                }.get(nom_pays_var.get())
                if id_pays is None:
                    raise ValueError("Pays non trouvé")
                id_discipline = {
                    "Athlétisme": "1",
                    "Natation": "2",
                    "Judo": "3",
                }.get(nom_discipline_var.get())
                if id_discipline is None:
                    raise ValueError("Discipline non trouvée")
                ajout_prenom = prenom_var.get()
                ajout_nom = nom_var.get()
                ajouter_sportif(ajout_nom, ajout_prenom, id_pays, id_discipline)
                # après l'ajout du sportif, on efface le prénom et le nom pour que l'utilisateur puisse en rentrer un nouveau
                nom_entry.delete(0, tk.END)
                prenom_entry.delete(0, tk.END)

                label_avertissement.pack_configure(pady=0)
                # Coins arrondis sur le Canvas
                canvas_avertissement.config(bg="lightgray", width=240, height=140)
                arrondis(canvas_avertissement, 20, 20, 220, 120, radius=20, fill='#ACCDD8', outline="black")
                canvas_avertissement.create_text(120, 70, 
                                                 text="Veuillez fermer la fenêtre.\nPuis relancer l'application.\n\n     (Pour mettre à jour \n    la base de données.)", 
                                                 font=(police,12))
            except ValueError as e:
                label_avertissement.pack_configure(pady=20)
                label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
        else:
            label_avertissement.pack_configure(pady=20)
            label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')

    # Fonction pour supprimer un sportif
    def recuperer_valeurs_suppr(): 
        champs = (nom_var.get(), prenom_var.get())
        if all(champs) and nom_var.get() != "Nom" and prenom_var.get() != "Prénom": 
            nom = nom_var.get()
            prenom = prenom_var.get()
            supprimer_sportif(nom, prenom)
            nom_entry.delete(0, tk.END)
            prenom_entry.delete(0, tk.END)
            
            label_avertissement.pack_configure(pady=0)
            label_avertissement.config(text="", bg="lightgray")
            # Coins arrondis sur le Canvas
            canvas_avertissement.config(bg="lightgray", width=240, height=140)
            arrondis(canvas_avertissement, 20, 20, 220, 120, radius=20, fill='#ACCDD8', outline="black")
            canvas_avertissement.create_text(120, 70, 
                            text="Veuillez fermer la fenêtre.\nPuis relancer l'application.\n\n     (Pour mettre à jour \n    la base de données.)", 
                            font=(police,12))
        else:
            label_avertissement.pack_configure(pady=20)
            label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
            canvas_avertissement.config(bg="lightgray", width=0, height=0)

# Fonction pour effacer le contenu du cadre central
def vider_cadre3():
    for widget in cadre3.winfo_children(): # recherche de tous les éléments dans le cadre
        if widget != fond: # le contenu du cadre est supprimé sauf ce qui permet d'afficher l'image de fond
            widget.destroy()
    fond.configure(image=anneaux) 

# Fonction permettant de fermer les menus
def fermer_menu(cadre, bouton_deroulant, parametre):
   for widget in cadre.winfo_children():
        if widget != bouton_deroulant and widget != parametre:
            widget.destroy()
   vider_cadre3()

# Fonction pour l'etat du menu "fermé"
def appel_fonction_fermer_liste():
   fermer_menu(cadre2, bouton_deroulant2, bouton_parametre) # le menu se ferme
   bouton_deroulant2.config(image=img_up) # fermeture du menu : flèche vers le haut
   bouton_deroulant2.config(command=menu_liste) # la commande du bouton change pour pouvoir réouvrir le menu plus tard
  
# Fonction pour afficher le menu de gauche
def menu_resultat():
    bouton_deroulant1.config(image=img_down) # ouverture du menu : flèche vers le bas
    
    # Fonction pour l'affichage des résultats par pays
    def menu_resultats_pays():
        vider_cadre3()
        fond.configure(image=pixel_gris, bg="lightgray") # l'image des anneaux des JO devient l'image d'un pixel gris invisible
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des résultats par pays",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    # barre de défilement invisible
                                    scrollbar_button_hover_color="lightgray",
                                    scrollbar_button_color="lightgray")
        cadre_ctk.pack(expand=tk.YES, fill=tk.BOTH)
        for pays, resultat in resultat_pays.dico_resultat_pays.items():
            # on associe chaque pays à son image
            if pays == "Angleterre":
                img = gb
            elif pays == "Canada":
                img = ca
            elif pays == "États-Unis":
                img = us
            elif pays == "France":
                img = fr
            elif pays == "Italie":
                img = it
            for medaille in resultat:
                # Pour chaque élément du tuple resultat, on associe la bonne médaille
                gold = medaille[0]
                silver = medaille[1]
                bronze = medaille[2]
                affichage1 = f"{pays} : {gold}"
                cadre_label = tk.Frame(cadre_ctk, bg="lightgray")  
                cadre_label.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
                # ligne de séparation
                underscore = "___________________________________________________________________________________________________________________"
                ligne = tk.Label(cadre_label, text=underscore, font=(police, 12), bg="lightgray")
                ligne.pack(expand=tk.YES)
                # drapeau pays
                contenu_img = tk.Label(cadre_label, image=img, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # Pays + nombre de médailles d'or
                contenu_txt = tk.Label(cadre_label, text=affichage1, font=police, bg="lightgray")#cadre_scrollbar
                contenu_txt.pack(side=tk.LEFT)
                # image médaille d'or
                contenu_img = tk.Label(cadre_label, image=img_gold, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # nombre de médailles d'argent
                contenu_txt = tk.Label(cadre_label, text=silver, font=police, bg="lightgray")#cadre_scrollbar
                contenu_txt.pack(side=tk.LEFT)
                # image médaille d'argent
                contenu_img = tk.Label(cadre_label, image=img_silver, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # nombre de médailles de bronze
                contenu_txt = tk.Label(cadre_label, text=bronze, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                # image médaille de bronze
                contenu_img = tk.Label(cadre_label, image=img_bronze, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
         
    # Fonction pour l'affichage des résultats des pays par discipline
    def menu_resultats_disciplines():
        vider_cadre3()
        fond.configure(image=pixel_gris, bg="lightgray")
        # Création de la barre de défilement etc
        cadre_scrollbar = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Liste des résultats par discipline",
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 orientation="vertical")
        cadre_scrollbar.pack(expand=tk.YES, fill=tk.BOTH, side =tk.TOP)
        for discipline, valeur in resultat_discipline.dico_resultat_disciplines.items():
            # Affichage de la discipline
            affichage_discipline = tk.Label(cadre_scrollbar, text=discipline, font=(police,18), bg="lightgray")
            affichage_discipline.pack(side=tk.TOP)
            for i in valeur:
                # on associe chaque pays à son image
                pays = i[0]
                if pays == "Angleterre":
                    img = gb
                elif pays == "Canada":
                    img = ca
                elif pays == "États-Unis":
                    img = us
                elif pays == "France":
                    img = fr
                elif pays == "Italie":
                    img = it
                # on associe la bonne médaille
                gold = i[1]
                silver = i[2]
                bronze = i[3]
                affichage1 = f"{pays} : {gold}"
                # création d'un cadre pour chaque "groupe" d'affichage
                cadre_label = tk.Frame(cadre_scrollbar, bg="lightgray") 
                cadre_label.pack(side=tk.TOP, expand=tk.YES) 
                # ligne de séparation
                underscore = "_______________________________________________________________________________________________________________"
                ligne = tk.Label(cadre_scrollbar, text=underscore, font=(police, 12), bg="lightgray")
                ligne.pack(expand=tk.YES)
                # drapeau pays
                contenu_img = tk.Label(cadre_label, image=img, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # Pays + nombre de médailles d'or
                contenu_txt = tk.Label(cadre_label, text=affichage1, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                # image médaille d'or
                contenu_img = tk.Label(cadre_label, image=img_gold, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # nombre de médaille d'argent
                contenu_txt = tk.Label(cadre_label, text=silver, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                # image médaille d'argent
                contenu_img = tk.Label(cadre_label, image=img_silver, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                # nombre de médailles de bronze
                contenu_txt = tk.Label(cadre_label, text=bronze, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                # image médaille de bronze
                contenu_img = tk.Label(cadre_label, image=img_bronze, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)

    # Création des boutons du menu de gauche
    bouton_pays = tk.Button(cadre1,
                             cursor='hand2',
                             text="Pays", 
                             font=(police, 12), 
                             width=13,
                             bg='gray', 
                             fg='black', 
                             command=menu_resultats_pays,
                             activebackground = '#ACCDD8')
    
    bouton_pays.pack()
    bouton_disciplines = tk.Button(cadre1,
                                   cursor='hand2', 
                                   text="Pays / Discipline", 
                                   font=(police, 12),
                                   width=13, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_resultats_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_resultat = tk.Button(cadre1, text="Ajouter un resultat", font=(police, 11),
                    width=13,
                    bg='lightpink', 
                    fg='black', 
                    command=fenetre_ajouter_resultat,
                    activebackground = 'lightpink') 
    bouton_ajouter_resultat.pack()
    bouton_deroulant1.config(command=appel_fonction_fermer_resultat)
    fond.config(command=fermeture_menus)

def fenetre_ajouter_resultat():
    vider_cadre3() 
    fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    # On crée les variables pour stocker
    nom_pays_var = tk.StringVar()
    nom_pays_var.set('Pays ') 
    nom_discipline_var = tk.StringVar()
    nom_discipline_var.set('Discipline ')
    choix_medaille_var = tk.StringVar()
    choix_medaille_var.set('Médaille ')
    # On crée les listes
    pays = ["France", "États-Unis", "Canada", "Angleterre", "Italie"]
    discipline = ["Athlétisme", "Natation", "Judo"]
    medaille = ["Or", "Argent", "Bronze"]
    # On crée les différents boutons
    bouton_discipline = tk.OptionMenu(cadre3, nom_discipline_var, *discipline)
    bouton_discipline.pack(pady=3) 
    bouton_pays = tk.OptionMenu(cadre3, nom_pays_var, *pays)
    bouton_pays.pack(pady=3)
    bouton_medaille = tk.OptionMenu(cadre3, choix_medaille_var, *medaille)
    bouton_medaille.pack(pady=3)
    bouton_ajouter_resultat = tk.Button(cadre3, text="Ajouter un resultat", font=(police, 12), 
        width=20,
        bg='#51AA3A', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#51AA3A', 
        command=lambda: recuperer_valeurs_result(),
        )
    bouton_ajouter_resultat.pack()
    # Zone pour message d'erreur
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray',)
    label_avertissement.pack(pady=10) 
    # Zone pour message d'avertissement qui indiquera qu'il faut relancer le programme
    canvas_avertissement = tk.Canvas(cadre3, width=30, height=20, bg="lightgray",highlightthickness=0)
    canvas_avertissement.pack()
    # Fonction pour ajouter le résultat à la base de données
    def recuperer_valeurs_result(): 
        label_avertissement.config(text="", bg="lightgray")
        canvas_avertissement.config(bg="lightgray", width=0, height=0)
        champs = (choix_medaille_var.get(), nom_pays_var.get(), nom_discipline_var.get())
        if all(champs): # Vérifie si tous les champs sont non-vides 
            try:
                id_pays = {
                    "France": "1",
                    "États-Unis": "2",
                    "Canada": "3",
                    "Angleterre": "4",
                    "Italie": "5",
                }.get(nom_pays_var.get())
                if id_pays is None: 
                    raise ValueError("Pays non trouvé") 
                id_discipline = {
                    "Athlétisme": "1",
                    "Natation": "2",
                    "Judo": "3",
                }.get(nom_discipline_var.get())
                if id_discipline is None:
                    raise ValueError("Discipline non trouvée")
                if choix_medaille_var.get() == "Or":
                    ajouter_resultat(id_pays, id_discipline, "1", "0", "0")
                elif choix_medaille_var.get() == "Argent":
                    ajouter_resultat(id_pays, id_discipline, "0", "1", "0")
                elif choix_medaille_var.get() == "Bronze":
                    ajouter_resultat(id_pays, id_discipline, "0", "0", "1")
                else:
                    raise ValueError("Médaille non trouvée") 
                # Coins arrondis sur le Canvas
                canvas_avertissement.config(bg="lightgray", width=240, height=140)
                arrondis(canvas_avertissement, 20, 20, 220, 120, radius=20, fill='#ACCDD8', outline="black")
                canvas_avertissement.create_text(120, 70, 
                                                 text="Veuillez fermer la fenêtre.\nPuis relancer l'application.\n\n     (Pour mettre à jour \n    la base de données.)", 
                                                 font=(police,12))
            except ValueError as e:
                label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
        else:
            print("Erreur")
    bouton_config(bouton_pays)
    bouton_config(bouton_discipline)
    bouton_config(bouton_medaille)

def appel_fonction_fermer_resultat(): 
   fermer_menu(cadre1, bouton_deroulant1, bouton_parametre) # le menu se ferme
   bouton_deroulant1.config(image=img_up) # fermeture du menu : flèche vers le haut
   bouton_deroulant1.config(command=menu_resultat) # la commande du bouton change pour pouvoir réouvrir le menu plus tard

def bouton_config(bouton):
    # configuration du design des boutons OptionMenu déroulants
    bouton.config(
        bg="#184A73",
        fg="white",
        activebackground="#184A73",
        activeforeground="white",
        font=(police,12),
        border=0,
        pady=10,
        highlightthickness=1,
        highlightbackground='white',
        indicatoron=0,
        image=img_down,
        compound=tk.RIGHT,
        width=100,
        height=10)

    # configuration du design des choix des boutons OptionMenu déroulants
    bouton['menu'].config(
        bg="gray",
        fg="white",
        activebackground="white",
        activeforeground="gray",
        font=(police,10),
        border=0)
    
def fenetre_parametre():
    vider_cadre3() 
    taille_var = tk.StringVar() 
    taille_var.set('Taille') 
    choix_taille = ["Grand: 1920x1080", "Moyen: 1280x720", "Petit: 720x576"]
    police_var = tk.StringVar() 
    police_var.set('Taille') 
    choix_police = ["Arial", "Helvetica"]
    fond.configure(image=pixel_gris, bg="lightgray") # l'image des anneaux des JO devient l'image d'un pixel gris invisible
    # création de la barre de défilement 
    cadre_parametre = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Parametre", # titre du cadre
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 )
    cadre_parametre.pack(expand=tk.YES, fill=tk.BOTH)
    bouton_taille = tk.OptionMenu(cadre_parametre, taille_var, *choix_taille)
    bouton_taille.pack(pady=3)
    bouton_config(bouton_taille)
    bouton_police = tk.OptionMenu(cadre_parametre, police_var, *choix_police)
    bouton_police.pack(pady=3)
    bouton_config(bouton_police)
    bouton_sauvegarder = tk.Button(cadre_parametre,
                                   text="Sauvegarder",
                                   font=(police, 12),
                                   width=20, 
                                   bg='#51AA3A', 
                                   fg='white', 
                                   activeforeground= 'black', 
                                   activebackground = '#51AA3A',
                                   command=lambda: parametre(taille_var, police_var))
    bouton_sauvegarder.pack()
    contacter = tk.Label(cadre_parametre, text="""Nous contacter en cas de problème: 
    nicolas.thierry@groupe-esigelec.org
     baptiste.michel@groupe-esigelec.org""", font=police, bg="lightgray")
    contacter.pack(pady=3)
def parametre(taille_var, police_var):
    taille = taille_var.get()
    police = police_var.get()
    if taille == "Grand: 1920x1080":
        fenetre.geometry("1920x1080")
    elif taille == "Moyen: 1280x720":
        fenetre.geometry("1280x720")
    elif taille == "Petit: 720x576":
        fenetre.geometry("720x576")
    elif police == "Arial":
        police = font.Font(family="Arial", size=15)
    elif police == "Helvetica":
        police = font.Font(family="Helvetica", size=15)

    
# Fonctions pour ouvrir et fermer les 2 menus latéraux en cliquant sur l'image d'anneaux des JO
def ouverture_menus():
    menu_resultat()
    menu_liste()
    fond.config(command=fermeture_menus)
def fermeture_menus():
    appel_fonction_fermer_resultat()
    appel_fonction_fermer_liste()
    fond.config(command=ouverture_menus)

# Cadre pour le premier bouton déroulant à gauche
cadre1 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre1.pack(side="left", fill="y")
# Cadre pour le deuxieme bouton déroulant à droite
cadre2 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre2.pack(side="right", fill="y")
# Cadre central pour l'image et pour les différentes fenetres d'affichage
cadre3 = tk.Frame(fenetre, bg='lightgray')
cadre3.pack(expand=tk.YES,side="top", fill="both")

# Bouton déroulant à gauche
bouton_deroulant1 = tk.Button(cadre1,
                              text="Resultats ",
                              width=120, 
                              command=menu_resultat,
                              cursor='hand2', 
                              font=(police, 12), 
                              bg='#ACCDD8', 
                              activebackground='#ACCDD8',
                              fg ='black',
                              image = img_up, 
                              compound=tk.RIGHT,
                              )
bouton_deroulant1.pack(fill=tk.X)

# Bouton parametre
bouton_parametre = tk.Button(cadre1,
                             image = img_parametre,
                             bg='#ACCDD8',
                             command=fenetre_parametre)
bouton_parametre.pack(anchor="sw", side="bottom")

# Bouton déroulant à droite
bouton_deroulant2 = tk.Button(cadre2,
                              text="Listes ",
                              width=120, 
                              command=menu_liste,
                              cursor='hand2', 
                              font=(police, 12), 
                              bg='#ACCDD8', 
                              activebackground='#ACCDD8',
                              fg ='black',
                              image = img_up, 
                              compound=tk.RIGHT,
                              )
bouton_deroulant2.pack(fill=tk.X)

fond = tk.Button(cadre3, image=anneaux, border=0, command=ouverture_menus)
fond.pack()

# Lancement de la boucle principale
fenetre.mainloop()
