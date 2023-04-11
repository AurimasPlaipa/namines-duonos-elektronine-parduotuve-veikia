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
CORS(app)
ma = Marshmallow(app)
csrf = CSRFProtect(app)
app.config.from_prefixed_env()

# FIXME: Should be removed before deploying to production (i.e. on Digital Ocean)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.db')
app.config['SECRET_KEY'] = "Your_secret_string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'
login_manager.login_message = "You need to Login!"
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
mail = Mail(app)

from app.views import *
from app.admin import *