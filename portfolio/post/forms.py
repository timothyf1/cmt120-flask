from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class New_post(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Add Post')
