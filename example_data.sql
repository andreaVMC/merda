-- Inserting data into the user table
INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('johndoe', 'john.doe@example.com', 'hashed_password1', 'John', 'Doe', 'M', '1990-01-01', 70.50);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('janedoe', 'jane.doe@example.com', 'hashed_password2', 'Jane', 'Doe', 'F', '1992-02-02', 60.25);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('alice', 'alice@example.com', 'hashed_password3', 'Alice', 'Smith', 'F', '1985-03-03', 55.75);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('bob', 'bob@example.com', 'hashed_password4', 'Bob', 'Johnson', 'M', '1988-04-04', 80.00);

-- stalin@urss.it asdasdasd
INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('stalin1991', 'stalin@urss.it', '$2b$12$xgNo01WVreSpdxf/Dxd/wOywQKZJDvC23H6eWxm7yV9R6PJpSlegK', 'Joseph', 'Stalin', 'M', '2004-03-08', 80.00);

-- Inserting random data into the shit table
INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (2, 5, 1, 4, 7, 1, 'No issues', '2024-06-10 08:00:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (2, 3, 2, 6, 5, 2, 'Slightly soft', '2024-06-09 12:00:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (5, 2, 3, 2, 3, 1, 'Color unusual', '2024-06-08 15:00:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (6, 4, 1, 5, 6, 2, 'Normal experience', '2024-06-07 10:00:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (3, 1, 2, 3, 2, 3, 'Quick and easy', '2024-06-06 08:30:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (5, 7, 3, 8, 9, 1, 'Best one yet', '2024-06-05 11:45:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (4, 6, 1, 7, 8, 3, 'Satisfying', '2024-06-04 09:20:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (3, 5, 2, 6, 7, 2, 'Felt good', '2024-06-03 14:00:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (2, 2, 3, 4, 4, 2, 'Not bad', '2024-06-02 16:20:00');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes", "created_at")
VALUES (1, 8, 1, 9, 10, 1, 'Extremely satisfying', '2024-06-01 17:30:00');

-- Inserting random data in the team table
INSERT INTO team VALUES (1, 'Gli sterminatori di stitichezza');
INSERT INTO team VALUES (2, 'I re del trono');
INSERT INTO team VALUES (3, 'Gli scaricatori di fogne');
INSERT INTO team VALUES (4, 'Gli intasatori professionisti');
INSERT INTO team VALUES (5, 'Gli espellitori espliciti');
INSERT INTO team VALUES (6, 'I campioni di cacaton');
INSERT INTO team VALUES (7, 'Le macchine da defecazione');
INSERT INTO team VALUES (8, 'I virtuosi del WC');
INSERT INTO team VALUES (9, 'I padroni del bagno');
INSERT INTO team VALUES (10, 'Gli evacuatori eroici');

-- Inserting random data in the UserTeam table
INSERT INTO user_team VALUES (1, 1);
INSERT INTO user_team VALUES (2, 2);
INSERT INTO user_team VALUES (3, 3);
INSERT INTO user_team VALUES (4, 10);
INSERT INTO user_team VALUES (5, 10);


