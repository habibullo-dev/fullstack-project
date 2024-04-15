import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import json

engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")

# Connect to the database
conn = engine.connect()


# Fetch data from the 'Doctors' table
doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
Doctors = conn.execute(doctors_statement).fetchall()

# Fetch data from the 'Facilities' table
facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
Facilities = conn.execute(facilities_statement).fetchall()

# Convert tuples to dictionaries for Doctors
doctors_dict = [{'Name': doctor[0], 'Specialty': doctor[1], 'Hospital/Clinic': doctor[2], 'Address': doctor[3], 'Contact': doctor[4]} for doctor in Doctors]

# Convert tuples to dictionaries for Facilities
facilities_dict = [{'Name': facility[0], 'Contact Person': facility[1], 'Type': facility[2], 'Address': facility[3], 'Phone': facility[4], 'Fax': facility[5], 'Hours': facility[6]} for facility in Facilities]


# Commit the transaction if necessary (only if you made changes, such as insertions)
conn.commit()

# Close the database connection after retrieving the data
conn.close()

# Create a dictionary with the data
data = {
    'doctors': doctors_dict,
    'facilities': facilities_dict
}

# Convert the dictionary to JSON format
json_data = json.dumps(data, indent=4)

# Print the JSON data
print(json_data)