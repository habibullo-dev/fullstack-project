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
    speaker VARCHAR(255),
    type VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(20),
    emergency VARCHAR(20),
    services VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE, 
    gender VARCHAR(20),
    phone VARCHAR(15),
    allergy VARCHAR(255),
    `condition` VARCHAR(255),
    subscribe BOOLEAN DEFAULT true,
    logged_in BOOLEAN DEFAULT false,
    is_admin BOOLEAN DEFAULT false,
    join_date DATE NOT NULL
);

-- Add the new columns with default values to the Users table
ALTER TABLE Users
ADD COLUMN subscribe BOOLEAN DEFAULT true,
ADD COLUMN logged_in BOOLEAN DEFAULT false;

-- Add new column with default value = false to the Users table
ALTER TABLE Users
ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;


-- Update all existing rows to set subscribe = true and logged_in = false
UPDATE Users
SET subscribe = true, logged_in = false;

-- Update all existing rows to set is_admin = true for id[1,2,3,4] and else = false
UPDATE Users
SET 
    subscribe = true,
    logged_in = false,
    is_admin = CASE 
                    WHEN id IN (1,2,3,4) THEN true
                    ELSE false
                END;


-- Create a new table for password resetCREATE TABLE PasswordReset (
    CREATE TABLE IF NOT EXISTS PasswordReset (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    token VARCHAR(255) NOT NULL,
    expiration_date DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Second batch of data for the Facilities Table in the Database Project

INSERT INTO Facilities (id, name, speaker, type, address, phone, emergency, services) VALUES
(10, 'Samsung Medical Center', 'Unknown', 'Hospital', '50 Ilwong-Dong, Gangnam-Gu, Seoul', '3410-2114', '3410-2060', '24_hours'),
(11, 'Asan Medical Center', 'Unknown', 'Hospital', '388-1 Pungnap-2 Dong, Songpa-Gu, Seoul', '3010-5001, 5002', '02-3010-3333', '24_hours'),
(12, 'Soon Chun Hyang Univeristy Hospital', 'Unknown', 'Hospital', '657 Hannam-Dong, Yongsan-Gu, Seoul', '2072-2890', '2072-2473', '24_hours'),
(13, 'Seoul National University Hospital', 'Unknown', 'Hospital', '28- Yeongeon-dong, Jonggo-gu, Seoul', '2072-2890', '2072-2473', '24_hours'),
(14, "St. Mary's Hospital", 'Unknown', 'Hospital', '505 Banpo-dong, Seocho-gu, Seoul', '590-1114', '590-1632', '24_hours'),
(15, 'Cha General Hospital', 'Unknown', 'Hospital', '650-9 Yeoksam-dong, Gangnam-gu, Seoul', '02-3465-3127', '010-4707-9179', '24_hours'),
(16, 'Gangbuk Samsung Hospital', 'Unknown', 'Hospital', '108 Pyeong-dong, Jonggu-gu, Seoul', '02-2001-1101', '2001-1000', '24_hours'),
(17, 'Samsung Cheil General Hospital', 'Unknown', 'Hospital', '1-19 Mukjeong-dong, Jung-gu, Seoul', '2000-7000', '02-2000-7062', '24_hours');


-- Update table rows for testing purposes
UPDATE Facilities
SET name = 'Kang Internal Medicine Clinic',
    speaker = 'Dr. Kang, Pil-joong',
    type = 'Clinic',
    address = '245-3, Bujeon 2-dong, Jin-Ku, Busan',
    phone = 'Unknown',
    emergency = '817-2334'
WHERE id = 1;

UPDATE Facilities
SET name = 'Dong-A University Hospital',
    speaker = 'Ms. Kim, Sung-Ah',
    type = 'Hospital',
    address = '1, Dongdaesin-dong 3-ga, Seo-gu',
    phone = '240-2415',
    emergency = '240-5580'
WHERE id = 7;

-- Update the table column for extra stuff
ALTER TABLE Doctors
ADD ratings VARCHAR(20) NOT NULL;

 
ALTER TABLE Doctors
ADD availability DATE NOT NULL;


-- Add new column called about with default sentences to the Doctors Table
ALTER TABLE Doctors
ADD COLUMN about VARCHAR(255) NULL


-- Update the about column (one entry) in the Doctors Table <----- FOR TEST PURPOSES ONLY
UPDATE Doctors
SET about = 'Comprehensive dental care with a gentle touch and patient education.'
WHERE name = 'Dr. Chung Chin-Koo';

-- Update multiple doctors about Column in the Doctors Table using SQL CASE
UPDATE Doctors
SET about =
    CASE
        WHEN name = 'Dr. Shin Ho-Chul' THEN 'Over 15 years of experience, provides compassionate care, emphasizing preventive health, patient relationships, holistic wellness, and actively contributes to community outreach and medical education'
        WHEN name = 'Dr. Yoon Shin-ae' THEN 'Specializes in allergic diseases and immunology, creating supportive environments for children\s health'
        WHEN name = 'Dr. Kwak' THEN 'Dedicated to comprehensive care, emphasizing open communication and patient empowerment'
        WHEN name = 'Dr. H.S. Rhee' THEN 'Extensive experience matched with excellence in patient care, fostering trust and confidence'
        WHEN name = 'Dr. John Linton' THEN 'Priorities preventive medicine and health education, empowering patients for wellness'
        WHEN name = 'Dr. Jang' THEN 'Expertise in general practice, compassionate and collaborative care for physical and emotional well-being'
        WHEN name = 'Dr. Ho-wan Han' THEN 'Compassionate care in obstetrics and gynaecology, guiding women through every reproductive stage'
        WHEN name = 'Dr. Sung Hae-Ree' THEN 'Passion for women\s health, evidence-based care tailored to individual needs and preferences'
        WHEN name = 'Dr. Chung Chin-koo' THEN 'Comprehensive dental care with a gentle touch and patient education'
        WHEN name = 'Dr. Lee Soo-Chan' THEN 'Skilled in various dental procedures, prioritizing personalized care and patient satisfaction'
        WHEN name = 'Dr. Kong' THEN 'Highly skilled in preserving and enhancing vision, personalized care with compassion and education'
        WHEN name = 'Dr. James Lee' THEN 'Enhances health naturally, specializing in spinal health and holistic therapies for balance and relief'
    END
WHERE name IN ('Dr. Shin Ho-Chul', 'Dr. Yoon Shin-ae', 'Dr. Kwak', 'Dr. H.S. Rhee', 'Dr. John Linton', 'Dr. Jang', 'Dr. Ho-wan Han', 'Dr. Sung Hae-Ree', 'Dr. Chung chin-koo', 'Dr. Lee Soo-Chan', 'Dr. Kong', 'Dr. James Lee');

-- No ELSE part and no conditions are true, it returns NULL
-- about column in the Doctors Table is set to NULL
 


-- We will not use these sql query / schema from below to save the images we have into the database
-- This only acts as an example on how to alter a table and insert an image as blob


-- Add new column called images with data type blob to Doctors table
ALTER TABLE Doctors
ADD COLUMN IF NOT EXISTS images BLOB;

-- Drop column images in the Doctors Table 
ALTER TABLE Doctors
DROP COLUMN images
