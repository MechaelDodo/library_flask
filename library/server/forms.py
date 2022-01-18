from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, Label
from wtforms.validators import Email, DataRequired


class AuthorizationForm(FlaskForm):
    message = TextAreaField('message:')#, validators=[TextAreaField()])
    message.validators = [DataRequired()]
    username = StringField('username:')# validators=[DataRequired()])
    username.validators = [DataRequired()]
    password = PasswordField('password:')#, validators=[DataRequired()])
    password.validators = [DataRequired()]
    submit = SubmitField('enter')


class DetailListForm(FlaskForm):
    books_list = SelectField('Books: ', choices=[])
    authors_list = SelectField('Author: ', choices=[])


class AuthorForm(FlaskForm):
    author_name = StringField('Author: ')
    #author_name.validators = [DataRequired()]
    biography = StringField('Biography: ')
    submit = SubmitField('Add')


#class BooksListForm(FlaskForm):
#    label_name = StringField('Book list')


