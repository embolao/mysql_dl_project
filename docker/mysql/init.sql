CREATE DATABASE IF NOT EXISTS dl_data;

USE dl_data;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

INSERT INTO users (name, email, age) VALUES
('Alice', 'alice@example.com', 28),
('Bob', 'bob@example.com', 35),
('Charlie', 'charlie@example.com', 40);
