from flask import Flask
import app.models

app = Flask(__name__)
app.config.from_object("config")
from app.controllers import default
