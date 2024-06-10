-- Inserting data into the user table
INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('johndoe', 'john.doe@example.com', 'hashed_password1', 'John', 'Doe', 'M', '1990-01-01', 70.50);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('janedoe', 'jane.doe@example.com', 'hashed_password2', 'Jane', 'Doe', 'F', '1992-02-02', 60.25);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('alice', 'alice@example.com', 'hashed_password3', 'Alice', 'Smith', 'F', '1985-03-03', 55.75);

INSERT INTO "user" (nickname, email, password, name, surname, sex, date_of_birth, weight)
VALUES ('bob', 'bob@example.com', 'hashed_password4', 'Bob', 'Johnson', 'M', '1988-04-04', 80.00);

-- Inserting random data into the shit table
INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (2, 5, 1, 4, 7, 1, 'No issues');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (2, 3, 2, 6, 5, 2, 'Slightly soft');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (5, 2, 3, 2, 3, 1, 'Color unusual');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (6, 4, 1, 5, 6, 2, 'Normal experience');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (3, 1, 2, 3, 2, 3, 'Quick and easy');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (5, 7, 3, 8, 9, 1, 'Best one yet');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (4, 6, 1, 7, 8, 3, 'Satisfying');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (3, 5, 2, 6, 7, 2, 'Felt good');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (2, 2, 3, 4, 4, 2, 'Not bad');

INSERT INTO shit ("shape", "quantity", "colorID", "dimension", "level_of_satisfaction", "userID", "notes")
VALUES (1, 8, 1, 9, 10, 1, 'Extremely satisfying');
