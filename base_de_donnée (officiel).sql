--
-- Création des tables :
--

CREATE TABLE Pays (
    id_pays INT PRIMARY KEY,
    nom_pays VARCHAR(100) NOT NULL,
    drapeau_pays VARCHAR(255)
);

-- Table pour les disciplines
CREATE TABLE Disciplines (
    id_discipline INT PRIMARY KEY,
    nom_discipline VARCHAR(100) NOT NULL,
    description_discipline INT
);

-- Table pour les sportifs
CREATE TABLE Sportifs (
    id_sportif INT PRIMARY KEY,
    nom_sportif VARCHAR(100) NOT NULL,
    prenom_sportif VARCHAR(100) NOT NULL,
    date_de_naissance DATE,
    id_pays INT,
    id_discipline INT,
    FOREIGN KEY (id_pays) REFERENCES Pays(id_pays)
);

-- Table pour les équipes
CREATE TABLE Equipes (
    id_equipe INT PRIMARY KEY,
    nom_equipe VARCHAR(100) NOT NULL,
    id_pays INT,
    id_discipline INT,
    id_sportif INT,
    FOREIGN KEY (id_pays) REFERENCES Pays(id_pays),
    FOREIGN KEY (id_discipline) REFERENCES Disciplines(id_discipline)
    FOREIGN KEY (id_sportif) REFERENCES Sportifs(id_sportif)
);

-- Table pour les résultats par pays (or, argent, bronze)
CREATE TABLE Resultats (
    id_resultat INT PRIMARY KEY,
    id_pays INT,
    id_discipline INT,
    medaille_or INT DEFAULT 0,
    medaille_argent INT DEFAULT 0,
    medaille_bronze INT DEFAULT 0,
    FOREIGN KEY (id_pays) REFERENCES Pays(id_pays),
    FOREIGN KEY (id_discipline) REFERENCES Disciplines(id_discipline)
);





--
-- Insertion de valeurs dans les tables :
--


-- Insertion pour les Pays
INSERT INTO Pays
VALUES	(1, 'FRANCE', 'https://fr.wikipedia.org/wiki/Drapeau_de_la_France#/media/Fichier:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg'),
	(2, 'ALLEMAGNE', 'https://fr.wikipedia.org/wiki/Drapeau_de_l%27Allemagne#/media/Fichier:Flag_of_Germany.svg');


-- Insertion pour les disciplines
INSERT INTO Pays
VALUES	(1, 'Foot', 'Un jeu avec un ballon'),
	(2, 'Judo', 'a quand gary vs kenzi ?');