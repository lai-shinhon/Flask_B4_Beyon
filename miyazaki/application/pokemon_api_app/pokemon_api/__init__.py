from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('pokemon_api.config')

db = SQLAlchemy(app)

from pokemon_api.views import views