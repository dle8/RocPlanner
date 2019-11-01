from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired("Email is not in correct form"), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('submit')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired(), Length(min=6, max=15)])
    class_year = IntegerField('class_year', validators=[NumberRange(min=2019, max=2023), DataRequired()])
    submit = SubmitField('submit')
