-- Creazione del database
DROP DATABASE IF EXISTS shit_app;
CREATE DATABASE shit_app;

-- Connessione al database
\c shit_app

-- Creating the User table
CREATE TABLE "user" (
    "id" SERIAL PRIMARY KEY,
    "nickname" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) UNIQUE NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "surname" VARCHAR(50) NOT NULL,
    "sex" CHAR(1) CHECK (sex IN ('M', 'F')),
    "date_of_birth" DATE,
    "weight" DECIMAL(5, 2) CHECK (weight >= 0)
);

-- Creating the Team table
CREATE TABLE "team" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);

-- Creating the ShitColors table to classify shit based on predefined colors
CREATE TABLE "shit_color" (
    "id" SERIAL PRIMARY KEY,
    "color" VARCHAR(30) UNIQUE NOT NULL
);

-- Insert the 10 predefined colors into the ShitColors table
INSERT INTO shit_color (color)
VALUES 
    ('Yellow-Brown'),
    ('Brown'),
    ('Green-Brown'),
    ('Green-Black'),
    ('Green'),
    ('White or pale'),
    ('Bright red'),
    ('Black'),
    ('Red streacks');

CREATE TABLE "shit" (
    "id" SERIAL PRIMARY KEY,
    "shape" INT CHECK (shape >= 1 AND shape <= 7) NOT NULL,
    "quantity" INT CHECK (quantity >= 0 AND quantity <= 10),
    "colorID" INT REFERENCES shit_color(id) NOT NULL,
    "dimension" INT CHECK (dimension >= 0 AND dimension <= 10),  -- Assuming this is the intended constraint
    "level_of_satisfaction" INT CHECK (level_of_satisfaction >= 0 AND level_of_satisfaction <= 10),
    "userID" INT REFERENCES "user"(id) ON DELETE CASCADE,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    "notes" TEXT,
);

-- Creating the UserTeam table to represent the many-to-many relationship between Users and Teams
CREATE TABLE "user_team" (
    "userID" INT REFERENCES "user"(id) ON DELETE CASCADE,
    "teamID" INT REFERENCES "team"(id) ON DELETE CASCADE,
    PRIMARY KEY ("userID", "teamID")
);





