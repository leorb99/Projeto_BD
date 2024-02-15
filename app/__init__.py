from flask import Flask
import app.models
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config")
app.config['SECRET_KEY'] = "ec9439cfc6c796ae2029594d"
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
from app.controllers import routes