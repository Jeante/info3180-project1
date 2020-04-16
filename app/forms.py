from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField, TextField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField ('Gender', choices=[('male','Male'), ('female','Female')])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography= TextField('Biography', validators=[InputRequired()]) 
    photo = FileField ('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])