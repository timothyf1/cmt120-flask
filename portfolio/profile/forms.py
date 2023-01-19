from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, RadioField, BooleanField, StringField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from ..models import User

def check_username(form, field):
    if form.username.data != form.current_username.data:
        user_qur = User.query.filter_by(username=form.username.data).first()
        if user_qur is not None:
            raise ValidationError('This username has already been used, please enter a different username')

class Change_password(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, message="Passwords must be atleast 8 characters")])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="Passwords do not match")])
    submit = SubmitField('Change Password')

class Change_Username(FlaskForm):
    current_username = HiddenField()
    username = StringField('Username', validators=[DataRequired(), Length(max=20), check_username])
    password = PasswordField('Please enter your password to confirm', validators=[DataRequired()])
    submit = SubmitField('Change Username')

class Display_Settings(FlaskForm):
    dark = RadioField('Select dark mode preference', choices=[(0, 'System'), (1, 'Light'), (2, 'Dark')], default=0)
    accessibility = BooleanField('Accessibility mode')
    submit = SubmitField('Apply')
