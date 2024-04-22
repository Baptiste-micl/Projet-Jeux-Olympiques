import tkinter as tk
from tkinter import font
from listes import *
from resultats import *
import customtkinter as ctk

# JE SAIS PAS A QUOI CA SERT 
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

# Fenêtre, titre et icone
fenetre = tk.Tk()
fenetre.title("Jeux-Olympique")
fenetre.geometry("720x420")
fenetre.minsize(550, 300)
fenetre.config(background='lightgray')
fenetre.iconbitmap("images/icone_application.ico")

# Listes des resultats
resultats = ["Pays", "Pays + Disciplines"]
# Listes des sportifs et des disciplines
listes = ["Sportifs", "Disciplines"]

# Ici on charge les images
fond = tk.PhotoImage(file="images/anneaux_olympiques.png")
pixel_gris = tk.PhotoImage(file="images/pixel-gris.png") 
img_up = tk.PhotoImage(file="images/up.png")  
img_down = tk.PhotoImage(file="images/down.png")

# Ici on défini une police pour toute la fenetre
police = font.Font(family="Arial", size=15)

# Fonction pour afficher le menu de droite
def menu_liste():
    bouton_deroulant2.config(image=img_down)
    def menu_sportifs():
        vider_cadre3() 
        label_fond.configure(image=pixel_gris, bg="lightgray")
        #création de la barre de défilement etc
        cadre_scrollbar = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Liste des sportifs",
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 )
        cadre_scrollbar.pack(expand=tk.YES, fill=tk.BOTH)
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_sportifs.dico_sportifs.items())
        contenu = tk.Label(cadre_scrollbar, text=texte, font=police, bg="lightgray")
        contenu.pack(expand=tk.YES, fill=tk.BOTH)

    def menu_disciplines():
        vider_cadre3() 
        label_fond.configure(image=pixel_gris, bg="lightgray")
        #changement
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des disciplines",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    scrollbar_button_hover_color="lightgray",
                                    scrollbar_button_color="lightgray")
        cadre_ctk.pack(expand=tk.YES, fill=tk.BOTH)
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_disciplines.dico_disciplines.items())
        contenu = tk.Label(cadre_ctk, text=texte, font=police, bg="lightgray")
        contenu.pack(expand=tk.YES, fill=tk.BOTH)

    bouton_sportifs = tk.Button(cadre2,
                             cursor='hand2',
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
    bouton_ajouter_sportif = tk.Button(cadre2, text="Gérer les sportifs", font=(police, 10), 
                    width=13,
                    bg='lightpink', 
                    fg='black', 
                    command=fenetre_ajouter_sportif,
                    activebackground = '#ffcdc2') 
    bouton_ajouter_sportif.pack()
    global_bouton_deroulant2.config(command=appel_fonction_fermer_liste)

def fenetre_ajouter_sportif():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    def entry_click(event):
        if prenom_entry.get() == "Prénom" and nom_entry.get() == "Nom":
            prenom_entry.delete(0, tk.END)
            nom_entry.delete(0, tk.END) 
            prenom_entry.config(fg="blue")
            nom_entry.config(fg="blue")
    prenom_txt = "Prénom"
    nom_txt = "Nom"
    nom_var = tk.StringVar()
    prenom_var = tk.StringVar()
    nom_entry = tk.Entry(cadre3, textvariable=nom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry = tk.Entry(cadre3, textvariable=prenom_var, font=(police), bg='lightgray', fg='grey')
    prenom_entry.insert(0, prenom_txt)
    nom_entry.insert(0, nom_txt)
    prenom_entry.bind("<FocusIn>", entry_click)
    nom_entry.bind("<FocusIn>", entry_click)
    prenom_entry.pack()
    nom_entry.pack()
    bouton_ajouter_sportif = tk.Button(cadre3, text="Ajouter un sportif", font=(police, 12), 
        width=20,
        bg='#009000', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#b0eab6', 
        command=lambda: recuperer_valeurs1(),
        )
    bouton_ajouter_sportif.pack()
    bouton_supprimer_sportif = tk.Button(cadre3, text="Supprimer un sportif", font=(police, 12), 
        width=20,
        bg='#CE0000', 
        fg='white',
        activeforeground= 'black', 
        activebackground = '#ffcdc2', 
        command=lambda: recuperer_valeurs2(),
        )
    bouton_supprimer_sportif.pack()
    
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray')
    label_avertissement.pack(pady=20) 
    def recuperer_valeurs1():
       nom = nom_var.get()
       prenom = prenom_var.get()
       ajouter_sportif(nom, prenom)
       nom_entry.delete(0, tk.END)
       prenom_entry.delete(0, tk.END)
       if label_avertissement.cget("text") == "": 
           label_avertissement.config(text="Veuillez relancer le programme pour mettre à jour la base de données.", bg='white')
       elif label_avertissement.cget("text") == "Veuillez relancer le programme pour mettre à jour la base de données.":
           pass
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
    for widget in cadre3.winfo_children():
        if widget != label_fond: 
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
def menu_resultat():
    bouton_deroulant1.config(image=img_down)
    def menu_resultats_pays():
        vider_cadre3()
        label_fond.configure(image=pixel_gris, bg="lightgray")
        #changement
        cadre_ctk = ctk.CTkScrollableFrame(cadre3,
                                    label_text="Liste des résultats par pays",
                                    label_font=(police,19),
                                    fg_color="lightgray",
                                    scrollbar_button_hover_color="lightgray",
                                    scrollbar_button_color="lightgray")
        cadre_ctk.pack(expand=tk.YES, fill=tk.BOTH)
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in resultat_pays.dico_resultat_pays.items())
        contenu = tk.Label(cadre_ctk, text=texte, font=police, bg="lightgray")
        contenu.pack(expand=tk.YES, fill=tk.BOTH)
         
    def menu_resultats_disciplines():
        vider_cadre3()
        label_fond.configure(image=pixel_gris, bg="lightgray")
        #création de la barre de défilement etc
        cadre_scrollbar = ctk.CTkScrollableFrame(cadre3,
                                                 label_text="Liste des résultats par disciplines",
                                                 label_font=(police,19),
                                                 fg_color="lightgray",
                                                 orientation="horizontal",)
        cadre_scrollbar.pack(expand=tk.YES, fill=tk.BOTH)
        #cadre_scrollbar.bind("<MouseWheel>", lambda event: cadre_scrollbar.xview_scroll(-int(event.delta/60), "units"))
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in resultat_discipline.dico_resultat_disciplines.items())
        contenu = tk.Label(cadre_scrollbar, text=texte, font=police, bg="lightgray")
        contenu.pack(fill=tk.BOTH, side="top")

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
    bouton_ajouter_resultat = tk.Button(cadre1, text="Ajouter un resultat", font=(police, 10),
                    width=13,
                    bg='lightpink', 
                    fg='black', 
                    command=fenetre_ajouter_resultat,
                    activebackground = '#ffcdc2') 
    bouton_ajouter_resultat.pack()
    global_bouton_deroulant1.config(command=appel_fonction_fermer_resultat)

