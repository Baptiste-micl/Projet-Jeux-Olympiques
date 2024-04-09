import main


def fenetre_ajouter_sportif():
    main.vider_cadre3() 
    main.label_fond.configure(image=main.pixel_gris, font=main.police, bg="lightgray") 
    nom_var = main.tk.StringVar()
    prenom_var = main.tk.StringVar()
    nom_entry = main.tk.Entry(main.cadre3, textvariable=nom_var, font=(main.police), bg='lightgray', fg='darkgreen')
    nom_entry.pack()
    prenom_entry = main.tk.Entry(main.cadre3, textvariable=prenom_var, font=(main.police), bg='lightgray', fg='darkgreen')
    prenom_entry.pack()
    bouton_ajouter_sportif = main.tk.Button(main.cadre3, text="Ajouter un sportif", font=(main.police, 12), 
        width=20,
        bg='green', 
        fg='white', 
        activeforeground= 'black', 
        activebackground = '#b0eab6', 
        command=lambda: recuperer_valeurs1(),
        )
    bouton_ajouter_sportif.pack()
    bouton_supprimer_sportif = main.tk.Button(main.cadre3, text="Supprimer un sportif", font=(main.police, 12), 
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
       main.ajouter_sportif(nom, prenom)
    def recuperer_valeurs2():
        nom = nom_var.get()
        prenom = prenom_var.get()
        main.supprimer_sportif(nom, prenom)
    