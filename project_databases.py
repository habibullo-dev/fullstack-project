import sqlalchemy
from sqlalchemy.sql import text

engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")
# engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23")



# @app.route('/database')
# def insert_data():
#     conn = engine.connect()

#         Insert data into Doctors table
#         conn.execute(
#             text("INSERT INTO Doctors (name, expertise, company, address, phone) VALUES (:name, :expertise, :company, :address, :phone)"),
#             {
#                 'name': 'Dr. Shin Ho-Chul', 
#                 'expertise': 'General Practice', 
#                 'company': 'Kangbuk Samsung Hospital', 
#                 'address': '108 Pyong-dong, Chung-ku, Seoul', 
#                 'phone': '2001-2911, 5100'
#             }
#         )

#         conn.execute(
#             text("INSERT INTO Facilities (name, speaker, type, address, phone, emergency, services) VALUES (:name, :speaker, :type, :address, :phone, :emergency, :services)"),
#             {
#                 'name': 'Yonsei University Medical Center, Severance Hospital', 
#                 'speaker': 'Dr. John Linton, M.D.', 
#                 'company': 'Hospital', 
#                 'address': '134 Shinchon-Dong, Seodaemun-Gu Seoul 120-752', 
#                 'phone': '2228-5800',
#                 'emergency': '010-9948-0983',
#                 'services': '24_hours'
#             },
#         )

#         conn.commit()
#         conn.close()

#         conn = engine.connect()

#         doctors_data = [
#             {
#                 'name': 'Dr. Shin Ho-Chul', 
#                 'expertise': 'General Practice', 
#                 'company': 'Kangbuk Samsung Hospital', 
#                 'address': '108 Pyong-dong, Chung-ku, Seoul', 
#                 'phone': '2001-2911, 5100'
#             },
#             {
#                   'name': 'Dr. Yoo Shin-ae', 
#                   'expertise': 'General Practice', 
#                   'company': 'Samsung Medical Centre', 
#                   'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 
#                   'phone': '3410-0200'
#             }, 
#             {
#                   'name': 'Dr. Kwak', 'expertise': 'General Practice', 
#                   'company': 'Seoul Chungang Hospital', 
#                   'address': '388-1 Poongnap-dong, Songpa-ku, Seoul', 
#                   'phone': '3010-5001/2'
#             }, 
#             {
#                   'name': 'Dr. H.S. Rhee', 
#                   'expertise': 'General Practice', 
#                   'company': 'Seoul Foreign Clinic', 
#                   'address': '5-3 Hannam-dong, Yongsan-ku, Seoul', 
#                   'phone': '796-1871-2'
#             }, 
#             {
#                   'name': 'Dr. John Linton', 
#                   'expertise': 'General Practice', 
#                   'company': 'Severance Yonsei Hospital', 
#                   'address': '134 Shinchon-dong, Sodaemun-ku, Seoul', 
#                   'phone': '361-6540'
#             },
#             {
#                   'name': 'Dr. Jang', 
#                   'expertise': 'General Practice', 
#                   'company': 'Soonchunhyang Hospital', 
#                   'address': '657-58 Hannam-dong, Yongsan-ku, Seoul', 
#                   'phone': '709-9158'
#             },
#             {
#                   'name': 'Dr. Ho-wan Han', 
#                   'expertise': 'Obstetrics and Gynaecology', 
#                   'company': 'Samsung Cheil Hospital', 
#                   'address': '1/23 Mukchung-dong, Chung-ku, Seoul', 
#                   'phone': '2273-0151'
#             },
#             {
#                   'name': 'Dr. Sung Hae-ree', 
#                   'expertise': 'Obstetrics and Gynaecology', 
#                   'company': 'UN Village Clinic', 
#                   'address': 'UN Village, Seoul', 
#                   'phone': '790-0802'
#             },
#             {
#                   'name': 'Dr. Yoo Shin-ae', 
#                   'expertise': 'Paediatrics / Allergy', 
#                   'company': 'Samsung Medical Centre', 
#                   'address': '50 Ilwon-dong, Kangnam-ku, Seoul', 
#                   'phone': '3410-0200'
#             },
#             {
#                   'name': 'Dr. Chung Chin-koo', 
#                   'expertise': 'Dentist', 
#                   'company': 'Unknown', 
#                   'address': '135-3 Itaewon-dong, Yongsan-ku, Seoul', 
#                   'phone': '795-7726'
#             },
#             {
#                   'name': 'Dr. Lee Soo-chan', 
#                   'expertise': 'Dentist', 
#                   'company': 'Unknown', 
#                   'address': '186 Hangang-Ro, 2ga, Yongsan-ku, Seoul', 
#                   'phone': '798-0500'
#             },
#             {
#                   'name': 'Dr. Kong', 
#                   'expertise': 'Opthamologist', 
#                   'company': "Dr. Kong's Eye Clinic", 
#                   'address': 'Injoo Building, 111-1 Seorin-dong, Chongno-ku, Seoul', 
#                   'phone': '733-6890'
#             },
#             {
#                   'name': 'Dr. James Lee', 
#                   'expertise': 'Chiropractic physician', 
#                   'company': 'Itaewon Wellnes', 
#                   'address': 'Itaewon Subway Exit #2, Hannam Bldg., 3F', 
#                   'phone': '02-794-3536'
#             }
#         ]

