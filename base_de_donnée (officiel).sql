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
    nom_pays VARCHAR(100) NOT NULL
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
VALUES (1,'France'),
       (2,'États-Unis'),
       (3,'Canada'),
       (4,'Angleterre'),
       (5,'Italie');


-- Insertion pour les disciplines
INSERT INTO Disciplines 
VALUES (1,'Athlétisme', 'L’athlétisme est un ensemble d’épreuves sportives codifiées comprenant les courses, sauts, lancers, épreuves combinées et marche.'),
       (2,'Natation', 'La natation désigne les méthodes qui permettent aux êtres humains de se mouvoir en milieu aquatique sans aucune autre force propulsive que leur propre énergie corporelle.'),
       (3,'Judo', 'Le judo est un art martial, créé au Japon en 1882 par Jigorō Kanō en tant que pédagogie physique, mentale et morale.');

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
       (10,'Basile', 'Fabio', '1994-09-07', 5, 3),
        (11, 'Spitz', 'Mark', '1950-02-10',2,2),
        (12, 'Lewis', 'Carl', '1961-07-01',2,1),
        (13, 'Thompson', 'Jenny', '1973-02-26',2,2),
        (14, 'Biondi', 'Matt', '1965-10-08',2,2),
        (15, 'Taylor', 'Henry', '1885-03-17',4,2)
        ;


-- Insertion pour les resultats
INSERT INTO Resultats 
VALUES (1, 1, 1, 0, 0, 1),  -- France, Athlétisme
       (2, 1, 2, 0, 1, 0),  -- France, Natation
       (3, 1, 3, 2, 1, 0),  -- France, Judo
       (4, 2, 1, 1, 0, 1),  -- États-unis, Athlétisme
       (5, 2, 2, 2, 0, 0),  -- États-unis, Natation
       (6, 2, 3, 0, 0, 0),  -- États-unis, Judo
       (7, 3, 1, 0, 0, 0),  -- Canada, Athlétisme
       (8, 3, 2, 0, 0, 1),  -- Canada, Natation
       (9, 3, 3, 0, 0, 0),  -- Canada, Judo
       (10, 4, 1, 0, 1, 0),  -- Angleterre, Athlétisme
       (11, 4, 2, 0, 0, 1),  -- Angleterre, Natation
       (12, 4, 3, 0, 0, 0),  -- Angleterre, Judo
       (13, 5, 1, 0, 0, 0),  -- Italie, Athlétisme
       (14, 5, 2, 0, 1, 0),  -- Italie, Natation
       (15, 5, 3, 0, 0, 1);  -- Italie, Judo
