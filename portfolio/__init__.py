import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '<please generate a new secret key>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (os.environ["MYSQL_USERNAME"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_HOST"], os.environ["MYSQL_DB_NAME"])

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from portfolio.home.home import bp_home
from portfolio.course.course import bp_education
from portfolio.modules.modules import bp_modules
from portfolio.auth.auth import bp_auth

app.register_blueprint(bp_home)
app.register_blueprint(bp_education)
app.register_blueprint(bp_modules)
app.register_blueprint(bp_auth, url_prefix='/auth')
