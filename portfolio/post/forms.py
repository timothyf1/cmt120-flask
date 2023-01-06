from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

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
