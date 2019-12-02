from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Register(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Pasword', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sign_up = SubmitField('Sign Up')

class LoginForm(FlaskForm):
   email = StringField('Email', validators=[DataRequired(), Email()])         
   username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
   password = PasswordField('Pasword', validators=[DataRequired()])
   rember = BooleanField('Remember Me')
   sign_up = SubmitField('Log In')


            

