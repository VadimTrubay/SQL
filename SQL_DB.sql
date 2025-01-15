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

SELECT * FROM contacts

SELECT name, email FROM contacts ORDER BY name

SELECT name, email
FROM contacts
WHERE favorite = true
ORDER BY name

SELECT name, email
FROM users
WHERE age IN(20, 30, 40)
ORDER BY name

SELECT name, email, age
FROM users
WHERE age BETWEEN 30 AND 40
ORDER BY name

SELECT name, email
FROM contacts
WHERE name LIKE '%L%'
ORDER BY name

SELECT name, email, age
FROM users
WHERE age NOT BETWEEN 30 AND 40
ORDER BY name

SELECT min(age) as minAge
FROM users

SELECT avg(age) as averageAge
FROM users

SELECT COUNT(user_id) as total_contacts, user_id
FROM contacts
GROUP BY user_id

SELECT *
FROM contacts
WHERE user_id IN (SELECT id
    FROM users
    WHERE age < 30)

SELECT id, name as fullName, phone as mobile
FROM contacts

SELECT u.id, u.name, u.email, g.name AS gender
FROM users AS u
INNER JOIN genders AS g ON g.id = u.gender_id

SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
JOIN users AS u ON u.id = c.user_id

UPDATE contacts SET user_id = 3 WHERE id = 5;

DELETE FROM contacts WHERE id = 4;

TRUNCATE TABLE contacts;

DROP TABLE contacts;

ALTER TABLE table_name CHANGE column_a column_b INTEGER;

ALTER TABLE table_name MODIFY column_b BIGINT NOT NULL;

ALTER TABLE table_name ADD column_c FLOAT;

ALTER TABLE table_name ADD column_d VARCHAR(30) AFTER column_c;

ALTER TABLE table_name DROP COLUMN column_c;

ALTER TABLE table_name ADD INDEX index_name_ix (column_b);

CREATE INDEX fullname_ix ON users (fullname);

DROP INDEX table1_price_ix ON table1;

ALTER TABLE table1 ADD CONSTRAINT table1_id_pk PRIMARY KEY (id);

ALTER TABLE table1 DROP PRIMARY KEY;

CREATE TABLE persons (
    id INT PRIMARY KEY,
    email CHAR(50) NOT NULL,
    fullName varchar(100) NULL,
    CONSTRAINT persons_email_un UNIQUE KEY (email)
);












