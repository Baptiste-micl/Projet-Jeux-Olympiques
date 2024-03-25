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

# Fonction pour afficher le menu de droite
def menu_liste():
    def liste_sportifs():
         label_sportifs = tk.Label(cadre3, 
                                  text="Liste des sportifs :", 
                                  font=("Berlin Sans FB", 20), 
                                  bg='lightgray', 
                                  fg ='darkgreen')
         label_sportifs.pack()

    def liste_disciplines():
        label_discipline = tk.Label(cadre3, 
                                text="Liste des disciplines :", 
                                font=("Berlin Sans FB", 20), 
                                 bg='lightgray', 
                                 fg ='darkgreen')
        label_discipline.pack()

    bouton_sportifs = tk.Button(cadre2,
                             cursor='hand2',
                             text="Sportifs", 
                             font=("Courrier", 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=liste_sportifs,
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
                                   command=liste_disciplines)
    bouton_disciplines.pack()
    bouton_gerer_sportifs = tk.Button(cadre2,
                                      cursor='hand2', 
                                      text="Gérer les sportifs", 
                                      font=("Courrier", 10),
                                      width=12, 
                                      bg='lightgreen', 
                                      activebackground= '#AED8AC',
                                      fg='black', 
                                      command=test_liste)
    bouton_gerer_sportifs.pack()
    print("ouvert")
    bouton_deroulant2.config(command=menu_liste_fermer)
# Fonction pour l'etat du menu "fermé"
def menu_liste_fermer():
   #cadre2.destroy() # NE FONCTIONNE PAS
   print("fermé")
   bouton_deroulant2.config(command=menu_liste)

# Fonction test pour futur affichage des listes
def test_liste():
    def test_chercher():
        mot = "TA GUEULE"
        entry.delete(0, tk.END)
        entry.insert(0, mot)
    entry = tk.Entry(cadre3, font=("Georgia", 20), bg='lightgray', fg ='darkgreen')
    entry.pack()
    bouton_afficher2 = tk.Button(cadre3, 
                                 text="Chercher", 
                                 command=test_chercher, 
                                 font=("Georgia", 12), 
                                 bg='lightgreen', 
                                 fg ='black', 
                                 cursor='hand2')
    bouton_afficher2.pack()

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

# Bouton pour afficher les résultats
bouton_afficher1 = tk.Button(cadre1, 
                             text="Résultats", 
                             command=lambda: afficher_selection(choix_selectionne1.get()))
bouton_afficher1.pack()

label_fond = tk.Label(fenetre, image=fond)
label_fond.pack()


label = tk.Label(fenetre, text="")
label.pack()

# Lancement de la boucle principale
fenetre.mainloop()
