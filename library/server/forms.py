from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired


class AuthorizationForm(FlaskForm):
    message = StringField('message:')#, validators=[TextAreaField()])
    message.validators = [TextAreaField()]
    username = StringField('username:')# validators=[DataRequired()])
    username.validators = [DataRequired()]
    password = PasswordField('password:')#, validators=[DataRequired()])
    password.validators = [DataRequired()]
    submit = SubmitField('enter')
