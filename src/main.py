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
fond = tk.PhotoImage(file="images/anneaux_olympiques.png")
pixel_gris = tk.PhotoImage(file="images/pixel-gris.png") # image permettant de résoudre des dysfonctionnements graphiques
# icônes de flèches à côté des boutons des menus déroulants
img_up = tk.PhotoImage(file="images/up.png")  
img_down = tk.PhotoImage(file="images/down.png")
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

# Fonction pour afficher le menu de droite
def menu_liste():
    bouton_deroulant2.config(image=img_down) # ouverture du menu : flèche vers le bas
    def menu_sportifs():
        vider_cadre3() 
        label_fond.configure(image=pixel_gris, bg="lightgray") # l'image des anneaux des JO devient l'image d'un pixel gris invisible
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
                sportif = f"{prenom_sportif} : {nom_sportif}"
                
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
        label_fond.configure(image=pixel_gris, bg="lightgray")
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des disciplines",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    orientation="horizontal")
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
    global_bouton_deroulant2.config(command=appel_fonction_fermer_liste) # à modifier ?

def fenetre_ajouter_sportif():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    def entry_click(event): # lorsque l'utilisateur clique dans les champs d'écriture
        # l'affichage "Prénom" et "Nom" en gris s'efface
        if prenom_entry.get() == "Prénom" and nom_entry.get() == "Nom":
            prenom_entry.delete(0, tk.END)
            nom_entry.delete(0, tk.END) 
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
    nom_entry = tk.Entry(cadre3, textvariable=nom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry = tk.Entry(cadre3, textvariable=prenom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry.insert(0, prenom_txt)
    nom_entry.insert(0, nom_txt)
    prenom_entry.bind("<FocusIn>", entry_click) # lorsque l'utilisateur clique dans les champs d'écriture
    nom_entry.bind("<FocusIn>", entry_click)
    prenom_entry.pack()
    nom_entry.pack()
    bouton_pays = tk.OptionMenu(cadre3, nom_pays_var, *pays) # boutons de menus déroulants
    bouton_pays.pack(pady=3)
    bouton_discipline = tk.OptionMenu(cadre3, nom_discipline_var, *discipline)
    bouton_discipline.pack(pady=3)
    bouton_ajouter_sportif = tk.Button(cadre3, text="Ajouter un sportif", font=(police, 12), 
        width=20,
        bg='#51AA3A', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#51AA3A', 
        command=lambda: recuperer_valeurs1(),
        )
    bouton_ajouter_sportif.pack()
    bouton_supprimer_sportif = tk.Button(cadre3, text="Supprimer un sportif", font=(police, 12), 
        width=20,
        bg='#C3423D', 
        fg='white',
        activeforeground= 'black', 
        activebackground = '#C3423D', 
        command=lambda: recuperer_valeurs2(),
        )
    bouton_supprimer_sportif.pack()
    bouton_config(bouton_pays)
    bouton_config(bouton_discipline)
    # futur message d'avertissement (pour l'instant invisible)
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray')
    label_avertissement.pack(pady=20) 
    def recuperer_valeurs1():
        label_avertissement.config(text="", bg="lightgray")
        champs = (nom_var.get(), prenom_var.get(), nom_pays_var.get(), nom_discipline_var.get())
        # Vérifie si tous les champs sont non-vides
        if all(champs) and nom_var.get() != "Nom" and prenom_var.get() != "Prénom":  
            try:# test si chaque champs est remplis
                id_pays = {
                    "France": "1",
                    "États-unis": "2",
                    "Canada": "3",
                    "Angleterre": "4",
                    "Italie": "5",
                }.get(nom_pays_var.get())
                if id_pays is None: 
                    raise ValueError("Pays non trouvé") # si on l'utilise pas autant le supprimer ?
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
                nom_entry.delete(0, tk.END)
                prenom_entry.delete(0, tk.END)
                label_avertissement.config(text="Veuillez fermer la fenêtre, puis relancer l'application pour mettre à jour la base de données.", bg="white")
            except ValueError as e:
                label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
        else:
            label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
    def recuperer_valeurs2(): 
        nom = nom_var.get()
        prenom = prenom_var.get()
        supprimer_sportif(nom, prenom)
        nom_entry.delete(0, tk.END)
        prenom_entry.delete(0, tk.END)
        if label_avertissement.cget("text") == "": 
            label_avertissement.config(text="Veuillez relancer le programme pour mettre à jour la base de données.", bg='white')
        elif label_avertissement.cget("text") == "Veuillez relancer le programme pour mettre à jour la base de données.":
            pass
  
#Fonction pour effacer le contenu du cadre central
def vider_cadre3():
    for widget in cadre3.winfo_children(): # recherche de tous les éléments dans le cadre
        if widget != label_fond: # le contenu du cadre est supprimé sauf ce qui permet d'afficher l'image de fond
            widget.destroy()
    label_fond.configure(image=fond) 

# Fonction permettant de fermer les menus
def fermer_menu(cadre, bouton_deroulant):
   for widget in cadre.winfo_children():
        if widget != bouton_deroulant:
            widget.destroy()
   vider_cadre3()

# Fonction pour l'etat du menu "fermé"
def appel_fonction_fermer_liste():
   fermer_menu(cadre2, global_bouton_deroulant2)
   bouton_deroulant2.config(image=img_up)
   global_bouton_deroulant2.config(command=menu_liste)
  
# Fonction pour afficher le menu de gauche
# Pour plus d'infos et d'explications sur cette fonction, voir la fonction menu_liste ligne n°~42
def menu_resultat():
    bouton_deroulant1.config(image=img_down)
    def menu_resultats_pays():
        vider_cadre3()
        label_fond.configure(image=pixel_gris, bg="lightgray")
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des résultats par pays",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    scrollbar_button_hover_color="lightgray",
                                    scrollbar_button_color="lightgray")
        cadre_ctk.pack(expand=tk.YES, fill=tk.BOTH)
        for pays, resultat in resultat_pays.dico_resultat_pays.items():
            if pays == "France":
                img = fr
            elif pays == "États-Unis":
                img = us
            elif pays == "Canada":
                img = ca
            elif pays == "Angleterre":
                img = gb
            elif pays == "Italie":
                img = it
            
            for medaille in resultat:
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
                contenu_txt = tk.Label(cadre_label, text=bronze, font=police, bg="lightgray")#cadre_scrollbar
                contenu_txt.pack(side=tk.LEFT)
                # image médaille de bronze
                contenu_img = tk.Label(cadre_label, image=img_bronze, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
         
    def menu_resultats_disciplines():
        vider_cadre3()
        label_fond.configure(image=pixel_gris, bg="lightgray")
        #création de la barre de défilement etc
        cadre_scrollbar = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Liste des résultats par disciplines",
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 orientation="vertical")
        cadre_scrollbar.pack(expand=tk.YES, fill=tk.BOTH, side =tk.TOP)
        for discipline, valeur in resultat_discipline.dico_resultat_disciplines.items():
            affichage_discipline = tk.Label(cadre_scrollbar, text=discipline, font=(police,18), bg="lightgray")
            affichage_discipline.pack(side=tk.TOP)
            for i in valeur:
                pays = i[0]
                if pays == "France":
                    img = fr
                elif pays == "États-Unis":
                    img = us
                elif pays == "Canada":
                    img = ca
                elif pays == "Angleterre":
                    img = gb
                elif pays == "Italie":
                    img = it
                gold = i[1]
                silver = i[2]
                bronze = i[3]
                affichage1 = f"{pays} : {gold}"
                # pour plus de détails sur l'affichage, voir la fonction menu_resultats_pays ligne 275
                cadre_label = tk.Frame(cadre_scrollbar, bg="lightgray") 
                cadre_label.pack(side=tk.TOP, expand=tk.YES) 
                underscore = "_______________________________________________________________________________________________________________"
                ligne = tk.Label(cadre_scrollbar, text=underscore, font=(police, 12), bg="lightgray")
                ligne.pack(expand=tk.YES)
                contenu_img = tk.Label(cadre_label, image=img, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                contenu_txt = tk.Label(cadre_label, text=affichage1, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                contenu_img = tk.Label(cadre_label, image=img_gold, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                contenu_txt = tk.Label(cadre_label, text=silver, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                contenu_img = tk.Label(cadre_label, image=img_silver, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)
                contenu_txt = tk.Label(cadre_label, text=bronze, font=police, bg="lightgray")
                contenu_txt.pack(side=tk.LEFT)
                contenu_img = tk.Label(cadre_label, image=img_bronze, font=police, bg="lightgray")
                contenu_img.pack(side=tk.LEFT)

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
                                   text="Disciplines", 
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
    global_bouton_deroulant1.config(command=appel_fonction_fermer_resultat)

def fenetre_ajouter_resultat():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
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
    bouton_discipline.pack(pady=3) # changement de l'ordre
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
        command=lambda: recuperer_valeurs3(),
        )
    bouton_ajouter_resultat.pack()
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray')
    label_avertissement.pack(pady=20) 
    def recuperer_valeurs3(): 
        label_avertissement.config(text="", bg="lightgray")
        champs = (choix_medaille_var.get(), nom_pays_var.get(), nom_discipline_var.get())
        if all(champs): # Vérifie si tous les champs sont non-vides 
            try:
                id_pays = {
                    "France": "1",
                    "États-unis": "2",
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
                label_avertissement.config(text="Veuillez fermer la fenêtre, puis relancer l'application pour mettre à jour la base de données.", bg="white")
            except ValueError as e:
                label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
        else:
            label_avertissement.config(text="Tous les champs doivent être remplis.", bg='white')
    bouton_config(bouton_pays)
    bouton_config(bouton_discipline)
    bouton_config(bouton_medaille)
        
def appel_fonction_fermer_resultat(): 
   fermer_menu(cadre1, global_bouton_deroulant1)
   bouton_deroulant1.config(image=img_up)
   global_bouton_deroulant1.config(command=menu_resultat)

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
    
# Cadre pour le premier bouton déroulant à gauche
cadre1 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre1.pack(side="left", fill="y")
# Cadre pour le deuxieme bouton déroulant à droite
cadre2 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre2.pack(side="right", fill="y")
# Cadre central pour l'image et pour les différentes fenetres d'affichage
cadre3 = tk.Frame(fenetre, bg='lightgray')
cadre3.pack(expand=tk.YES,side="top", fill="both")

# Variable pour stocker la sélection
choix_selectionne1 = tk.StringVar() # sert à rien ?
choix_selectionne2 = tk.StringVar()

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
global global_bouton_deroulant1
global_bouton_deroulant1 = bouton_deroulant1

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
global global_bouton_deroulant2
global_bouton_deroulant2 = bouton_deroulant2

label_fond = tk.Label(cadre3, image=fond, border=0)
label_fond.pack()

# Lancement de la boucle principale
fenetre.mainloop()
