from flask import render_template
from sqlalchemy.sql import text
from Project import app, sql


@app.route('/')
def home_page():
    return render_template("index.html")