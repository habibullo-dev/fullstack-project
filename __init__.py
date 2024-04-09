from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

sql = create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

import Project.views