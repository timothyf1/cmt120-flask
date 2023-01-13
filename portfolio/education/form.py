from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Regexp

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

class New_Topic(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags', validators=[Regexp('^([0-9a-zA-Z-]+ ?)*$', message='Tags can only contain letters, numbers or - and must be sepreated by a space.')])
    submit = SubmitField('Add Topic')

class Edit_Topic(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags', validators=[Regexp('^([0-9a-zA-Z-]+ ?)*$', message='Tags can only contain letters, numbers or - and must be sepreated by a space.')])
    submit = SubmitField('Edit Topic')

class Delete_Topic(FlaskForm):
    confirm = BooleanField('The action of deleting a topic is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')

class Delete_Tag(FlaskForm):
    confirm = BooleanField('The action of deleting a tag is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')

class Image_Upload(FlaskForm):
    file_up = FileField('File')
    submit = SubmitField('Upload')
