from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine


app = Flask(__name__)

engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")
# engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")



import website.views



    