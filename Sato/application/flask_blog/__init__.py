from flask import Flask

app=Flask(__name__)

import flask_blog.views

app.config.from_object('flask_blog.config')