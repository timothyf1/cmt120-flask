from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
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

class Change_password(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, message="Passwords must be atleast 8 characters")])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="Passwords do not match")])
    submit = SubmitField('Change Password')

class Dark_mode(FlaskForm):
    submit = SubmitField('Apply')
    pref = RadioField('Select dark mode preference', choices=[(0, 'System'), (1, 'Light'), (2, 'Dark')], default=0)
