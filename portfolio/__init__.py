import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_breadcrumbs import Breadcrumbs, default_breadcrumb_root

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['FILE_UPLOAD'] = os.path.join(os.path.dirname(__file__), "static", "upload")
app.config['ALLOWED_TAGS'] = ['a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li', 'code', 'strong', 'blockquote', 'em', 'img', 'pre']
app.config['ALLOWED_ATTRIBUTES'] = {'a': ['href', 'title'],
                                    'abbr': ['title'],
                                    'acronym': ['title'],
                                    'img': ['alt', 'src']}
app.config['ALLOWED_IMG_EXTENSIONS'] = ('.png', '.jpg', '.jpeg', '.gif')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

Breadcrumbs(app=app)

from . import errors
from .home.home import bp_home
from .education.education import bp_education
from .auth.auth import bp_auth
from .profile.profile import bp_profile

app.register_blueprint(bp_home)
app.register_blueprint(bp_education, url_prefix='/education')
app.register_blueprint(bp_auth, url_prefix='/auth')
app.register_blueprint(bp_profile, url_prefix='/profile')

# https://github.com/inveniosoftware/flask-breadcrumbs/issues/33#issuecomment-244692682
default_breadcrumb_root(bp_home, '.')

from .models import User

@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    return User.query.get(int(user_id))
