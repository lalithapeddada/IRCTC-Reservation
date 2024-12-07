USE railway_db;
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(80) NOT NULL,
    role ENUM('admin', 'user') NOT NULL
);
CREATE TABLE Train (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    source VARCHAR(80) NOT NULL,
    destination VARCHAR(80) NOT NULL,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL
);
CREATE TABLE Booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    train_id INT NOT NULL,
    seats_booked INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (train_id) REFERENCES Train(id)
);
SHOW TABLES;
DESCRIBE User;
INSERT INTO User (username, password, role) VALUES ('admin', 'admin123', 'admin');
INSERT INTO Train (name, source, destination, total_seats, available_seats) 
VALUES ('Express Train', 'Station A', 'Station B', 100, 100);
SHOW TABLES;
SELECT * FROM User;
SHOW TABLES;
SELECT * FROM User;
SELECT * FROM Train;
