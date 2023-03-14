from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo


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
    # type = StringField("Tipas", validators=[DataRequired()])
    price = FloatField("Kaina", validators=[DataRequired()])
    # supply = IntegerField("Kiek turime sandėlyje", validators=[DataRequired()])
    # size = StringField("Dydis (kiekis)", validators=[DataRequired()])
    description = StringField("Produkto aprašymas", validators=[DataRequired()])
    photo = FileField("Pridėti paveikslėlį", validators=[FileRequired(), FileAllowed(["jpg", "png", "jpeg"], "Įkelti galima tik paveikslėlius!")])
    submit = SubmitField("Įkelti produktą")

class EmailForm(FlaskForm):
    email = StringField('El. paštas', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Užsakyti')
