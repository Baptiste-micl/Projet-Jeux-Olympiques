import main
import tkinter as tk
# Fonction pour afficher le menu de droite

def menu_liste():
    main.bouton_deroulant2.config(image=main.img_down)
    def menu_sportifs():
         main.vider_cadre3() 
         titre = "Liste des sportifs"+"\n"
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in main.liste_sportifs.dico_sportifs.items())
         main.label_fond.configure(text=titre+texte, image=(), font=main.police, bg="lightgray")

    def menu_disciplines():
        main.vider_cadre3() 
        titre = "Liste des disciplines"+"\n"
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in main.liste_disciplines.dico_disciplines.items())
        main.label_fond.configure(text=titre+texte, image=(), font=main.police, bg="lightgray")

    bouton_sportifs = tk.Button(main.cadre2,
                             cursor='hand2',
                             text="Sportifs", 
                             font=(main.police, 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_sportifs,
                             activebackground = '#ACCDD8')
    
    bouton_sportifs.pack()
    bouton_disciplines = tk.Button(main.cadre2,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=(main.police, 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_sportif = tk.Button(main.cadre2, text="Ajouter un sportif", font=(main.police, 10), 
                    width=12,
                    bg='lightpink', 
                    fg='black', 
                    command=main.fenetre_ajouter_sportif,
                    activebackground = '#ffcdc2') 
    bouton_ajouter_sportif.pack()
    main.global_bouton_deroulant2.config(command=main.appel_fonction_fermer_liste)