#         # conn.execute(
#         #     text("INSERT INTO Doctors (name, expertise, company, address, phone) VALUES (:name, :expertise, :company, :address, :phone)"), doctors_data)


#         conn.commit()
#         conn.close()


#         conn = engine.connect()

#         facilities_data = [
#             {
#                   'name': 'Dong-A University Hospital', 
#                   'speaker': 'Ms. Kim, Sung-Ah', 
#                   'type': 'Hospital', 
#                   'address': '1, Dongdaesin-dong 3-ga, Seo-gu', 
#                   'phone': '240-2415', 
#                   'emergency': '240-5580',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Pusan National Univ. Hospital', 
#                   'speaker': 'Ms. Lee, Kyung-Ah', 
#                   'type': 'Hospital', 
#                   'address': 'Amidong 1-ga, Seo-gu', 
#                   'phone': '240-7890', 
#                   'emergency': '240-7501',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Baptist Hospital', 
#                   'speaker': 'Ms. Song, Jung-Ok', 
#                   'type': 'Hospital', 
#                   'address': '374-75, Namsan-dong Geumjeong-gu', 
#                   'phone': '580-1313', 
#                   'emergency': '580-1212',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Baptist Hospital', 
#                   'speaker': 'Mr. Lee, Jung-Sang', 
#                   'type': 'Hospital', 
#                   'address': '374-75, Namsan-dong Geumjeong-gu', 
#                   'phone': '580-1251', 
#                   'emergency': '580-1212',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Inje Univ.Busan Paik Hospital', 
#                   'speaker': 'Mr. Cha, Ji-Hoon', 
#                   'type': 'Hospital', 
#                   'address': '633-165, Gaegeum 2-dong, Busanjin-gu', 
#                   'phone': '890-6220', 
#                   'emergency': '890-6221',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Maryknoll General Hospital', 
#                   'speaker': 'Mr. Park, Myung-hwan', 
#                   'type': 'Hospital', 
#                   'address': '12, Daecheong-dong, 4-ga, jung-gu', 
#                   'phone': '468-3858', 
#                   'emergency': '461-2300',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Kang Internal Medicine Clinic', 
#                   'speaker': 'Dr. Kang, Pil-joong', 
#                   'type': 'Clinic', 
#                   'address': '245-3, Bujeon 2-dong, Jin-Ku, Busan', 
#                   'phone': 'Unknown', 
#                   'emergency': '817-2334',
#                   'services': 'unknown'
#             },
#             {
#                   'name': 'Ye Dental Clinic', 
#                   'speaker': 'Dr. Kim, Byung-Soo', 
#                   'type': 'Clinic', 
#                   'address': '255-1, Dong-A Bldg., 6th Floor, Bujeon 2-dong, Jin-Ku, Busan', 
#                   'phone': 'Unknown', 
#                   'emergency': '808-2900',
#                   'services': 'unknown'
#             }
#         ]

#         conn.execute(
#             text("INSERT INTO Facilities(name, speaker, type, address, phone, emergency, services) VALUES (:name, :speaker, :company, :address, :phone, :emergency, :services)"), facilities_data)
        
#         conn.commit()
#         con.close()

