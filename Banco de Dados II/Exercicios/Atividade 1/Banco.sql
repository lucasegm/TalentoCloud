CREATE DATABASE Yougioh

USE DATABASE Yougioh

CREATE TABLE Players (
    id_player INTEGER PRIMARY KEY AUTOINCREMENT,
    name_player VARCHAR(50),
    age_player INTEGER
);


CREATE TABLE Cards (
    id_card INTEGER PRIMARY KEY AUTOINCREMENT,
    name_card VARCHAR(50),
    id_player INTEGER,
    FOREIGN KEY (id_player) REFERENCES Players (id_player)
);

INSERT INTO Players(name_player, age_player) values ('Yougi', 15);
INSERT INTO Players(name_player, age_player) values ('Kaiba', 18);

INSERT INTO Cards(name_card, id_player) values ('Mago Negro', 1);
INSERT INTO Cards(name_card, id_player) values ('Dragão Branco de Olhos Azuis', 2);

SELECT name_player, name_card FROM Cards
RIGHT JOIN Players
on Players.id_player = cards.id_card

SELECT name_player, name_card FROM Cards
LEFT JOIN Players
on Players.id_player = cards.id_card

SELECT name_player, name_card FROM Cards
INNER JOIN Players
on Players.id_player = cards.id_card

SELECT name_player, name_card FROM Cards
LEFT JOIN Players
on Players.id_player = cards.id_card
UNION
SELECT name_player, name_card FROM Cards
RIGHT JOIN Players
on Players.id_player = cards.id_card