from flask import render_template
from flask import Blueprint
from website import app, sql

views = Blueprint("views", __name__)
@app.route('/')
def home():
    return render_template("index.html")