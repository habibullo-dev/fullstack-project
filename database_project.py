import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, Date, Boolean

# Create an engine that connects to the MariaDB server
engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")
engine = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/")


# Connect to the server and create the database if it doesn't exist
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS Project"))

# Create a new engine that connects directly to the Project database
engine = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")

# Define the metadata object
metadata = MetaData()

# Define the Doctors table
Doctors = Table('Doctors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('expertise', String(255), nullable=False),
    Column('company', String(255)),
    Column('address', String(255)),
    Column('phone', String(255)),
    Column('ratings', String(20), nullable=True),  # Add nullable=True to avoid issues before column creation
    Column('availability', Date, nullable=True),  # Add nullable=True to avoid issues before column creation
    Column('about', String(255), nullable=True)
)

# Define Facilities table
Facilities = Table('Facilities', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('speaker', String(255)),
    Column('type', String(255)),
    Column('address', String(255)),
    Column('phone', String(20)),
    Column('emergency', String(20), nullable=False),
    Column('services', String(20), nullable=False)
)


Users = Table('Users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), nullable=False),
    Column('password', String(255), nullable=False),
    Column('email', String(255), nullable=False),
    Column('first_name', String(255), nullable=False),
    Column('last_name', String(255), nullable=False),
    Column('birth_date', Date),
    Column('gender', String(20)),
    Column('phone', String(15)),
    Column('allergy', String(255)),
    Column('condition', String(255)),
    Column('subscribe', Boolean, default=True),
    Column('logged_in', Boolean, default=False),
    Column('is_admin', Boolean, default=False),
    Column('join_date', Date, nullable=False)
)
# Create the tables if they don't exist
metadata.create_all(engine)

#print to see if database and tables are created
print("Database and tables created successfully.")


# Create a new engine that connects directly to the Project database
engine = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")


