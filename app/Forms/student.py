from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, DecimalField, HiddenField, SelectField
from wtforms.validators import DataRequired, Regexp

class AddStudent(FlaskForm):
    studentID = StringField(
        "Student ID (Format: ####-####)",
        validators=[
            DataRequired(),
            Regexp(r"\d{4}-\d{4}", message="Student ID must be in the format ####-####")
        ]
    )
    Name = StringField("Name", validators=[DataRequired()])
    YearLevel = SelectField(
        "Year Level",
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        validators=[DataRequired()]
    )
    Gender = SelectField(
        "Gender",
        choices=[('Male', 'Male'), ('Female', 'Female')],
        validators=[DataRequired()]
    )
    Course = SelectField(
        "Course",
        choices=[],  # Will be populated dynamically in the view
        validators=[DataRequired()]
    )
    College = SelectField(
        "College",
        choices=[],  # Will be populated dynamically in the view
        validators=[DataRequired()]
    )
    Photo = FileField("Upload Photo", 
                           validators=[DataRequired()])