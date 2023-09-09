from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Patient(FlaskForm):
    username=StringField('Patient Name', validators=[DataRequired(),Length(min=3,max=20)])
    email=StringField('E-Mail', validators=[DataRequired(),Email()])
    pin=PasswordField('PIN', validators=[DataRequired()])
    conpin=PasswordField('Confirm PIN', validators=[DataRequired(),EqualTo('pin')])
    submit=SubmitField('Register')

class Doctor(FlaskForm):
    username=StringField('Doctor Name', validators=[DataRequired(),Length(min=3,max=20)])
    email=StringField('E-Mail', validators=[DataRequired(),Email()])
    pin=PasswordField('Password', validators=[DataRequired()])
    conpin=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('pin')])
    submit=SubmitField('Employee')
