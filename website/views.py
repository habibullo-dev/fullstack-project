from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.sql import text
from website import app, engine


@app.route('/')
def home():
    return render_template("index.html")

# contains the register page with a link to take user into login page
@app.route('/verify')
def verify_page():
    return render_template("verify.html")

# route for the login page
@app.route('/login')
def login():
    # params = {
    #     'user': request.form.get('username', ''),
    #     'pass': request.form.get('password', '')
    # }
    return render_template('login.html')


# we can use this route to connect to the mvp page and use the search box to 
# @app.route('/mvp')
# def search_page():
#     with engine.connect() as conn:
#         doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
#         facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM facilities")).fetchall()
#     return render_template("mvp.html", doctors=doctors, facilities=facilities)

# @app.route('/mvp')
# def mvp_page():
#     with engine.connect() as conn:
#         doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
#         facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

#         for doctor in doctors:
#             print(f"Doctor Name: {doctor.name}, Expertise: {doctor.expertise}, Company: {doctor.company}, Address: {doctor.address}, Phone: {doctor.phone}")
    
#         for facility in facilities:
#             print(f"Facility Name: {facility.name}, Speaker: {facility.speaker}, Type: {facility.type}, Address: {facility.address}, Phone: {facility.phone}, Emergency: {facility.emergency}, Services: {facility.services}")

#     return render_template('mvp.html', doctors=doctors, facilities=facilities)

# # create search function and route
# @app.route('/search_data')
# def get_search_data():

#     #Retrieve the search input from the query string
#     search_input = request.args.get('input', '')
#     # Connect to the database
#     conn = engine.connect()

#     # Fetch data from the 'Doctors' table
#     doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
#     Doctors = conn.execute(doctors_statement).fetchall()

#     # Fetch data from the 'Facilities' table
#     facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
#     Facilities = conn.execute(facilities_statement).fetchall()

#      # Convert rows(tuples) to a list of dictionaries
#     doctors_dict = [{'Name': doctor[0], 'Specialty': doctor[1], 'Hospital/Clinic': doctor[2], 'Address': doctor[3], 'Contact': doctor[4]} for doctor in Doctors]
#     facilities_dict = [{'Name': facility[0], 'Contact Person': facility[1], 'Type': facility[2], 'Address': facility[3], 'Phone': facility[4], 'Fax': facility[5], 'Hours': facility[6]} for facility in Facilities]

#     # Close the database connection after retrieving the data
#     conn.close()

#     print("Doctors Dictionary:")
#     for doctor in doctors_dict:
#         print(doctor)

#     print("\nFacilities Dictionary:")
#     for facility in facilities_dict:
#         print(facility)
    
#      # Return the data as JSON
#     return jsonify({
#         'doctors': doctors_dict,
#         'facilities': facilities_dict
#     })
    
#     return render_template('search.html', doctors=doctors_dict, facilities=facilities_dict, input=search_input)
@app.route('/search_data')
def get_search_data():
    # Retrieve the search input from the query string
    search_input = request.args.get('input', '').lower()
    
    # Connect to the database
    conn = engine.connect()
    
    # Query to fetch data from Doctors table based on search input
    doctors_query = text(
        "SELECT name, expertise, company, address, phone FROM Doctors WHERE LOWER(name) LIKE :search_input"
    )
    
    # Query to fetch data from Facilities table based on search input
    facilities_query = text(
        "SELECT name, speaker, type, address, phone, emergency, services FROM Facilities WHERE LOWER(name) LIKE :search_input"
    )
    
    # Execute queries and fetch results
    doctors_results = conn.execute(doctors_query, {'search_input': f"%{search_input}%"}).fetchall()
    facilities_results = conn.execute(facilities_query, {'search_input': f"%{search_input}%"}).fetchall()
    
    # Convert rows to dictionaries
    doctors_dict = [
        {'Name': doc[0], 'Specialty': doc[1], 'Hospital/Clinic': doc[2], 'Address': doc[3], 'Contact': doc[4]}
        for doc in doctors_results
    ]
    facilities_dict = [
        {'Name': fac[0], 'Contact Person': fac[1], 'Type': fac[2], 'Address': fac[3], 'Phone': fac[4], 'Emergency': fac[5]}
        for fac in facilities_results
    ]
    
    # Close the database connection
    conn.close()
    
    # Render the search.html template with the search results and input
    return render_template(
        'search.html',
        doctors=doctors_dict,
        facilities=facilities_dict,
        input=search_input
    )

    # # Define SQL statements to retrieve data from 'Doctors' and 'Facilities' tables
    # doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
    # facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
    
    # # Execute the data retrieval statements for 'Doctors' and 'Facilities'
    # doctors = conn.execute(doctors_statement).fetchall()
    # facilities = conn.execute(facilities_statement).fetchall()
    # print("Doctors:", doctors)
    # print("Facilities:", facilities)

    # # Close the database connection after retrieving the data
    # conn.close()

    # # Convert the results into lists of dictionaries
    # # doctors_list = [dict(row) for row in doctors]
    # # facilities_list = [dict(row) for row in facilities]


    # doctors_list = [dict(row) for row in doctors]
    # print("Doctor list:", doctors_list)
    # print("Facilities List:", facilities_list)

    # # Convert the 'doctor s' result set into a list of dictionaries
    # # doctors_list = []
    # # for row in doctors:
    # #     row_dict = {} # Create a dictionary for each row, using the column names as keys
    # #     for column in row.keys():
    # #         row_dict[column] = row[column]
    # #     doctors_list.append(row_dict)  # Append the dictionary to the list

    # # # Convert the 'facilities' result set into a list of dictionaries
    # # facilities_list = []
    # # for row in facilities:
    # #     row_dict = {} # Create a dictionary for each row, using the column names as keys
    # #     for column in row.keys():
    # #         row_dict[column] = row[column]
    # #     facilities_list.append(row_dict)  # Append the dictionary to the list

    # # Combine the data from 'doctors' and 'facilities' into a single dictionary
    # data = {
    #     "doctors": doctors_list,
    #     "facilities": facilities_list
    # }
        
    # # Return the combined data as a JSON response using Flask's `jsonify()` function.
    # return jsonify(data)



#  To Display Database Project with TABLES Doctors and Facilities
@app.route('/db_data')
def db_data():
    # Fetch data from the database
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

    # Render HTML template with fetched data
    return render_template('db_info.html', doctors=doctors, facilities=facilities)


# @app.route('/register', methods=['POST'])
# def register():
#     # Get user input from the form
#     username = request.form.get('username')
#     password = request.form.get('password')
#     email = request.form.get('email')

#     if not username or not password or not email:
#         return render_template("verify.html", error="All fields are required.")

# add some extra logic to validate the input?
    # do not forget to save the data to the database


# Create custom error pages 404 and 500

@app.errorhandler(404) # Invalid Url
def page_not_found(error):
    return render_template('message.html', title="404 - Page Not Found", message="...Oops Error! Sorry, the page you are looking for could not be found."), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('message.html', title="500 - Internal Server Error", message="Some Internal Error occurred..."), 500

@app.route('/simulate500')
def simulate_error():
    return render_template('message.html',  title="500 - Internal Server Error", message="Oops, some error occurred..."), 500

    
if __name__ == '__main__':
    app.run(debug=True)
