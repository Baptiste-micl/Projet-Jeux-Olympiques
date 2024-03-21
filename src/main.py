import tkinter as tk

# Fenêtre et titre
fenetre = tk.Tk()
fenetre.title("Jeux-Olympique")
fenetre.geometry("800x400")

# Listes des resultats
resultats = ["Pays", "Pays + Disciplines"]
# Listes des sportifs et des disciplines
listes = ["Sportifs", "Disciplines"]
anneaux_olympique = tk.PhotoImage(file="Baptiste-micl/Projet-Jeux-Olympiques/images/anneaux_olympiques.jpg")

# Fonction pour afficher la sélection
def afficher_selection(choix):
  label.config(text=f"Sélectionné : {choix}")

# Cadre pour le premier bouton déroulant
cadre1 = tk.Frame(fenetre)
cadre1.pack(side="left")
# Cadre pour le deuxieme bouton déroulant
cadre2 = tk.Frame(fenetre)
cadre2.pack(side="right")
# Cadre pour l'image
cadre3 = tk.Frame(fenetre)
cadre3.pack()

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

# Bouton pour afficher la sélection
bouton_afficher1 = tk.Button(cadre1, text="Résultats", command=lambda: afficher_selection(choix_selectionne1.get()))
bouton_afficher1.pack()

# Bouton pour afficher la sélection
bouton_afficher2 = tk.Button(cadre2, text="Listes", command=lambda: afficher_selection(choix_selectionne2.get()))
bouton_afficher2.pack()

label2 = tk.Label(cadre3, image=anneaux_olympique)
label2.pack()

label = tk.Label(fenetre, text="")
label.pack()

# Lancement de la boucle principale
fenetre.mainloop()