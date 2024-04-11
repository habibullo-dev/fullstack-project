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

@app.route('/mvp')
def mvp_page():
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

    return render_template('mvp.html', doctors=doctors, facilities=facilities)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        user = request.form.get("username", '')
        password = request.form.get("password", '')
        email = request.form.get("email", '')
    
    # add some extra logic to validate the input?
    # do not forget to save the data to the database

    # print the received data
    print(f"Received registration details: Username: {user}, Password: {password}, Email: {email}")
    
     # After processing the registration, you might want to redirect the user to home page
    return redirect(url_for('home'))
    # return render_template("index.html")



#  To Display Database Project with TABLES Doctors and Facilities
@app.route('/db_data')
def db_data():
    # Fetch data from the database
    with engine.connect() as conn:
        doctors = conn.execute(text("SELECT name, expertise, company, address, phone FROM Doctors")).fetchall()
        facilities = conn.execute(text("SELECT name, speaker, type, address, phone, emergency, services FROM Facilities")).fetchall()

    # Render HTML template with fetched data
    return render_template('db_info.html', doctors=doctors, facilities=facilities)


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

