from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,SubmitField, PasswordField, BooleanField, SelectField, DateField, TextAreaField, PasswordField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app.models.Bread import Bread
from app.models.Purchase import Purchase 
from app.models.User import User

class LoginForm(FlaskForm):
    email = StringField('El. Paštas: ', validators=[DataRequired(), Email(message="Įveskite teisingą el. pašto adresą.")])
    password = PasswordField("Slaptažodis: ", validators=[DataRequired(), Length(min=8, max=25, message="Slaptažodis turi būti tarp 8-25 simbolių.")])
    login_button = SubmitField("Prisijungti")


class RegisterForm(FlaskForm):
    name = StringField("Vardas: ", validators=[DataRequired()])
    email = StringField("El. Paštas ", validators=[DataRequired(), Email(message="Nurodytas neteisingas el. pašto adresas")])
    password = PasswordField("Slaptažodis: ", validators=[DataRequired(), EqualTo(fieldname="confirm_password", message="Slaptažodžiai turi sutapti")])
    confirm_password = PasswordField("Patvirtinti slaptažodį", validators=[DataRequired(), Length(min=8, max=25, message="Slaptažodis turi būti tarp 8-25 simbolių.")])
    register_button = SubmitField("Registruotis")


class BreadForm(FlaskForm):
    name = StringField("Pavadinimas", validators=[DataRequired()])
    price = FloatField("Kaina", validators=[DataRequired()])
    description = StringField("Produkto aprašymas", validators=[DataRequired()])
    photo = FileField("Pridėti paveikslėlį", validators=[FileRequired(), FileAllowed(["jpg", "png", "jpeg"], "Įkelti galima tik paveikslėlius!")])
    submit = SubmitField("Įkelti produktą")

class EmailForm(FlaskForm):
    email = StringField('El. paštas', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Užsakyti')
