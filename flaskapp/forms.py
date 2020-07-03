from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from wtforms.widgets import TextArea
from flaskapp.models import User

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',
    validators=[DataRequired(),
    Length(min=2,max=25)])

    lastname = StringField('Last Name',
    validators=[DataRequired(),
    Length(min=2,max=25)])

    submit = SubmitField('Sign Up')

class RegisterUser(FlaskForm):
    def validate_username(form, username):
        user = User.query.filter_by(username=username.data).first()
        # if len(field.data) > 50:
        if user:
            raise ValidationError('Username Taken')

    def validate_email(form, email):
        user = User.query.filter_by(email=email.data).first()
        # if len(field.data) > 50:
        if user:
            raise ValidationError('Email Taken')

    fname = StringField('First Name',
    validators=[DataRequired(),
    Length(min=2,max=25)])

    lname = StringField('Last Name',
    validators=[DataRequired(),
    Length(min=2,max=25)])

    username = StringField('Username',
    validators=[DataRequired(),
    Length(min=2,max=25)])

    

    
    
    email  = StringField('Email',
    validators=[DataRequired(),
    Length(min=2,max=25),Email()])

    password = PasswordField('Password',
    validators=[DataRequired(),
    Length(min=6,max=15),EqualTo('confirm',message="Passwords do not match.")])

    confirm=PasswordField('Confirm Password')

    submit = SubmitField('Sign Up')

class LoginUser(FlaskForm):
    
    email = StringField('Email',
    validators=[DataRequired(),
    Length(min=10,max=50)])

    password = PasswordField('Password',
    validators=[DataRequired(),
    Length(min=6,max=15)])


    submit = SubmitField('Login')