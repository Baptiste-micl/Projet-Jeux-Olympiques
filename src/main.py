import tkinter as tk

# Création de la fenêtre principale
fenetre= tk.Tk()
fenetre.title("Jeux-Olympiques")

liste_resultat = Listbox(fenetre)
liste_resultat.insert(1, "test")

# Création d'un bouton
bouton = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton.pack()

# Lancement de la boucle principale
fenetre.mainloop()