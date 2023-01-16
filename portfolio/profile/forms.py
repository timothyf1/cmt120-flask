from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, RadioField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length

class Change_password(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, message="Passwords must be atleast 8 characters")])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="Passwords do not match")])
    submit = SubmitField('Change Password')

class Display_Settings(FlaskForm):
    dark = RadioField('Select dark mode preference', choices=[(0, 'System'), (1, 'Light'), (2, 'Dark')], default=0)
    accessibility = BooleanField('Accessibility mode')
    submit = SubmitField('Apply')
