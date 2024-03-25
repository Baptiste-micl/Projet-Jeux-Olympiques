import tkinter as tk
from tkinter import font
from listes import liste_disciplines
from listes import liste_sportifs


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

# Ici on charge l'image
fond = tk.PhotoImage(file="images/anneaux_olympiques.png")

# Ici on défini une police pour toute la fenetre
police = font.Font(family="Arial", size=20)

# Fonction pour afficher le menu de droite
def menu_liste():
    def menu_sportifs():
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_sportifs.dico_sportifs.items())
         texte = texte.replace("{", "").replace("}", "")
         label_fond.configure(text=texte, image=(), font=police, bg="lightgray")

    def menu_disciplines():
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_disciplines.dico_disciplines.items())
        texte = texte.replace("{", "").replace("}", "")
        label_fond.configure(text=texte, image=(), font=police, bg="lightgray")

    bouton_sportifs = tk.Button(cadre2,
                             cursor='hand2',
                             text="Sportifs", 
                             font=("Courrier", 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_sportifs,
                             activebackground = '#ACCDD8')
    
    bouton_sportifs.pack()
    bouton_disciplines = tk.Button(cadre2,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=("Courrier", 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_disciplines)
    bouton_disciplines.pack()
  
# Fonction pour afficher le menu de gauche
def menu_resultat():
    def menu_sportifs():
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_sportifs.dico_sportifs.items())
         texte = texte.replace("{", "").replace("}", "")
         label_fond.configure(text=texte, image=(), font=police, bg="lightgray")

    def menu_disciplines():
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_disciplines.dico_disciplines.items())
        texte = texte.replace("{", "").replace("}", "")
        label_fond.configure(text=texte, image=(), font=police, bg="lightgray")

    bouton_pays = tk.Button(cadre1,
                             cursor='hand2',
                             text="Pays", 
                             font=("Courrier", 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_sportifs,
                             activebackground = '#ACCDD8')
    
    bouton_pays.pack()
    bouton_disciplines = tk.Button(cadre1,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=("Courrier", 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_disciplines)
    bouton_disciplines.pack()


# Cadre pour le premier bouton déroulant
cadre1 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre1.pack(side="left", fill="y")
# Cadre pour le deuxieme bouton déroulant
cadre2 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre2.pack(side="right", fill="y")
# Cadre pour l'image et pour les différentes fenetres
cadre3 = tk.Frame(fenetre)
cadre3.pack(expand=False,side="top", fill="y")

# Variable pour stocker la sélection
choix_selectionne1 = tk.StringVar()

# Variable pour stocker la sélection
choix_selectionne2 = tk.StringVar()

# Bouton déroulant2
bouton_deroulant1 = tk.Button(cadre1, 
                              text="Resultats",
                              width=12, 
                              command=menu_resultat,
                              cursor='hand2', 
                              font=("Georgia", 12), 
                              bg='lightblue', 
                              fg ='black',
                              )
bouton_deroulant1.pack()

# Bouton déroulant2
bouton_deroulant2 = tk.Button(cadre2, 
                              text="Listes",
                              width=12, 
                              command=menu_liste,
                              cursor='hand2', 
                              font=("Georgia", 12), 
                              bg='lightblue', 
                              fg ='black',
                              )
bouton_deroulant2.pack()

label_fond = tk.Label(fenetre, image=fond)
label_fond.pack()

# Lancement de la boucle principale
fenetre.mainloop()
