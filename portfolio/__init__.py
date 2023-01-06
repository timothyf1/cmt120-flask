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
from portfolio.post.posts import bp_posts
from portfolio.auth.auth import bp_auth
from portfolio.profile.profile import bp_profile

app.register_blueprint(bp_home)
app.register_blueprint(bp_education, url_prefix='/education')
app.register_blueprint(bp_modules, url_prefix='/module')
app.register_blueprint(bp_posts, url_prefix='/post')
app.register_blueprint(bp_auth, url_prefix='/auth')
app.register_blueprint(bp_profile, url_prefix='/profile')

from .models import User

@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    return User.query.get(int(user_id))
