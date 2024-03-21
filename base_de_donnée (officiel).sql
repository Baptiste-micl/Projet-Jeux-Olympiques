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
INSERT INTO Pays (nom_pays, drapeau_pays)
VALUES ('France', '[Image du drapeau français: URL non valide]'),
       ('États-Unis', '[Image du drapeau américain: URL non valide]'),
       ('Canada', '[Image du drapeau canadien: URL non valide]'),
       ('Angleterre', '[Image du drapeau britannique: URL non valide]'),
       ('Italie', '[Image du drapeau italien: URL non valide]');


-- Insertion pour les disciplines
INSERT INTO Disciplines (nom_discipline, description_discipline)
VALUES ('Athlétisme', 'Course, saut, lancer'),
       ('Natation', 'Crawl, dos, papillon...'),
       ('Judo', 'un jeu de bagarre');

-- Insertion pour les sportifs
INSERT INTO Sportifs (nom_sportif, prenom_sportif, date_de_naissance, id_pays, id_discipline)
VALUES ('Mayer', 'Kevin', '1992-02-10', 1, 1),
       ('Riner', 'Teddy', '1989-04-07', 1, 3),
       ('Lyles', 'Noah', '1997-07-18', 2, 1),
       ('Phelps', 'Michael', '1985-06-30', 2, 2),
       ('Warner', 'Damian', '1989-10-04', 3, 1),
       ('Know', 'Finlay', '2001-01-08', 3, 2)
       ('Peaty', 'Adam', '1994-12-28', 4, 2),
       ('Clark', 'Sarah', '1978-01-03', 4, 3),
       ('Ceccon', 'Thomas', '2001-01-27', 5, 2),
       ('Basile', 'Fabio', '1994-09-07', 5, 3);


-- Insertion pour les resultats
INSERT INTO Resultats (id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze)
VALUES (1, 2, 1, 0, 0),  -- France, Athlétisme
       (1, 1, 1, 0, 0),  -- France, Judo
       (2, 1, 0, 1, 0),  -- États-unis, Athlétisme
       (2, 6, 1, 0, 0),  -- États-unis, Natation
       (3, 6, 1, 0, 0),  -- Canada, Athlétisme
       (3, 6, 0, 1, 0),  -- Canada, Natation
       (4, 8, 0, 0, 1),  -- Angleterre, Natation
       (4, 8, 0, 0, 1),  -- Angleterre, Judo
       (5, 4, 1, 0, 0);  -- Italie, Natation
       (5, 4, 1, 0, 0);  -- Italie, Judo
