import tkinter as tk
from liste_sportifs import liste_sportifs


# Fenêtre, titre et icone
fenetre = tk.Tk()
fenetre.title("Jeux-Olympique")
fenetre.geometry("600x400")
fenetre.minsize(500, 300)
fenetre.config(background='lightgray')
fenetre.iconbitmap("images/icone_application.ico")

# Listes des resultats
resultats = ["Pays", "Pays + Disciplines"]
# Listes des sportifs et des disciplines
listes = ["Sportifs", "Disciplines"]

# Ici on charge l'image
fond = tk.PhotoImage(file="images/anneaux_olympiques.png").subsample(2)

# Fonction pour afficher la sélection
def afficher_selection(choix):
  if choix == "Pays":
    print("bonjour")
  elif choix == "Pays + Disciplines":
    print("Bonjour2")
  elif choix == "Sportifs":
    label_fond.configure(text="bonjour", image="")
  else:
    print("Bonjour4")

# Cadre pour le premier bouton déroulant
cadre1 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre1.pack(side="left", fill="y")
# Cadre pour le deuxieme bouton déroulant
cadre2 = tk.Frame(fenetre, bg='lightgray', bd=1, relief="solid")
cadre2.pack(side="right", fill="y")
# Cadre pour l'image et pour les différentes fenetres
cadre3 = tk.Frame(fenetre)
cadre3.pack(expand=1,side="top", fill="both")

# Variable pour stocker la sélection
choix_selectionne1 = tk.StringVar()

# Variable pour stocker la sélection
choix_selectionne2 = tk.StringVar()

# Bouton déroulant1
bouton_deroulant1 = tk.OptionMenu(cadre1, choix_selectionne1, *resultats)
bouton_deroulant1.pack()

# Bouton déroulant2
bouton_deroulant2 = tk.OptionMenu(cadre2, choix_selectionne2, *listes)
bouton_deroulant2.pack()

# Bouton pour afficher les résultats
bouton_afficher1 = tk.Button(cadre1, text="Résultats", command=lambda: afficher_selection(choix_selectionne1.get()))
bouton_afficher1.pack()

# Bouton pour afficher les différentes listes
bouton_afficher2 = tk.Button(cadre2, text="Listes", command=lambda: afficher_selection(choix_selectionne2.get()))
bouton_afficher2.pack()


label_fond = tk.Label(fenetre, image=fond)
label_fond.pack()


label = tk.Label(fenetre, text="")
label.pack()

# Lancement de la boucle principale
fenetre.mainloop()
