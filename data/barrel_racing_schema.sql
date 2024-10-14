-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Horses Table
CREATE TABLE Horses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    breed VARCHAR(50),
    age INT,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Shows Table
CREATE TABLE Shows (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    date DATE NOT NULL
);

-- Rides Table
CREATE TABLE Rides (
    id SERIAL PRIMARY KEY,
    horse_id INT NOT NULL,
    show_id INT NOT NULL,
    time DECIMAL(10, 2) -- assuming time in seconds with two decimal places
    money_earned DECIMAL(10, 2),
    ride_date DATE NOT NULL,
    FOREIGN KEY (horse_id) REFERENCES horses(id) ON DELETE CASCADE,
    FOREIGN KEY (show_id) REFERENCES shows(id) ON DELETE CASCADE
);

-- Arenas Table
CREATE TABLE Arenas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

-- Ride_Arenas Table (Many-to-Many relationship)
CREATE TABLE Ride_Arenas (
    id SERIAL PRIMARY KEY,
    ride_id INT NOT NULL,
    arena_id INT NOT NULL,
    PRIMARY KEY (ride_id, arena_id),
    FOREIGN KEY (ride_id) REFERENCES rides(id) ON DELETE CASCADE,
    FOREIGN KEY (arena_id) REFERENCES arenas(id) ON DELETE CASCADE
);
