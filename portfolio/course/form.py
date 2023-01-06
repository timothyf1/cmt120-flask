from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length

class New_Course(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(max=50)])
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Course')

class Edit_Course(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(max=50)])
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Apply Changes')

class Delete_Course(FlaskForm):
    confirm = BooleanField('The action of deleting a course is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
