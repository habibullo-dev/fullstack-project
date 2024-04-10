from flask import render_template
from sqlalchemy.sql import text
from website import app, sql

if __name__ == '__main__':
    app.run(debug=True)