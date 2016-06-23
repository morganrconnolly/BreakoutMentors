from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class StudentForm(Form):
	name = StringField('Student Name', validators=[DataRequired()])
