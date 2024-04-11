from flask import Flask
from sqlalchemy import create_engine


app = Flask(__name__)

sql = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

<<<<<<< HEAD:__init__.py
# Define routes and database operations here

import Project.views
=======
from .views import views

app.register_blueprint(views, url_prefix="/")
>>>>>>> 0e0c0d0ec9218b58bdda96bc42a085d403e8c1e9:website/__init__.py
