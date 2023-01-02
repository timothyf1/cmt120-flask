from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class New_Module(FlaskForm):
    name = StringField('Module Name', validators=[DataRequired()])
    code = StringField('Module Code', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Module')

class Edit_Module(FlaskForm):
    name = StringField('Module Name', validators=[DataRequired()])
    code = StringField('Module Code', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Apply Changes')

class Delete_Module(FlaskForm):
    confirm = BooleanField('The action of deleting a module is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
