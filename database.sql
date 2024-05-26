create database freebird;
USE freebird;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
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
	dest_id INT,
    name VARCHAR(255),
    description TEXT,
	FOREIGN KEY (dest_id) REFERENCES destinations(destina_id)
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

CREATE TABLE event (
	event_id INT AUTO_INCREMENT PRIMARY KEY,
	type VARCHAR(255),
	description TEXT,
	date DATE
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

CREATE TABLE reviews (
	review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT ,
    dest_id INT NULL ,
    accommodation_id INT NULL,
    review TEXT NOT NULL,
    rating INT ,
	attraction_id INT NULL,
    event_id INT  NULL,
    review_type ENUM('Write', 'View', 'Update') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (dest_id) REFERENCES destinations(destination_id),
    FOREIGN KEY (accommodation_id) REFERENCES accommodation(accommodation_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
	FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);


CREATE TABLE points (
	user_id INT PRIMARY KEY,
	points_expiry DATE,
	total_points INT(10),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
	);
CREATE TABLE groups (
	group_id INT AUTO_INCREMENT PRIMARY KEY,
        members TEXT,
	team_name VARCHAR(255)
	);

CREATE TABLE booking (
	user_id INT ,
	booking_id INT AUTO_INCREMENT PRIMARY KEY,
	start_t DATE,
    	finish DATE,
	event VARCHAR(255) NULL,
	destination VARCHAR(255), 
	FOREIGN KEY (user_id) REFERENCES users(user_id)
	);

INSERT INTO destinations (location, museums, nature, beach, hiking, art, history, science, wild_life, clubs, sports, food, shopping, mountains, forest, night_life, ratings)
VALUES
('Paris', 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 4.5),
('Sydney', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 4.8),
('Rio de Janeiro', 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 4.2),
('Tokyo', 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 4.6),
('Cape Town', 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 4.4);

INSERT INTO users (user_id, name, surname, email, username, password)
VALUES
(null, 'Maria', 'Nikolaou', 'marianik@email.com', 'MariaNik', 2545),
(null, 'Petros', 'Petrou', 'ppetrou@email.com', 'PetrouP', 2845),
(null, 'George', 'Papadopoulos', 'geopap@email.com', 'GeoPap', 25645);

INSERT INTO points (user_id, points_expiry, total_points) //επειδή δεν έχουμε υλοποιήσει τo περιβάλλον πληρωμής βάζουμε χειροκίνητα τιμή στους πόντους 
VALUES 
(3, '2025-04-27', 1200);

INSERT INTO booking (user_id, booking_id, start_t, finish, event, destination) values (3, null, '15/7/2024', '29/7/2024', null, 'Paris');
