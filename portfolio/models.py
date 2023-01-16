from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from portfolio import db, app

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    default_password = db.Column(db.Boolean, default=False)

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # User Settings
    dark_mode = db.Column(db.Integer, default=0)
    accessibility = db.Column(db.Boolean, default=0)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.is_active}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    modules = db.relationship('Module', order_by="Module.year.desc()", back_populates='course')

    def __repr__(self):
        return f"Course('{self.id}', '{self.name}', '{self.description}')"

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.Text)

    course = db.relationship('Course', back_populates='modules')
    topics = db.relationship('Topic', order_by="Topic.date.desc()", back_populates='module')

    def __repr__(self):
        return f"Module('{self.id}', '{self.name}', '{self.description}')"

tag_assignment = db.Table(
    "tag_assignment",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("topic_id", db.ForeignKey("topic.id")),
    db.Column("tag_id", db.ForeignKey("tag.id")),
)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100), unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    draft = db.Column(db.Boolean, default=False)

    module = db.relationship('Module', back_populates='topics')
    tags = db.relationship('Tag', secondary=tag_assignment, order_by="Tag.name", back_populates='topics')

    def __repr__(self):
        return f"topic('{self.id}', '{self.title}')"

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    topics = db.relationship('Topic', secondary=tag_assignment, back_populates='tags')

class ImageUpload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False, unique=True)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    employer = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime)
    current = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)
