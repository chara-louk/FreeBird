create database freebird;
USE freebird;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255),
    points INT(5)
);
CREATE TABLE filters (
    filter_id INT AUTO_INCREMENT PRIMARY KEY,
    ratings FLOAT,
    travelers INT,
    start DATE,
    finish DATE,
    additional_needs TEXT,
	budget float
);

CREATE TABLE destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255),
    attractions TEXT,
    additional_needs TEXT,
    museums BOOLEAN,
    nature BOOLEAN,
    beach BOOLEAN,
    hiking BOOLEAN,
    art BOOLEAN,
    history BOOLEAN,
    science BOOLEAN,
    wild_life BOOLEAN,
    clubs BOOLEAN,
    sports BOOLEAN,
    food BOOLEAN,
    shopping BOOLEAN,
    mountains BOOLEAN, 
    forest BOOLEAN, 
    night_life BOOLEAN,
    ratings FLOAT,
    filter_id INT,
    FOREIGN KEY (filter_id) REFERENCES filters(filter_id)
);


CREATE TABLE attractions (
    attraction_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

CREATE TABLE destination_attraction (
    dest_id INT,
    attraction_id INT,
    PRIMARY KEY (dest_id, attraction_id),
    FOREIGN KEY (dest_id) REFERENCES destinations(destination_id),
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);



CREATE TABLE accommodation (
    accommodation_id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE transportation (
    transportation_id INT AUTO_INCREMENT PRIMARY KEY,
    dest_id INT,
    start DATE,
    finish DATE,
    type ENUM('plane', 'ship'),
    cost FLOAT,
    FOREIGN KEY (dest_id) REFERENCES destinations(destination_id)
);



CREATE TABLE trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT,
    user_id INT,
    accommodation_id INT,
    transportation_id INT,
    booking_id INT,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (accommodation_id) REFERENCES accommodation(accommodation_id),
    FOREIGN KEY (transportation_id) REFERENCES transportation(transportation_id)
	);
