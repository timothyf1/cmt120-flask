from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '<please generate a new secret key>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@csmysql.cs.cf.ac.uk:3306/%s' % (os.environ["MYSQL_USERNAME"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_DB_NAME"])
db = SQLAlchemy(app)

from portfolio.home.home import home_bp
from portfolio.modules.modules import modules_bp

app.register_blueprint(home_bp)
app.register_blueprint(modules_bp)
