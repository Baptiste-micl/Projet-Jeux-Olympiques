# ligne 50
for pays, valeur in liste_sportifs.dico_sportifs.items():
            cadre_label = tk.Frame(cadre_scrollbar, bg="lightgray")  # Création d'un cadre pour chaque paire de labels
            cadre_label.pack(fill=tk.X)
            if pays == 1:
                img = fr
            elif pays == 2:
                img = us
            elif pays == 3:
                img = ca
            elif pays == 4:
                img = gb
            elif pays == 5:
                img = it
            contenu_img = tk.Label(cadre_label, image=img, font=police, bg="lightgray")
            contenu_img.pack(side=tk.LEFT)
            
            prenom_sportif = valeur[0]
            nom_sportif = valeur[1]
            sportif = f"{prenom_sportif} : {nom_sportif}"
            contenu_txt = tk.Label(cadre_label, text=sportif, font=police, bg="lightgray")#cadre_scrollbar
            contenu_txt.pack(side=tk.LEFT)
            
            
# ancien code :
#texte = "\n".join(f"{clef}: {valeur}" for clef, valeur in liste_sportifs.dico_sportifs.items())
