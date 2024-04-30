import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import json

engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")

# Connect to the database
conn = engine.connect()


# Convert dict data to a file using json dump
def save_data():
    conn = engine.connect()

    # Fetch data from the 'Doctors' table
    doctors_statement = text("SELECT name, expertise, company, address, phone, ratings FROM Doctors")
    doctor_data = conn.execute(doctors_statement).fetchall()


    # Fetch data from the 'Facilities' table
    facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
    facility_data = conn.execute(facilities_statement).fetchall()

    #close connection
    conn.close()

     # Convert data to dictionaries
    doctors_dict = [
        {'Name': doctor[0], 
         'Expertise': doctor[1], 
         'Company': doctor[2], 
         'Address': doctor[3], 
         'Phone': doctor[4], 
         'Ratings': doctor[5]} for doctor in doctor_data]

    facilities_dict = [
        {'Name': facility[0], 
         'Speaker': facility[1], 
         'Type': facility[2], 
         'Address': facility[3], 
         'Phone': facility[4], 
         'Emergency': facility[5], 
         'Services': facility[6]} for facility in facility_data]

    return doctors_dict, facilities_dict

def data_to_json():
    doctors_dict, facilities_dict = save_data() # save_data() returns dictionaries

    # Save doctor data to JSON
    with open('doctors_data', 'w') as doc_file:
        json.dump(doctors_dict, doc_file, indent=4)
    
    # Save Facility data to JSON
    with open('facilities_data', 'w') as fac_file:
        json.dump(facilities_dict, fac_file, indent=4)

    # Print doctor data
    print("Doctor Data:")
    with open('doctors_data', 'r') as doc_file:
        print(doc_file.read())
    
    # Print facility data
    print("Facility Data:")
    with open('facilities_data', 'r') as fac_file:
        print(fac_file.read())
    
# Call the function to save the data and print the files
data_to_json()


# # Convert the dictionary to JSON format
# json_data = json.dumps(data, indent=4)

# # Print the JSON data
# print(json_data)