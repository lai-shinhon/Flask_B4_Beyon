from flask_script import Command
from ballon import db
from ballon.models.entries import Entry

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()