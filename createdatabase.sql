--Run the docker container docker run <container_pid>
--Connect to container: docker exec -it <container_pid> bash
--mysql -u root -p example
CREATE DATABASE bookstore;
use bookstore;
CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INTEGER
);

CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
INSERT INTO author (name) VALUES ('Stephen King'),
('Agatha Christie'),
('Carmen Mola');


INSERT INTO book (title, author_id) VALUES ('The Shining', 1),
('Misery', 1),
('The Murder of Roger Ackroyd', 2),
('The Mysterious Affair at Styles', 2),
('El último verano', 3),
('Los días de fuego', 3);
