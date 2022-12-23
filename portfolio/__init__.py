import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '<please generate a new secret key>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@csmysql.cs.cf.ac.uk:3306/%s' % (os.environ["MYSQL_USERNAME"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_DB_NAME"])

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from portfolio.home.home import home_bp
from portfolio.modules.modules import modules_bp
from portfolio.auth.auth import bp_auth

app.register_blueprint(home_bp)
app.register_blueprint(modules_bp)
app.register_blueprint(bp_auth)
