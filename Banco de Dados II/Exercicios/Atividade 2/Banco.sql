CREATE DATABASE Yugioh

USE DATABASE Yugioh

CREATE TABLE Player(
  id_player INTEGER PRIMARY KEY AUTOINCREMENT,
  name_player VARCHAR(50),
  favorite_card VARCHAR(50)
)

CREATE TRIGGER Card
AFTER INSERT 
ON Player
FOR EACH ROW 
BEGIN
    IF NEW.favorite_card IS NULL THEN 
        INSERT INTO lembrete (id_player, mensagem)
        VALUES (NEW.id_player, CONCAT('Oi ', NEW.name, ', insira sua carta favorita'));
    END IF;
END;