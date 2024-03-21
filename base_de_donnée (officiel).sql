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
    id_equipe INT,
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
INSERT INTO Sportifs (nom_sportif, prenom_sportif, date_de_naissance, id_pays, id_discipline, id_equipe)
VALUES ('Mayer', 'Kevin', '1992-02-10', 1, 1, 1),
       ('Riner', 'Teddy', '1989-04-07', 1, 3, 2),
       ('Lyles', 'Noah', '1997-07-18', 2, 1, 3),
       ('Phelps', 'Michael', '1985-06-30', 2, 2, 4),
       ('Warner', 'Damian', '1989-10-04', 3, 1, 5),
       ('Know', 'Finlay', '2001-01-08', 3, 2, 6)
       ('Peaty', 'Adam', '1994-12-28', 4, 2, 7),
       ('Clark', 'Sarah', '1978-01-03', 4, 3, 8),
       ('Ceccon', 'Thomas', '2001-01-27', 5, 2, 9),
       ('Basile', 'Fabio', '1994-09-07', 5, 3, 10);


-- Insertion pour les equipes
INSERT INTO Equipes (nom_equipe, id_pays, id_discipline, id_sportif)
VALUES ('equipe de France d athlétisme','1','1','1')
       ('equipe de France de judo', '1', '3', '2')
       ('equipe des états-unis d athlétisme', '2', '1', '3')
       ('equipe des état-unis de natation', '2', '2', '4')
       ('equipe du canada d athlétisme')
       ('equipe du canada de natation')
       ('equipe d Angleterre de natation')
       ('equipe d Angleterre de judo')
       ('equipe d Italie de natation')
       ('equipe d Italie de judo')


-- Insertion pour les resultats
INSERT INTO Resultats (id_pays, id_discipline, medaille_or, medaille_argent, medaille_bronze)
VALUES (2, 2, 1, 0, 0),  -- USA, Natation, Or
       (1, 1, 1, 0, 0),  -- France, Athlétisme, Or
       (3, 1, 0, 1, 0),  -- Canada, Athlétisme, Argent
       (1, 6, 1, 0, 0),  -- France, Tennis, Or
       (2, 6, 1, 0, 0),  -- USA, Tennis, Or
       (3, 6, 0, 1, 0),  -- Canada, Tennis, Argent
       (1, 8, 0, 0, 1),  -- France, Gymnastique, Bronze
       (7, 4, 1, 0, 0);  -- Espagne, Football, Or
