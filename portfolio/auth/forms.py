from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class Login_form(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(message="Please enter a username")]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter a password")]
    )
    submit = SubmitField('Log In')

class New_password(FlaskForm):
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Please enter a password"),
            Length(min=8, message="Passwords must be atleast 8 characters")
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message="Please enter a password"),
            EqualTo('password', message="Passwords do not match")
        ]
    )
    submit = SubmitField('Log In')