with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO Doctors (name, expertise, company, address, phone) VALUES (:name, expertise, :company, :address, :phone)"),
        {
            'name': 'Dr. Shin Ho-Chul', 
            'expertise': 'General Practice', 
            'company': 'Kangbuk Samsung Hospital', 
            'address': '108 Pyong-dong, Chung-ku, Seoul', 
            'phone': '2001-2911, 5100' 
        }
    )

    conn.execute(
        text("INSERT INTO Facilities (name, speaker, type, address, phone, emergency, services) VALUES (:name, :speaker, :type, :address, :phone, :emergency, :services)"),
        {
            'name': 'Yonsei University Medical Center, Severance Hospital', 
            'speaker': 'Dr. John Linton, M.D.', 
            'type': 'Hospital', 
            'address': '134 Shinchon-Dong, Seodaemun-Gu Seoul 120-752', 
            'phone': '2228-5800',
            'emergency': '010-9948-0983',
            'services': '24_hours'
        },
    )

    conn.commit()
    conn.close()

    conn = engine.connect()
    doctors_data = [
        {
            'name': 'Dr. Shin Ho-Chul', 
            'expertise': 'General Practice', 
            'company': 'Kangbuk Samsung Hospital', 
            'address': '108 Pyong-dong, Chung-ku, Seoul', 
            'phone': '2001-2911, 5100'
        },
        {
                'name': 'Dr. Yoo Shin-ae', 
                'expertise': 'General Practice', 
                'company': 'Samsung Medical Centre', 
                'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 
                'phone': '3410-0200'
        }, 
        {
                'name': 'Dr. Kwak', 'expertise': 'General Practice', 
                'company': 'Seoul Chungang Hospital', 
                'address': '388-1 Poongnap-dong, Songpa-ku, Seoul', 
                'phone': '3010-5001/2'
        }, 
        {
                'name': 'Dr. H.S. Rhee', 
                'expertise': 'General Practice', 
                'company': 'Seoul Foreign Clinic', 
                'address': '5-3 Hannam-dong, Yongsan-ku, Seoul', 
                'phone': '796-1871-2'
        }, 
        {
                'name': 'Dr. John Linton', 
                'expertise': 'General Practice', 
                'company': 'Severance Yonsei Hospital', 
                'address': '134 Shinchon-dong, Sodaemun-ku, Seoul', 
                'phone': '361-6540'
        },
        {
                'name': 'Dr. Jang', 
                'expertise': 'General Practice', 
                'company': 'Soonchunhyang Hospital', 
                'address': '657-58 Hannam-dong, Yongsan-ku, Seoul', 
                'phone': '709-9158'
        },
        {
                'name': 'Dr. Ho-wan Han', 
                'expertise': 'Obstetrics / Gynaecology', 
                'company': 'Samsung Cheil Hospital', 
                'address': '1/23 Mukchung-dong, Chung-ku, Seoul', 
                'phone': '2273-0151'
        },
        {
                'name': 'Dr. Sung Hae-ree', 
                'expertise': 'Obstetrics / Gynaecology', 
                'company': 'UN Village Clinic', 
                'address': 'UN Village, Seoul', 
                'phone': '790-0802'
        },
        {
                'name': 'Dr. Yoo Shin-ae', 
                'expertise': 'Paediatrics / Allergy', 
                'company': 'Samsung Medical Centre', 
                'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 
                'phone': '3410-0200'
        },
        {
                'name': 'Dr. Chung Chin-koo', 
                'expertise': 'Dentist', 
                'company': 'Global Dentist', 
                'address': '135-3 Itaewon-dong, Yongsan-ku, Seoul', 
                'phone': '795-7726'
        },
        {
                'name': 'Dr. Lee Soo-chan', 
                'expertise': 'Dentist', 
                'company': 'InterSeoul Dentist Clinic', 
                'address': '186 Hangang-Ro, 2ga, Yongsan-ku, Seoul', 
                'phone': '798-0500'
        },
        {
                'name': 'Dr. Kong', 
                'expertise': 'Opthamologist', 
                'company': "Dr. Kong's Eye Clinic", 
                'address': 'Injoo Building, 111-1 Seorin-dong, Chongno-ku, Seoul', 
                'phone': '733-6890'
        },
        {
                'name': 'Dr. James Lee', 
                'expertise': 'Chiropractic physician', 
                'company': 'Itaewon Wellnes', 
                'address': 'Itaewon Subway Exit #2, Hannam Bldg., 3F', 
                'phone': '02-794-3536'
        }
    ]

    conn.execute(
        text("INSERT INTO Doctors (name, expertise, company, address, phone) VALUES (:name, :expertise, :company, :address, :phone)"), doctors_data)


    conn.commit()
    conn.close()


    conn = engine.connect()

    facilities_data = [
        {
                'name': 'Dong-A University Hospital', 
                'speaker': 'Ms. Kim, Sung-Ah', 
                'type': 'Hospital', 
                'address': '1, Dongdaesin-dong 3-ga, Seo-gu', 
                'phone': '240-2415', 
                'emergency': '240-5580',
                'services': 'unknown'
        },
        {
                'name': 'Pusan National Univ. Hospital', 
                'speaker': 'Ms. Lee, Kyung-Ah', 
                'type': 'Hospital', 
                'address': 'Amidong 1-ga, Seo-gu', 
                'phone': '240-7890', 
                'emergency': '240-7501',
                'services': 'unknown'
        },
        {
                'name': 'Baptist Hospital', 
                'speaker': 'Ms. Song, Jung-Ok', 
                'type': 'Hospital', 
                'address': '374-75, Namsan-dong Geumjeong-gu', 
                'phone': '580-1313', 
                'emergency': '580-1212',
                'services': 'unknown'
        },
        {
                'name': 'Baptist Hospital', 
                'speaker': 'Mr. Lee, Jung-Sang', 
                'type': 'Hospital', 
                'address': '374-75, Namsan-dong Geumjeong-gu', 
                'phone': '580-1251', 
                'emergency': '580-1212',
                'services': 'unknown'
        },
        {
                'name': 'Inje Univ.Busan Paik Hospital', 
                'speaker': 'Mr. Cha, Ji-Hoon', 
                'type': 'Hospital', 
                'address': '633-165, Gaegeum 2-dong, Busanjin-gu', 
                'phone': '890-6220', 
                'emergency': '890-6221',
                'services': 'unknown'
        },
        {
                'name': 'Maryknoll General Hospital', 
                'speaker': 'Mr. Park, Myung-hwan', 
                'type': 'Hospital', 
                'address': '12, Daecheong-dong, 4-ga, jung-gu', 
                'phone': '468-3858', 
                'emergency': '461-2300',
                'services': 'unknown'
        },
        {
                'name': 'Kang Internal Medicine Clinic', 
                'speaker': 'Dr. Kang, Pil-joong', 
                'type': 'Clinic', 
                'address': '245-3, Bujeon 2-dong, Jin-Ku, Busan', 
                'phone': 'Unknown', 
                'emergency': '817-2334',
                'services': 'unknown'
        },
        {
                'name': 'Ye Dental Clinic', 
                'speaker': 'Dr. Kim, Byung-Soo', 
                'type': 'Clinic', 
                'address': '255-1, Dong-A Bldg., 6th Floor, Bujeon 2-dong, Jin-Ku, Busan', 
                'phone': 'Unknown', 
                'emergency': '808-2900',
                'services': 'unknown'
        }
    ]

    conn.execute(
        text("INSERT INTO Facilities(name, speaker, type, address, phone, emergency, services) VALUES (:name, :speaker, :type, :address, :phone, :emergency, :services)"), facilities_data)
    
    conn.commit()
    conn.close()

