import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask_marshmallow import Marshmallow
import secrets

app = Flask(__name__)
app.app_context().push()
Bootstrap(app)


app.config["SECRET_KEY"] = "Your secret string"


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(basedir, 'data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
mail = Mail(app)


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'
login_manager.login_message = "You need to Login!"
from app.views import *
from app.admin import *