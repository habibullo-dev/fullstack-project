from flask import Flask, flash, render_template, request, redirect, session, url_for, jsonify
import json
import hashlib
from sqlalchemy.sql import text
from website import app, engine


# route for the home page
@app.route('/')
def home():
    return render_template("index.html")

# route for the user page (in session or logged in)

@app.route('/users')
def user_page():
    if 'username' in session: # If username in sessions, if yes (user is logged in)
        return render_template('users.html', username=session['username'])
    else: 
        return render_template('users.html') # User not logged in, just pass users page
    
# contains the register page with a link to take user into login page
@app.route('/verify')
def verify_page():
    return render_template('verify.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     message = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         return
    
#  To Display Database Project with TABLES Doctors and Facilities
@app.route('/db_data')
def db_data():
    # Fetch data from the database
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

    # Render HTML template with fetched data
    return render_template('db_info.html', doctors=doctors, facilities=facilities)



# The function below, (hash_password) takes a password, encodes it into UTF-8
# hashes it using the SHA-256 algorithm from the hashlib library,
# then returns the hash as a hexadecimal string.

def hash_password(password):
    """Hash a password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

@app.route('/form', methods=['POST'])
def register():
    # Get user input from the form
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')

    # Check if any field is empty
    if not username or not password or not email:
        # Determine which fields are missing
        missing_fields = []
        if not username:
            missing_fields.append('Username')
        if not password:
            missing_fields.append('Password')
        if not email:
            missing_fields.append('Email')
        
        # Flash an error message with the list of missing fields
        flash(f"Missing fields: {', '.join(missing_fields)}", "error")

        # Redirect the user back to the form page
        return redirect(url_for('verify_page'))
        # return redirect(url_for('home'))
    
    # statement  below that calls hash_password(password) hashes the provided password
    # stores the result in the hashed_password variable for later use 
    #           (saving to a database or checking against stored passwords during login)

    # Hash the password using SHA-256
    hashed_password = hash_password(password)
    
    # To-Do: Save the user data to the database or perform any other actions
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO Users(username, password, email) VALUES (:username, :password, :email)"), 
            {"username": username, "password": hashed_password, "email": email}
        )

        # Flash a success message
        flash("Registration successful!", "success")

        # Redirect the user to the home page or another page
        return redirect(url_for('valid'))

# route for the login page
@app.route('/login')
def login():
    # params = {
    #     'user': request.form.get('username', ''),
    #     'pass': request.form.get('password', '')
    # }
    go_back = f'<p>Or <strong><a href="{url_for("home")}">click here</a></strong> to go back to home page</p>'
    return render_template('login.html', go_back=go_back)



# Route to take you to the mvp page
@app.route('/mvp')
def search_page():
    return render_template('mvp.html')

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
    doctors_dict = [
        {'Name': doctor[0], 
         'Expertise': doctor[1], 
         'Company': doctor[2], 
         'Address': doctor[3], 
         'Phone': doctor[4]} for doctor in doctors_data]
    
    facilities_dict = [
        {'Name': facility[0], 
         'Speaker': facility[1], 
         'Type': facility[2], 
         'Address': facility[3], 
         'Phone': facility[4], 
         'Emergency': facility[5], 
         'Services': facility[6]} for facility in facilities_data]
    
    # Combine the data into a dictionary
    data = {
        'Doctors': doctors_dict,
        'Facilities': facilities_dict
    }
    
    return data

# Load data once when the application starts
data = load_data()

# Function to filter data based on the search query or provided criteria
def filter_data(data, search_input, city, expert):
    # Convert inputs to lowercase for case-insensitive comparison
    search_input_lower = search_input.lower()
    city_lower = city.lower()
    expert_lower = expert.lower()

    # Combine all relevant fields into a single string and Join all values in the dictionary to create a combined string for each item
    # filter_data = [item for item in data if search_input in " ".join(str(value).lower() for value in item.values())]

    # Filter doctors based on search criteria
    filtered_doctors = [
        doctor for doctor in data['Doctors']
        if search_input_lower in doctor['Name'].lower() or
           search_input_lower in doctor['Expertise'].lower() or
           city_lower in doctor['Address'].lower() and
           expert_lower in doctor['Expertise'].lower()
    ]

    # Filter facilities based on search criteria
    filtered_facilities = [
        facility for facility in data['Facilities']
        if search_input_lower in facility['Name'].lower() or
           city_lower in facility['Address'].lower() and
           expert_lower in facility['Type'].lower()
    ]

    return {
        'Doctors': filtered_doctors,
        'Facilities': filtered_facilities
    }


# Define the '/search_input' endpoint
@app.route('/search_input', methods=['POST'])
def search_input():
    # Parse the JSON request data
    data_request = request.json

    # Get the search criteria from the request
    search_input = ''
    type_input = data_request.get('type', '')
    city_input = data_request.get('city', '')
    expert_input = data_request.get('expert', '')

    # Validate inputs
    if not type_input or not city_input or not expert_input:
        return jsonify({'error': 'Invalid input'}), 400

    # Filter the data based on the search criteria
    filtered_results = filter_data(data, search_input, city_input, expert_input)

    # Return the filtered results as JSON
    return jsonify(filtered_results)


# About page route
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