# Delete the ratings column in the Facilities table
    # with engine.begin() as db:
    #     db.execute(
    #         text("ALTER TABLE Facilities DROP COLUMN ratings")
    #     )
    #     db.commit()  
    #     db.close()


#  Reflect the existing database to get the current Doctors table schema
metadata.reflect(bind=engine)
Doctors = metadata.tables['Doctors']

# Connect to the Project database and perform the table modifications and updates

with engine.connect() as conn:
    # Add new columns to the Doctors table
    conn.execute(text("ALTER TABLE Doctors ADD ratings VARCHAR(20) NOT NULL"))
    conn.execute(text("ALTER TABLE Doctors ADD availability DATE NOT NULL"))
    conn.execute(text("ALTER TABLE Doctors ADD COLUMN about VARCHAR(255) NULL"))

    # Update the about column (one entry) in the Doctors table for testing purposes
    conn.execute(text("""
        UPDATE Doctors
        SET about = 'Comprehensive dental care with a gentle touch and patient education.'
        WHERE name = 'Dr. Chung Chin-Koo'
    """))

    # Update multiple doctors' about column in the Doctors table using SQL CASE
    conn.execute(text("""
        UPDATE Doctors
        SET about = CASE
            WHEN name = 'Dr. Shin Ho-Chul' THEN 'Over 15 years of experience, provides compassionate care, emphasizing preventive health, patient relationships, holistic wellness, and actively contributes to community outreach and medical education'
            WHEN name = 'Dr. Yoon Shin-ae' THEN 'Specializes in allergic diseases and immunology, creating supportive environments for children\'s health'
            WHEN name = 'Dr. Kwak' THEN 'Dedicated to comprehensive care, emphasizing open communication and patient empowerment'
            WHEN name = 'Dr. H.S. Rhee' THEN 'Extensive experience matched with excellence in patient care, fostering trust and confidence'
            WHEN name = 'Dr. John Linton' THEN 'Prioritizes preventive medicine and health education, empowering patients for wellness'
            WHEN name = 'Dr. Jang' THEN 'Expertise in general practice, compassionate and collaborative care for physical and emotional well-being'
            WHEN name = 'Dr. Ho-wan Han' THEN 'Compassionate care in obstetrics and gynaecology, guiding women through every reproductive stage'
            WHEN name = 'Dr. Sung Hae-Ree' THEN 'Passion for women\'s health, evidence-based care tailored to individual needs and preferences'
            WHEN name = 'Dr. Chung Chin-Koo' THEN 'Comprehensive dental care with a gentle touch and patient education'
            WHEN name = 'Dr. Lee Soo-Chan' THEN 'Skilled in various dental procedures, prioritizing personalized care and patient satisfaction'
            WHEN name = 'Dr. Kong' THEN 'Highly skilled in preserving and enhancing vision, personalized care with compassion and education'
            WHEN name = 'Dr. James Lee' THEN 'Enhances health naturally, specializing in spinal health and holistic therapies for balance and relief'
        END
        WHERE name IN ('Dr. Shin Ho-Chul', 'Dr. Yoon Shin-ae', 'Dr. Kwak', 'Dr. H.S. Rhee', 'Dr. John Linton', 'Dr. Jang', 'Dr. Ho-wan Han', 'Dr. Sung Hae-Ree', 'Dr. Chung Chin-Koo', 'Dr. Lee Soo-Chan', 'Dr. Kong', 'Dr. James Lee')
    """))

