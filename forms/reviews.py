from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email


class ReviewsForm(FlaskForm):
    submit = SubmitField('Разблокировать')