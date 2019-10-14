from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('uname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('pword', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('pword')])
    twofactor = StringField('2fa', validators=[DataRequired(), Length(10)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('uname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('pword', validators=[DataRequired()])
    twofactor = StringField('2fa', validators=[DataRequired(), Length(10)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ContentForm(FlaskForm):
    body = StringField(u'Text', widget=TextArea())
    submit = SubmitField('Spell Check')