print("Table modified and data updated successfully.")


# Reflect the existing database to get the current Users table schema
metadata.reflect(bind=engine)
Users = metadata.tables['Users']

# Connect to the Project database and perform the modifications
with engine.connect() as conn:
    # Add new columns to the Users table with default values
    conn.execute(text("ALTER TABLE Users ADD COLUMN subscribe BOOLEAN DEFAULT true"))
    conn.execute(text("ALTER TABLE Users ADD COLUMN logged_in BOOLEAN DEFAULT false"))
    conn.execute(text("ALTER TABLE Users ADD COLUMN is_admin BOOLEAN DEFAULT false"))
    
    # Update all existing rows to set subscribe = true and logged_in = false
    conn.execute(text("UPDATE Users SET subscribe = true, logged_in = false"))

    # Update all existing rows to set is_admin = true for id IN (1, 2, 3, 4) and else = false
    conn.execute(text("""
        UPDATE Users
        SET 
            is_admin = CASE 
                          WHEN id IN (1, 2, 3, 4) THEN true
                          ELSE false
                      END
    """))

print("Table updated successfully.")

# Reflect the existing database to get the current Facilities table schema
metadata.reflect(bind=engine)
Facilities = metadata.tables['Facilities']


# Connect to the Project database and perform the data insertions and updates
with engine.connect() as conn:
    # Insert the second batch of data into the Facilities table
    conn.execute(text("""
        INSERT INTO Facilities (id, name, speaker, type, address, phone, emergency, services) VALUES
        (10, 'Samsung Medical Center', 'Unknown', 'Hospital', '50 Ilwong-Dong, Gangnam-Gu, Seoul', '3410-2114', '3410-2060', '24_hours'),
        (11, 'Asan Medical Center', 'Unknown', 'Hospital', '388-1 Pungnap-2 Dong, Songpa-Gu, Seoul', '3010-5001, 5002', '02-3010-3333', '24_hours'),
        (12, 'Soon Chun Hyang Univeristy Hospital', 'Unknown', 'Hospital', '657 Hannam-Dong, Yongsan-Gu, Seoul', '2072-2890', '2072-2473', '24_hours'),
        (13, 'Seoul National University Hospital', 'Unknown', 'Hospital', '28- Yeongeon-dong, Jonggo-gu, Seoul', '2072-2890', '2072-2473', '24_hours'),
        (14, "St. Mary's Hospital", 'Unknown', 'Hospital', '505 Banpo-dong, Seocho-gu, Seoul', '590-1114', '590-1632', '24_hours'),
        (15, 'Cha General Hospital', 'Unknown', 'Hospital', '650-9 Yeoksam-dong, Gangnam-gu, Seoul', '02-3465-3127', '010-4707-9179', '24_hours'),
        (16, 'Gangbuk Samsung Hospital', 'Unknown', 'Hospital', '108 Pyeong-dong, Jonggu-gu, Seoul', '02-2001-1101', '2001-1000', '24_hours'),
        (17, 'Samsung Cheil General Hospital', 'Unknown', 'Hospital', '1-19 Mukjeong-dong, Jung-gu, Seoul', '2000-7000', '02-2000-7062', '24_hours')
    """))

    # Update the rows in the Facilities table for testing purposes
    conn.execute(text("""
        UPDATE Facilities
        SET name = 'Kang Internal Medicine Clinic',
            speaker = 'Dr. Kang, Pil-joong',
            type = 'Clinic',
            address = '245-3, Bujeon 2-dong, Jin-Ku, Busan',
            phone = 'Unknown',
            emergency = '817-2334'
        WHERE id = 1
    """))

    conn.execute(text("""
        UPDATE Facilities
        SET name = 'Dong-A University Hospital',
            speaker = 'Ms. Kim, Sung-Ah',
            type = 'Hospital',
            address = '1, Dongdaesin-dong 3-ga, Seo-gu',
            phone = '240-2415',
            emergency = '240-5580'
        WHERE id = 7
    """))

print("Data inserted and updated successfully.")