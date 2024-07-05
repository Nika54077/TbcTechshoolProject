from flask_wtf import FlaskForm
from wtforms.fields import  PasswordField, SubmitField, StringField

from wtforms.validators import  DataRequired, length, equal_to

class RegisterForm(FlaskForm):
    password = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), length(min=8, max=20)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password")])
    username = StringField("შეიყვანეთ იუზერი", validators=[DataRequired()])

    register = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    password = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), length(min=8, max=20)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password")])
    username = StringField("შეიყვანეთ იუზერი", validators=[DataRequired()])

    log_in = SubmitField("შესვლა")

