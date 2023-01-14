from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length

class Edit_Experience(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    employer = StringField('Employer', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    start = DateField('Start Date', validators=[DataRequired()])
    end = DateField('End Date')
    current = BooleanField('Current Job')
    description = StringField('Description')
    submit = SubmitField('Add Experience')

class Delete_Experience(FlaskForm):
    confirm = BooleanField('The action of deleting experience is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
