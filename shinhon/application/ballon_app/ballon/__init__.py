from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ballon.config')

db = SQLAlchemy(app)

from ballon.views import views