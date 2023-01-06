from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length

class New_Module(FlaskForm):
    name = StringField('Module Name', validators=[DataRequired(), Length(max=100)])
    code = StringField('Module Code', validators=[DataRequired(), Length(max=20)])
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Module')

class Edit_Module(FlaskForm):
    name = StringField('Module Name', validators=[DataRequired(), Length(max=100)])
    code = StringField('Module Code', validators=[DataRequired(), Length(max=20)])
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Apply Changes')

class Delete_Module(FlaskForm):
    confirm = BooleanField('The action of deleting a module is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
