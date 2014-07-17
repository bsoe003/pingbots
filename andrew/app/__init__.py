from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

db = SQLAlchemy(app)
lm = LoginManager()

from app import views, models
from config import basedir

lm.init_app(app)
