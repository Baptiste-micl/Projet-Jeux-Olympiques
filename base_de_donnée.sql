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
    FOREIGN KEY (pays_id) REFERENCES Pays(id_pays),
    FOREIGN KEY (id_discipline) REFERENCES Disciplines(id_discipline)
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

-- Table pour les lieux où se déroulent les épreuves
CREATE TABLE Lieu (
    id_lieu INT PRIMARY KEY,
    nom_lieu VARCHAR(100) NOT NULL,
    adresse VARCHAR(255),
    capacite INT
);

-- Table pour les épreuves
CREATE TABLE Epreuves (
    id_epreuve INT PRIMARY KEY,
    nom_epreuve VARCHAR(100) NOT NULL,
    date_debut DATE,
    date_fin DATE,
    id_lieu INT,
    id_discipline INT,
    FOREIGN KEY (id_lieu) REFERENCES Lieu(id_lieu),
    FOREIGN KEY (id_discipline) REFERENCES Disciplines(id_discipline)
);

-- Table pour les ventes de billets
CREATE TABLE Billets (
    id_billet INT PRIMARY KEY,
    id_epreuve INT,
    prix DECIMAL(10, 2),
    nombre_disponible INT,
    FOREIGN KEY (id_epreuve) REFERENCES Epreuves(id_epreuve)
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

-- Insertion pour les equipes

-- Insertion pour les lieux 
INSERT INTO Lieu
VALUES	(1, 'Paris', 'La Seine', '20000'),
	(2, 'Marseille', 'La plage', '10000');
