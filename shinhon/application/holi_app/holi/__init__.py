from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('holi.config')

db = SQLAlchemy(app)

from holi.views import views, form