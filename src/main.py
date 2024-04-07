import tkinter as tk
from tkinter import font
from listes import *
from resultats import *

# Fenêtre, titre et icone
fenetre = tk.Tk()
fenetre.title("Jeux-Olympique")
fenetre.geometry("900x500")
fenetre.minsize(500, 300)
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
police = font.Font(family="Arial", size=20)

# Fonction pour afficher le menu de droite
def menu_liste():
    bouton_deroulant2.config(image=img_down)
    def menu_sportifs():
         vider_cadre3() 
         titre = "Liste des sportifs"+"\n"
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_sportifs.dico_sportifs.items())
         label_fond.configure(text=titre+texte, image=(), font=police, bg="lightgray")

    def menu_disciplines():
        vider_cadre3() 
        titre = "Liste des disciplines"+"\n"
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_disciplines.dico_disciplines.items())
        label_fond.configure(text=titre+texte, image=(), font=police, bg="lightgray")

    bouton_sportifs = tk.Button(cadre2,
                             cursor='hand2',
                             text="Sportifs", 
                             font=(police, 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_sportifs,
                             activebackground = '#ACCDD8')
    
    bouton_sportifs.pack()
    bouton_disciplines = tk.Button(cadre2,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=(police, 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_sportif = tk.Button(cadre2, text="Ajouter un sportif", font=(police, 10), 
                    width=12,
                    bg='lightpink', 
                    fg='black', 
                    command=fenetre_ajouter_sportif,
                    activebackground = '#ffcdc2') 
    bouton_ajouter_sportif.pack()
    global_bouton_deroulant2.config(command=appel_fonction_fermer_liste)

def fenetre_ajouter_sportif():
    vider_cadre3() 
    label_fond.configure(image=pixel_gris, font=police, bg="lightgray") 
    nom_var = tk.StringVar()
    prenom_var = tk.StringVar()
    nom_entry = tk.Entry(cadre3, textvariable=nom_var, font=(police), bg='lightgray', fg='darkgreen')
    nom_entry.pack()
    prenom_entry = tk.Entry(cadre3, textvariable=prenom_var, font=(police), bg='lightgray', fg='darkgreen')
    prenom_entry.pack()
    bouton_ajouter_sportif = tk.Button(cadre3, text="Ajouter un sportif", font=(police, 12), 
        width=20,
        bg='green', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#b0eab6', 
        command=lambda: recuperer_valeurs1(),
        )
    bouton_ajouter_sportif.pack()
    bouton_supprimer_sportif = tk.Button(cadre3, text="Supprimer un sportif", font=(police, 12), 
        width=20,
        bg='darkred', 
        fg='white',
        activeforeground= 'black', 
        activebackground = '#ffcdc2', 
        command=lambda: recuperer_valeurs2(),
        )
    bouton_supprimer_sportif.pack()
    def recuperer_valeurs1():
       nom = nom_var.get()
       prenom = prenom_var.get()
       ajouter_sportif(nom, prenom)
    def recuperer_valeurs2():
        nom = nom_var.get()
        prenom = prenom_var.get()
        supprimer_sportif(nom, prenom)
    
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
         titre = "Liste des resultats par Pays"+"\n"
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in resultat_pays.dico_resultat_pays.items())
         label_fond.configure(text=titre+texte, image=(), font=police, bg="lightgray")
         

    def menu_resultats_disciplines():
        vider_cadre3()
        titre = "Liste des resultats par Discipline"+"\n"
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in resultat_discipline.dico_resultat_disciplines.items())
        label_fond.configure(text=titre+texte, image=(), font=police, bg="lightgray")

    bouton_pays = tk.Button(cadre1,
                             cursor='hand2',
                             text="Pays", 
                             font=(police, 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_resultats_pays,
                             activebackground = '#ACCDD8')
    
    bouton_pays.pack()
    bouton_disciplines = tk.Button(cadre1,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=(police, 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_resultats_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_resultat = tk.Button(cadre1, text="Ajouter un resultat", font=(police, 10), 
                    width=12,
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
    nom_discipline_var = tk.StringVar()
    nom_pays_var = tk.StringVar()
    choix_medaille_var = tk.StringVar()
    # On crée une liste pour les discipline
    medaille = ["Or", "Argent", "Bronze"]
    # On crée les différents boutons
    nom_entry = tk.Entry(cadre3, textvariable=nom_discipline_var, font=(police), bg='lightgray', fg='darkgreen')
    nom_entry.pack()
    prenom_entry = tk.Entry(cadre3, textvariable=nom_pays_var, font=(police), bg='lightgray', fg='darkgreen')
    prenom_entry.pack()
    bouton_discipline = tk.OptionMenu(cadre3, choix_medaille_var, *medaille)
    bouton_discipline.pack()
    bouton_ajouter_sportif = tk.Button(cadre3, text="Ajouter un resultat", font=(police, 12), 
        width=20,
        bg='green', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#b0eab6', 
        command=lambda: recuperer_valeurs3(),
        )
    bouton_ajouter_sportif.pack()
    def recuperer_valeurs3():
       nom_discipline = nom_discipline_var.get()
       nom_pays = nom_pays_var.get()
       choix_medaille = choix_medaille_var.get()
       ajouter_resultat(nom_discipline, nom_pays, choix_medaille)

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
# Cadre pour l'image et pour les différentes fenetres
cadre3 = tk.Frame(fenetre, bg='lightgray',)
cadre3.pack(expand=False,side="top", fill="y")

# Variable pour stocker la sélection
choix_selectionne1 = tk.StringVar()

# Variable pour stocker la sélection
choix_selectionne2 = tk.StringVar()

# Bouton déroulant2
bouton_deroulant1 = tk.Button(cadre1,
                              text="Resultats ",
                              width=110, 
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
                              width=110, 
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

