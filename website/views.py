import json
import hashlib
import datetime
from flask import Flask, flash, render_template, request, redirect, session, url_for, jsonify
from sqlalchemy.sql import text
from website import app, engine


# route for the home page
@app.route('/')
def home():
    return render_template("index.html")

#route for admin page
@app.route('/admin') 
def admin(): 
    #Fetch user data from the database
    with engine.connect() as conn:
        users = conn.execute(text("SELECT username, password, email, first_name, last_name, birth_date, gender, phone, allergy, `condition`, join_date FROM Users")).fetchall()
        # Render HTML template with fetched data
    return render_template('admin.html', users=users)

#  To Display Database Project with TABLES Doctors and Facilities
@app.route('/db_data')
def db_data():
    # Fetch data from the database
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone, ratings, availability FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()
    # Render HTML template with fetched data
    return render_template('db_info.html', doctors=doctors, facilities=facilities)


# The function below, (hash_password) takes a password, encodes it into UTF-8
# hashes it using the SHA-256 algorithm from the hashlib library,
# then returns the hash as a hexadecimal string.

# Hash password for security purposes
def hash_password(password):
    """Hash a password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password


def verify_password(input_password, hashed_password):
    """Verify if the input password matches the stored hashed password."""
    # Hash the input password provided during login
    hashed_input_password = hashlib.sha256(input_password.encode('utf-8')).hexdigest()

    # For debugging, print the hashed passwords
    # print("Input Password Hash:", hashed_input_password)
    # print("Stored Password Hash:", hashed_password)

    return hashed_input_password == hashed_password


# Add user to the database
def add_user(username, hashed_password, email, first_name, last_name, birth_date, gender, phone, allergy, condition):
    # Get the current date and time
    join_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Start a new connection with database
    with engine.begin() as conn:
        # Execute the INSERT statement using parameterized query
        res = conn.execute(
        text("INSERT INTO Users(username, password, email, first_name, last_name, birth_date, gender, phone, allergy, `condition`, join_date) VALUES (:username, :password, :email, :first_name, :last_name, :birth_date, :gender, :phone, :allergy, :condition, :join_date)"),
        {"username": username, "password": hashed_password, "email": email, "first_name": first_name, "last_name": last_name, "birth_date": birth_date, "gender": gender, "phone": phone, "allergy": allergy, "condition": condition, "join_date": join_date}
    )
        # Check if the data is inserted
        # If the 'rowcount' is greater than 0, we have a successful insertion of the data from register page
        return res.rowcount > 0

# Retrieve user info from the database
def get_user(username):
    with engine.connect() as conn:
        res = conn.execute(
            text("SELECT * FROM Users WHERE username = :username"),
            {"username": username}
        )
        return res.fetchone() # fetch one row from db

# route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        user = get_user(username)
        # breakpoint() #stop the code (debugger)

        if user:
            stored_password = user[2] #user['password'] // coming in as tuple
            if verify_password(password, stored_password):
                session['username'] = username
                # app.logger.info(f"User '{username}' logged in successfully.")
                flash('Login Successful!', category='success')
                return redirect(url_for('user_page')) # Pass email to user_page route
            else:
                # app.logger.warning(f"Failed login attempt for user '{username}' - Incorrect password {password}.")
                flash('Incorrect username or password. Please try again!', category='error')
        else:
            # app.logger.warning(f"Failed login attempt - User '{username}' does not exist and Password does not exist {password}.")
            flash('User does not exist. Please go to the registration page to create an account.', category='error')

    return render_template('verify.html')


# contains the register page with a link to take user into login page
@app.route('/register', methods=['GET', 'POST'])
def register():

    # Handle registration
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        birth_date = request.form.get('birth_date')
        gender = request.form.get('gender')
        allergy = request.form.get('allergy')
        condition = request.form.get('condition')

        # Check if email already exists
        registered_email = get_user(email)
        if registered_email:
            flash('Email is already registered. Please use a different email address.', category='error')
        
        #Validate form  inputs
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 5:
            flash('Username must be at least 5 characters long.', category='error')
        elif len(first_name) < 2:
            flash('First name must be at least 2 characters long.', category='error')
        elif len(last_name) < 2:
            flash('Last_name must be at least 2 characters long.', category='error')
        elif len(password) < 5:
            flash('Password must be greater than 5 characters long.', category='error')
        else:
            # Hash the password using SHA-256
            hashed_password = hash_password(password)

             # Add the new user to the database
            result = add_user(username, hashed_password, email, first_name, last_name, birth_date, gender, phone, allergy, condition)
            if result:
                flash('Registration is successful. Account is created!', category='success')
                return redirect(url_for('login')) # This will redirect the user to the booking page after registration
            else:
                flash('Registration failed. Please continue trying.', category='error')
            
    return render_template('verify.html')

# route for the user page (accessible only if user is logged in)
@app.route('/users')
def user_page():
    # Render the user page. 
    if 'username' in session: # If username in sessions, (user is logged in) pass to user page
        return render_template('users.html', username=session['username'])
    else: 
         return redirect(url_for('home'))  # User not logged in, redirect to home page


# pops up the 'username' session variable. Therefore, the ' /' URL displays the start page again.
# route for the logout page
@app.route('/logout')
def logout():
    # Implement a simple login check - We do not want to access the logout route or page if user is not login
    if 'username' not in session:
        flash('You must be logged in to access this page (logout).', category='error')
        return redirect(url_for('login')) # Assuming user not logged in, We can redirect user back to login page

    session.clear()  # Clear the session data
    session.pop('username', None) # remove the username from the session if it is there
    flash('You have been logged out.', category='success') # Flash a message for logging out
    return render_template('logout.html')

# New feature for the project (Chat Room)
# Routes
@app.route('/chat')
def chat():
    if 'username' not in session:
        flash("You must be logged in to access this page.", category='error')
        return redirect(url_for('login')) # Assuming the user is not logged in
    else:
        user = session['username']
    
    return render_template('chat.html', user=user)


@app.route('/send_message', methods=['POST'])
def send_message():
        
    if 'username' in session:
        user = session['username']

    data = request.get_json()
    message = data.get('text', '')  # Adjusted to match JSON structure

    if not message:
        return jsonify({'message': 'Message is required.'}), 401

    # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time = datetime.now()

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO Messages (user, message, time) VALUES (:user, :message, :time)"),
            {"user": user, "message": message, "time": time}
        )

    print(f"New message from {user}: {message}")

    return jsonify({'message': 'Message sent successfully'}), 200


@app.route('/all_messages')
def all_messages():
    if 'username' not in session:
        return jsonify({'message': 'User is not logged in'}), 401

    messages = []
    with engine.begin() as conn:
        res = conn.execute(text("SELECT user, message, time FROM Messages"))
    messages = get_messages_from_db()

    return jsonify(messages), 200


# def get_messages_from_db():
#     messages = []
#     with engine.begin() as conn:
#         res = conn.execute(text("SELECT user, message_text, date_time FROM Messages"))
#         for row in res:
#             message = {
#                 'user': row.user,
#                 'text': row.message_text,
#                 'time': row.date_time.strftime("%Y-%m-%d %H:%M:%S")
#             }
#             messages.append(message)

#     return messages


# End feature for the Project (Chat Room)


# Route to take you to the mvp page
@app.route('/mvp')
def search_page():
    return render_template('mvp.html')

# Load data from the database and convert it to JSON format
def load_data():
    conn = engine.connect()
    
    # Fetch data from the 'Doctors' table
    doctors_statement = text("SELECT name, expertise, company, address, phone, ratings FROM Doctors")
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
         'Phone': doctor[4], 
         'Ratings': doctor[5]} for doctor in doctors_data]
    
    facilities_dict = [
        {'Name': facility[0], 
         'Speaker': facility[1], 
         'Type': facility[2], 
         'Address': facility[3], 
         'Phone': facility[4], 
         'Emergency': facility[5], 
         'Services': facility[6]} for facility in facilities_data]
    
    # Combine the data into a dictionary
    db_data = {
        'Doctors': doctors_dict,
        'Facilities': facilities_dict
    }
    
    return db_data

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
           search_input_lower in doctor['Phone'].lower() or
           search_input_lower in doctor['Ratings'].lower() or
           city_lower in doctor['Address'].lower() and
           expert_lower in doctor['Expertise'].lower()
    ]

    # Filter facilities based on search criteria
    filtered_facilities = [
        facility for facility in data['Facilities']
        if search_input_lower in facility['Name'].lower() or
           search_input_lower in facility['speaker'].lower() or
           search_input_lower in facility['phone'].lower() or
           search_input_lower in facility['emergency'].lower() or
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
    city_input = data_request.get('city', '')
    expert_input = data_request.get('expert', '')

    # Validate inputs
    if not city_input or not expert_input:
        return jsonify({'error': 'Invalid input'}), 400

    # Filter the data based on the search criteria
    filtered_results = filter_data(data, search_input, city_input, expert_input)

    # Return the filtered results as JSON
    return jsonify(filtered_results)
    # This turns the JSON output into a Response object with the application/json mimetype.


# About page route
@app.route('/about')
def about_us():
    intro = """
We are dedicated to providing reliable and comprehensive information about English-speaking medical professionals and facilities in South Korea. 
Our platform is designed to make healthcare more accessible and less stressful for foreigners visiting or living in South Korea. 
Whether you are a tourist, student, or expat, finding quality healthcare in a new country can be challenging, especially if there is a language barrier. 
We are here to help bridge that gap.
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
