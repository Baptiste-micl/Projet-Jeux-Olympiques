import tkinter as tk
import main
import ajouter_resultats as ar

# Fonction pour afficher le menu de gauche
def menu_resultat():
    main.bouton_deroulant1.config(image=main.img_down)
    def menu_resultats_pays():
         main.vider_cadre3()
         titre = "Liste des resultats par Pays"+"\n"
         texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in main.resultat_pays.dico_resultat_pays.items())
         main.label_fond.configure(text=titre+texte, image=(), font=main.police, bg="lightgray")
         

    def menu_resultats_disciplines():
        main.vider_cadre3()
        titre = "Liste des resultats par Discipline"+"\n"
        texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in main.resultat_discipline.dico_resultat_disciplines.items())
        main.label_fond.configure(text=titre+texte, image=(), font=main.police, bg="lightgray")

    bouton_pays = tk.Button(main.cadre1,
                             cursor='hand2',
                             text="Pays", 
                             font=(main.police, 12), 
                             width=12,
                             bg='gray', 
                             fg='black', 
                             command=menu_resultats_pays,
                             activebackground = '#ACCDD8')
    
    bouton_pays.pack()
    bouton_disciplines = tk.Button(main.cadre1,
                                   cursor='hand2', 
                                   text="Disciplines", 
                                   font=(main.police, 12),
                                   width=12, 
                                   bg='gray', 
                                   activebackground = '#ACCDD8',
                                   fg='black', 
                                   command=menu_resultats_disciplines)
    bouton_disciplines.pack()
    bouton_ajouter_resultat = tk.Button(main.cadre1, text="Ajouter un resultat", font=(main.police, 10), 
                    width=12,
                    bg='lightpink', 
                    fg='black', 
                    command=ar.fenetre_ajouter_resultat,
                    activebackground = '#ffcdc2') 
    bouton_ajouter_resultat.pack()
    main.global_bouton_deroulant1.config(command=main.appel_fonction_fermer_resultat)