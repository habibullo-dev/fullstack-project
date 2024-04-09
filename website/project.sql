-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS Project;


-- Use the Project database
USE Project;


-- Create the Doctors table if not exist
CREATE TABLE IF NOT EXISTS Doctors(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    expertise VARCHAR(255), 
    type VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(20)
);


-- Create the Facilities table if not exist
CREATE TABLE IF NOT EXISTS Facilities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    speaker VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(20)
);

