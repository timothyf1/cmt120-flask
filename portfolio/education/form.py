from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, TextAreaField, FileField, HiddenField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError

from ..models import Course, Module, Topic

def check_course_name(form, field):
    if form.name.data != form.current_name.data:
        cou_query = Course.query.filter_by(name=form.name.data).first()
        if cou_query is not None:
            raise ValidationError('This course name has already been used, please enter a different name')

def check_module_code(form, field):
    if form.code.data != form.current_code.data:
        mod_query = Module.query.filter_by(code=form.code.data).first()
        if mod_query is not None:
            raise ValidationError('This module code has been used, please enter a different code')

def check_topic(form, field):
    if form.title.data != form.current_title.data:
        top_query = Topic.query.filter_by(title=form.title.data).first()
        if top_query is not None:
            raise ValidationError('This title has been used, please enter a different title')

class Edit_Course(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100), check_course_name])
    current_name = HiddenField()
    location = StringField('Location', validators=[DataRequired(), Length(max=50)])
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Save Course')

class Edit_Module(FlaskForm):
    name = StringField('Module Name', validators=[DataRequired(), Length(max=100)])
    code = StringField('Module Code', validators=[DataRequired(), Length(max=20), check_module_code])
    current_code = HiddenField()
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Save Module')

class Edit_Topic(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100), check_topic])
    current_title = HiddenField()
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags', validators=[Regexp('^([0-9a-zA-Z-]+ ?)*$', message='Tags can only contain letters, numbers or - and must be sepreated by a space.')])
    submit = SubmitField('Publish Topic')
    draft = SubmitField('Save as draft')

class New_Topic(Edit_Topic):
    image = FileField('Upload Image')
    upload = SubmitField('Upload image')

class Delete(FlaskForm):
    confirm = BooleanField('The action of deletion is non reversible. Please tick this box to confirm', validators=[DataRequired()])
    submit = SubmitField('Delete')

class Image_Upload(FlaskForm):
    file_up = FileField('File')
    submit = SubmitField('Upload')
