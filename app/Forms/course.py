from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, DecimalField, HiddenField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class AddCourse(FlaskForm):
    courseName = StringField("Course Name", validators=[DataRequired()])
    college = SelectField("College", validators=[DataRequired()], choices=[])  # Choices will be set dynamically
    courseCode = StringField("Course Code", validators=[DataRequired()])
    submit = SubmitField("Submit")
