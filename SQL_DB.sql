DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contacts;

CREATE TABLE genders
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       VARCHAR(30),
    email      VARCHAR(30),
    password   VARCHAR(30),
    age        TINYINT UNSIGNEG,
    gender_id  INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gender_id) REFERENCES genders (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE contacts
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       VARCHAR(30),
    email      VARCHAR(30),
    phone      VARCHAR(30),
    favorite   BOOLEAN,
    user_id    INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO genders (name)
VALUES ('male'),
       ('female');

INSERT INTO users (name, email, password, age, gender_id)
VALUES ('Boris', 'boris@test.com', 'password', 23, 1),
       ('Alina', 'alina@test.com', 'password', 32, 2),
       ('Maksim', 'maksim@test.com', 'password', 40, 1);

INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
       ('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
       ('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
       ('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
       ('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);
