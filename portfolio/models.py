from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from portfolio import db, app

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    is_active = db.Column(db.Boolean, default=True)
    dark_mode = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"Module('{self.id}', '{self.name}', '{self.description}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Text)
    content = db.Column(db.Text)
