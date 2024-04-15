from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import hashlib
from sqlalchemy.sql import text
from website import app, engine



@app.route('/')
def home():
    return render_template("index.html")

# contains the register page with a link to take user into login page
@app.route('/register')
def verify_page():
    return render_template("verify.html")



# The function below, (hash_password) takes a password, encodes it into UTF-8
# hashes it using the SHA-256 algorithm from the hashlib library,
# then returns the hash as a hexadecimal string.

def hash_password(password):
    """Hash a password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

@app.route('/form', methods=['POST'])
def register():
    title = "Thank you!"
    message = f'<p>Or <strong><a href="{url_for("home")}">click here</a></strong> to go back to home page</p>'
    
    # Get user input from the form
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')

    # Check if any field is empty
    if not username or not password or not email:
        return redirect(url_for('home'))
    
    # statement  below that calls hash_password(password) hashes the provided password
    # stores the result in the hashed_password variable for later use 
    #           (saving to a database or checking against stored passwords during login)

    # Hash the password using SHA-256
    hashed_password = hash_password(password)
    
    # To-Do: Save the user data to the database or perform any other actions
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO Users(username, password, email) VALUES (:username, :password, :email)")
        )

    return render_template("form.html", title=title, message=message)

# add some extra logic to validate the input?
#     do not forget to save the data to the database


# route for the login page
@app.route('/login')
def login():
    # params = {
    #     'user': request.form.get('username', ''),
    #     'pass': request.form.get('password', '')
    # }
    go_back = f'<p>Or <strong><a href="{url_for("home")}">click here</a></strong> to go back to home page</p>'
    return render_template('login.html', go_back=go_back)


@app.route('/mvp')
def search_page():
    return render_template('mvp.html')

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


# Route to take you to the search page 
@app.route('/search')
def show_data():
    title = "Search Input"
    return render_template('search.html', title=title)


# Load data from the database and convert it to JSON format
def load_data():
    conn = engine.connect()
    
    # Fetch data from the 'Doctors' table
    doctors_statement = text("SELECT name, expertise, company, address, phone FROM Doctors")
    doctors_data = conn.execute(doctors_statement).fetchall()

    # Fetch data from the 'Facilities' table
    facilities_statement = text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")
    facilities_data = conn.execute(facilities_statement).fetchall()
    
    # Close the database connection
    conn.close()
    
    # Convert data to dictionaries
    doctors_dict = [{'Name': doctor[0], 'Expertise': doctor[1], 'Company': doctor[2], 'Address': doctor[3], 'Phone': doctor[4]} for doctor in doctors_data]
    facilities_dict = [{'Name': facility[0], 'Speaker': facility[1], 'Type': facility[2], 'Address': facility[3], 'Phone': facility[4], 'Emergency': facility[5], 'Services': facility[6]} for facility in facilities_data]
    
    # Combine the data into a dictionary
    data = {
        'Doctors': doctors_dict,
        'Facilities': facilities_dict
    }
    
    return data

# Load data once when the application starts
data = load_data()

# Define a search endpoint
@app.route('/search_input', methods=['POST'])
def search_input():
    search_input = request.json.get('search_input')
    
    if not search_input:
        return jsonify({'error': 'Invalid input'}), 400
    
    # Filter data based on the search input
    filtered_doctors = [doctor for doctor in data['Doctors'] if search_input.lower() in doctor['Name'].lower() or search_input.lower() in doctor['Expertise'].lower()]
    filtered_facilities = [facility for facility in data['Facilities'] if search_input.lower() in facility['Name'].lower() or search_input.lower() in facility['Type'].lower()]
    
    # Return filtered results
    return jsonify({
        'Doctors': filtered_doctors,
        'Facilities': filtered_facilities
    })



#  To Display Database Project with TABLES Doctors and Facilities
@app.route('/db_data')
def db_data():
    # Fetch data from the database
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

    # Render HTML template with fetched data
    return render_template('db_info.html', doctors=doctors, facilities=facilities)


@app.route('/about')
def about_us():
    intro = """
We are dedicated to providing reliable and comprehensive information about English-speaking medical professionals and facilities in South Korea. 
Our platform is designed to make healthcare more accessible and less stressful for foreigners visiting or living in South Korea. 
Whether you are a tourist, student, or expat, finding quality healthcare in a new country can be challenging, especially if there is a language barrier. 
We’re here to help bridge that gap.
"""
    mission = """
Our mission is to connect non-Korean speakers with medical services that can cater to their language and cultural needs.
We strive to make healthcare in South Korea easier to navigate, ensuring that everyone receives the medical attention they need without worrying about language barriers.
"""
    commitment = """
We are committed to providing a trustworthy and supportive platform for anyone seeking healthcare services in South Korea. 
Your well-being is our top priority, and we aim to make your experience in South Korea as comfortable and worry-free as possible.
"""
    return render_template('about.html', mission=mission, intro=intro, commit=commitment)



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
