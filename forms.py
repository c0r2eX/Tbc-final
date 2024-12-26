from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import PasswordField
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class Memeupload(FlaskForm):
    text = StringField("Description", validators=[DataRequired(), Length(min=-1, max=40)])
    img = FileField("Your meme picture")
    upload = SubmitField()

class Register(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField("Repeat Password", validators=[EqualTo("password", message="Passwords must match.")])
    register_submit = SubmitField()

class Login(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    login_submit = SubmitField("LOGIN")
