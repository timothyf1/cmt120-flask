from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, TextAreaField
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

class New_post(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')

class Edit_post(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Edit Post')

class Delete_Post(FlaskForm):
    confirm = BooleanField('The action of deleting a post is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')
