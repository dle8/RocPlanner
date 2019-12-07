from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, NumberRange, EqualTo

blank_field = "This field can not be blank"
incorrect_form_email = "Email is not in correct form"


def incorrect_range_number(min, max):
    return "Number is not in correct range: {} to {}".format(min, max)


class LoginForm(FlaskForm):
    email = StringField(
        'email',
        validators=[DataRequired(message=blank_field), Email(message=incorrect_form_email)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(blank_field), Length(min=6, max=15, message=incorrect_range_number(6, 15))]
    )
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField('submit')


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(blank_field)])
    email = StringField('email', validators=[DataRequired(blank_field), Email(incorrect_form_email)])
    password = PasswordField(
        'password',
        validators=[DataRequired(blank_field), Length(min=6, max=15, message=incorrect_range_number(6, 15))]
    )
    class_year = IntegerField(
        'class_year',
        validators=[NumberRange(min=2019, max=2023, message=incorrect_range_number(2019, 2023)),
                    DataRequired(blank_field)])
    submit = SubmitField('submit')


class ResetPasswordForm(FlaskForm):
    temporary_password = StringField('temporary_password', validators=[DataRequired(message=blank_field)])
    new_password = PasswordField(
        'new_password',
        validators=[
            DataRequired(),
            Length(min=6, max=15, message=incorrect_range_number(6, 15)),
            EqualTo('new_password_confirm', message='Password must match')
        ],
    )
    new_password_confirm = PasswordField('new_password_confirm', validators=[DataRequired(), Length(min=6, max=15,
                                                                                                    message=incorrect_range_number(
                                                                                                        6, 15))])
