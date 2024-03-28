--
-- Création de la base de donnée
--

DROP DATABASE IF EXISTS Jeux_olympiques;

CREATE DATABASE Jeux_olympiques CHARACTER SET 'utf8';

USE Jeux_olympiques;

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
    description_discipline VARCHAR(255)
);

-- Table pour les sportifs
CREATE TABLE Sportifs (
    id_sportif INT PRIMARY KEY AUTO_INCREMENT,
    nom_sportif VARCHAR(100) NOT NULL,
    prenom_sportif VARCHAR(100) NOT NULL,
    date_de_naissance DATE,
    id_pays INT,
    id_discipline INT,
    FOREIGN KEY (id_pays) REFERENCES Pays(id_pays)
);

-- Table pour les résultats par pays (or, argent, bronze)
CREATE TABLE Resultats (
    id_resultat INT PRIMARY KEY AUTO_INCREMENT,
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
VALUES (1,'France', '[Image du drapeau français: URL non valide]'),
       (2,'États-Unis', '[Image du drapeau américain: URL non valide]'),
       (3,'Canada', '[Image du drapeau canadien: URL non valide]'),
       (4,'Angleterre', '[Image du drapeau britannique: URL non valide]'),
       (5,'Italie', '[Image du drapeau italien: URL non valide]');


-- Insertion pour les disciplines
INSERT INTO Disciplines 
VALUES (1,'Athlétisme', 'Course, saut, lancer'),
       (2,'Natation', 'Crawl, dos, papillon...'),
       (3,'Judo', 'un jeu de bagarre');

-- Insertion pour les sportifs
INSERT INTO Sportifs 
VALUES (1,'Mayer', 'Kevin', '1992-02-10', 1, 1),
       (2,'Riner', 'Teddy', '1989-04-07', 1, 3),
       (3,'Lyles', 'Noah', '1997-07-18', 2, 1),
       (4,'Phelps', 'Michael', '1985-06-30', 2, 2),
       (5,'Warner', 'Damian', '1989-10-04', 3, 1),
       (6,'Know', 'Finlay', '2001-01-08', 3, 2),
       (7,'Peaty', 'Adam', '1994-12-28', 4, 2),
       (8,'Clark', 'Sarah', '1978-01-03', 4, 3),
       (9,'Ceccon', 'Thomas', '2001-01-27', 5, 2),
       (10,'Basile', 'Fabio', '1994-09-07', 5, 3);


-- Insertion pour les resultats
INSERT INTO Resultats 
VALUES (1, 1, 1, 0, 0, 1),  -- France, Athlétisme
       (2, 1, 3, 0, 0, 0),  -- France, Judo
       (3, 2, 1, 1, 0, 0),  -- États-unis, Athlétisme
       (4, 2, 2, 0, 0, 0),  -- États-unis, Natation
       (5, 3, 1, 0, 0, 0),  -- Canada, Athlétisme
       (6, 3, 2, 1, 0, 0),  -- Canada, Natation
       (7, 4, 2, 0, 1, 0),  -- Angleterre, Natation
       (8, 4, 3, 0, 1, 0),  -- Angleterre, Judo
       (9, 5, 2, 0, 0, 0),  -- Italie, Natation
       (10, 5, 3, 0, 0, 0);  -- Italie, Judo
