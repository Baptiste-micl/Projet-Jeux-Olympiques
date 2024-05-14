menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=entrer)
file_menu.add_command(label="Quitter", command=root.quit)
menu.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu)


#Faut changer vers la ligne 95 pour mettre d'abord le titre puis la description de la discipline
for clef, valeur in resultat_discipline.dico_resultat_disciplines.items():
            affichage_discipline = tk.Label(cadre_ctk, text=discipline, font=(police,18), bg="lightgray")
            affichage_discipline.pack(side=tk.TOP)
  contenu = tk.Label(cadre_ctk, text=description, font=police, bg="lightgray")
  contenu.pack(expand=tk.YES, fill=tk.BOTH)
