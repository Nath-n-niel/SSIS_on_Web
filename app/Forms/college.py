from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, DecimalField, HiddenField
from wtforms.validators import DataRequired

class AddCollege(FlaskForm):
    collegeName = StringField("Course Name", validators=[DataRequired()])
    college = StringField("College", validators=[DataRequired()]) 
    submit = SubmitField("Submit")