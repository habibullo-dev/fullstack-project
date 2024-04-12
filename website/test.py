import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine

engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")



# # Connect to the database
# conn = engine.connect()


# # Connect to the database
# conn = engine.connect()

# # Fetch data from the 'Doctors' table
# doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
# doctors = conn.execute(doctors_statement).fetchall()

# # Convert rows to a list of dictionaries
# doctors_list = [dict(row) for row in doctors]

# # Fetch data from the 'Facilities' table
# facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
# facilities = conn.execute(facilities_statement).fetchall()

#     # Convert rows to a list of dictionaries
# facilities_list = [dict(row) for row in facilities]

# conn.commit()
# # Close the database connection after retrieving the data
# conn.close()

# # Return the data as JSON
# print(jsonify({
#     'doctors': doctors_list,
#     'facilities': facilities_list
# }))

# Connect to the database
with engine.connect() as conn:
    # Fetch data from the 'Doctors' table
    doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
    Doctors = conn.execute(doctors_statement).fetchall()
    
    # print("Doctors:", doctors)
    # Convert rows to a list of dictionaries
    # doctors_list = [dict(row) for row in doctors]
    
    # Fetch data from the 'Facilities' table
    facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
    Facilities = conn.execute(facilities_statement).fetchall()
    
    # print("Facilities:", facilities)

    doctors_dict = [{'Name': doctor[0], 'Specialty': doctor[1], 'Hospital/Clinic': doctor[2], 'Address': doctor[3], 'Contact': doctor[4]} for doctor in Doctors]
    facilities_dict = [{'Name': facility[0], 'Contact Person': facility[1], 'Type': facility[2], 'Address': facility[3], 'Phone': facility[4], 'Fax': facility[5], 'Hours': facility[6]} for facility in Facilities]

    
    print("Doctors Dictionary:")
    for doctor in doctors_dict:
        print(doctor)

    print("\nFacilities Dictionary:")
    for facility in facilities_dict:
        print(facility)
    # # Convert rows to a list of dictionaries
    # facilities_list = [dict(row) for row in facilities]

    # print(doctors_list)
    # print(facilities_list)
# # Return the data as JSON
# return jsonify({
#     'doctors': doctors_list,
#     'facilities': facilities_list
# })