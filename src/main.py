import tkinter as tk

# Création de la fenêtre principale
racine = tk.Tk()
racine.title("Ma première application")

# Création d'un label
label = tk.Label(racine, text="Bonjour à tous !")
label.pack()

# Création d'un bouton
bouton = tk.Button(racine, text="Quitter", command=racine.quit)
bouton.pack()

# Lancement de la boucle principale
racine.mainloop()