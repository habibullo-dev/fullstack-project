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
    join_date DATE NOT NULL
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
ALTER TABLE Facilities
ADD ratings VARCHAR(20) NOT NULL;

 

