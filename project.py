from sqlalchemy.sql import text
from Project import sql


# def insert_doctor(data):

#     with sql.begin() as db:
        
#     res = db.execute(text("INSERT INTO Doctors (name, expertise, type, address, phone) VALUES (:name, :expertise, :type, :address, :phone)"))


# def insert_facilities(data)




doctors_data = [
    ('Dr. Shin Ho-Chul', 'General Practice', 'Kangbuk Samsung Hospital', '108 Pyong-dong, Chung-ku, Seoul', '2001-2911, 5100, 5110'),
    ('Dr. Yoo Shin-ae', 'General Practice', 'Samsung Medical Centre', '50 Ilwon-dong, Kangnam-ku, Seoul', '3410-0200'), 
    ('Dr. Kwak', 'General Practice', 'Seoul Chungang Hospital', '388-1 Poongnap-dong, Songpa-ku, Seoul', '3010-5001/2'), 
    ('Dr. H.S. Rhee', 'General Practice', 'Seoul Foreign Clinic', '5-3 Hannam-dong, Yongsan-ku, Seoul', '796-1871-2'), 
    ('Dr. John Linton', 'General Practice', 'Severance Yonsei Hospital', '134 Shinchon-dong, Sodaemun-ku, Seoul', '361-6540'),
    ('Dr. Jang', 'General Practice', 'Soonchunhyang Hospital' '657-58 Hannam-dong, Yongsan-ku, Seoul', '709-9158'),
    ('Dr. Ho-wan Han', 'Obstetrics and Gynaecology', 'Samsung Cheil Hospital', '1/23 Mukchung-dong, Chung-ku, Seoul', '2273-0151')
    ('Dr. Sung Hae-ree', 'Obstetrics and Gynaecology', 'UN Village Clinic', 'UN Village, Seoul', '790-0802'),
    ('Dr. Yoo Shin-ae', 'Paediatrics / Allergy', 'Samsung Medical Centre', '50 Ilwon-dong, Kangnam-ku, Seoul', '3410-0200'),
    ('Dr. Chung Chin-koo', 'Dentist', 'Unknown', '135-3 Itaewon-dong, Yongsan-ku, Seoul', '795-7726'),
    ('Dr. Lee Soo-chan', 'Dentist', 'Unknown', '186 Hangang-Ro, 2ga, Yongsan-ku, Seoul', '798-0500'),
    ('Dr. Kong', 'Opthamologist', 'Dr. Kong\'s Eye Clinic', 'Injoo Building, 111-1 Seorin-dong, Chongno-ku, Seoul', '733-6890'),
    ('Dr. James Lee', 'Chiropractic physician', 'Itaewon Wellnes', 'Itaewon Subway Exit #2, Hannam Bldg., 3F', '02-794-3536')
]


facilities_data = [
    ('Dong-A University Hospital','Ms. Kim, Sung-Ah' ,'Hospital', '1, Dongdaesin-dong 3-ga, Seo-gu', '240-2415', '240-5580'),
    ('Pusan National Univ. Hospital', 'Ms. Lee, Kyung-Ah', 'Hospital', 'Amidong 1-ga, Seo-gu', '240-7890', '240-7501'),
    ('Baptist Hospital', 'Ms. Song, Jung-Ok', 'Hospital', '374-75, Namsan-dong Geumjeong-gu', '580-1313', '580-1212'),
    ('Baptist Hospital', 'Mr. Lee, Jung-Sang', 'Hospital', '374-75, Namsan-dong Geumjeong-gu', '580-1251', '580-1212'),
    ('Inje Univ.Busan Paik Hospital', 'Mr. Cha, Ji-Hoon', 'Hospital', '633-165, Gaegeum 2-dong, Busanjin-gu', '890-6220', '890-6221'),
    ('Maryknoll General Hospital', 'Mr. Park, Myung-hwan', 'Hospital', '12, Daecheong-dong, 4-ga, jung-gu', '468-3858', '461-2300'),
    ('Kang Internal Medicine Clinic', 'Dr. Kang, Pil-joong', 'Clinic', '245-3, Bujeon 2-dong, Jin-Ku, Busan', 'NULL', '817-2334'),
    ('Ye Dental Clinic', 'Dr. Kim, Byung-Soo', 'Clinic', '255-1, Dong-A Bldg., 6th Floor, Bujeon 2-dong, Jin-Ku, Busan', 'NuLL', '808-2900')
]