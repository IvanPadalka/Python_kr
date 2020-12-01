from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
from wtforms.fields.html5 import DateField

from app.models import Car


class NewSong(FlaskForm):
    license_plate = StringField('Name', validators=[DataRequired()])
    brand = StringField('Autors', validators=[DataRequired()])
    condition = SelectField('Description', coerce=int, validators=[InputRequired()])
    on_go = SelectField('Type of the music', choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Funk', 'Funk')])
    price = StringField('Lenght', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    prod_date = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField('Create')

    def validate_licence_plate(self, field):
        if Car.query.filter_by(license_plate=field.data).first():
            raise ValidationError('Song already exists')


class EditSong(FlaskForm):
    license_plate = StringField('Name', validators=[DataRequired()])
    brand = StringField('Autors', validators=[DataRequired()])
    condition = SelectField('Description', coerce=int, validators=[InputRequired()])
    on_go = SelectField('Type of the music', choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Funk', 'Funk')])
    price = StringField('Lenght', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    prod_date = DateField('Pick the year', format='%Y-%m-%d')
    submit = SubmitField('Update')

    def validate_licence_plate(self, field):
        if Car.query.filter_by(license_plate=field.data).first():
            raise ValidationError('Song already exists')