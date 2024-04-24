from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.secret_key = 'my-secret-key430' 
engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")
# engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")



import website.views



    