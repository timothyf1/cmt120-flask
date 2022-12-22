from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '<please generate a new secret key>'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@csmysql.cs.cf.ac.uk:3306/%s' % (os.environ["mysql_username"], os.environ["mysql_password"], os.environ["mysql_db_name"])

db = SQLAlchemy(app)

from portfolio.routes import main, module

