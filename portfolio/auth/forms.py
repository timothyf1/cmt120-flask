from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class Signup_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter a username")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class Login_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter a username")])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password")])
    submit = SubmitField('Log In')

class New_password(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message="Please enter a password")])
    submit = SubmitField('Log In')