def fenetre_ajouter_resultat():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    # On crée les variables pour stocker
    nom_pays_var = tk.StringVar()
    nom_pays_var.set('Pays ') #changements
    nom_discipline_var = tk.StringVar()
    nom_discipline_var.set('Discipline ')
    choix_medaille_var = tk.StringVar()
    choix_medaille_var.set('Médaille ')
    # On crée les listes
    pays = ["France", "États-Unis", "Canada", "Angleterre", "Italie"]
    discipline = ["Athlétisme", "Natation", "Judo"]
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
    label_avertissement = tk.Label(cadre3, text="", font=(police, 10), bg='lightgray')
    label_avertissement.pack(pady=20) 
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
        
        if label_avertissement.cget("text") == "": 
           label_avertissement.config(text="Veuillez relancer le programme pour mettre à jour la base de données.", bg='white')
        elif label_avertissement.cget("text") == "Veuillez relancer le programme pour mettre à jour la base de données.":
           pass
        
    def bouton_config(bouton):
        bouton.config(
                bg="#0066FF",
                fg="white",
                activebackground="#0066FF",
                activeforeground="white",
                font=(police,12),
                border=0,
                highlightthickness=1,
                highlightbackground='white',
                pady=10,
                indicatoron=0,
                image=img_down,
                compound=tk.RIGHT,
                width=100,
                height=10,
                )

        bouton['menu'].config(
                bg="gray",
                fg="black",
                activebackground="white",
                activeforeground="gray",
                font=(police,10),
                border=0)
    bouton_config(bouton_pays)
    bouton_config(bouton_discipline)
    bouton_config(bouton_medaille)
        
def appel_fonction_fermer_resultat(): 
   fermer_menu(cadre1, global_bouton_deroulant1)
   bouton_deroulant1.config(image=img_up)
   global_bouton_deroulant1.config(command=menu_resultat)

# Cadre pour le premier bouton déroulant
cadre1 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre1.pack(side="left", fill="y")
# Cadre pour le deuxieme bouton déroulant
cadre2 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre2.pack(side="right", fill="y")
# cadre de la barre de défilement 
cadre_scrollbar = tk.Frame(fenetre, bg='lightgray', bd=0)
cadre_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Cadre pour l'image et pour les différentes fenetres
cadre3 = tk.Frame(fenetre, bg='lightgray',)
cadre3.pack(expand=tk.YES,side="top", fill="both")#changement

# Variable pour stocker la sélection
choix_selectionne1 = tk.StringVar()

# Variable pour stocker la sélection
choix_selectionne2 = tk.StringVar()

# Bouton déroulant2
bouton_deroulant1 = tk.Button(cadre1,
                              text="Resultats ",
                              width=120, 
                              command=menu_resultat,
                              cursor='hand2', 
                              font=(police, 12), 
                              bg='lightblue', 
                              fg ='black',
                              image = img_up, 
                              compound=tk.RIGHT,
                              )
bouton_deroulant1.pack(fill=tk.X)
global global_bouton_deroulant1
global_bouton_deroulant1 = bouton_deroulant1

# Bouton déroulant2
bouton_deroulant2 = tk.Button(cadre2,
                              text="Listes ",
                              width=120, 
                              command=menu_liste,
                              cursor='hand2', 
                              font=(police, 12), 
                              bg='lightblue', 
                              fg ='black',
                              image = img_up, 
                              compound=tk.RIGHT,
                              )
bouton_deroulant2.pack(fill=tk.X)
global global_bouton_deroulant2
global_bouton_deroulant2 = bouton_deroulant2

label_fond = tk.Label(cadre3, image=fond)
label_fond.pack()

# Lancement de la boucle principale
fenetre.mainloop()
