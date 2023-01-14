from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, ValidationError

def check_start_before_end(form, field):
    if not form.current.data:
        if form.end.data < form.start.data:
            raise ValidationError('End date must be after start date')

class Edit_Experience(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired(), Length(max=50)])
    employer = StringField('Employer', validators=[DataRequired(), Length(max=50)])
    location = StringField('Location', validators=[DataRequired(), Length(max=50)])
    start = DateField('Start Date', validators=[DataRequired()])
    end = DateField('End Date', validators=[check_start_before_end])
    current = BooleanField('Current Job')
    description = StringField('Description')
    submit = SubmitField('Add Experience')

class Delete_Experience(FlaskForm):
    confirm = BooleanField('The action of deleting experience is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
