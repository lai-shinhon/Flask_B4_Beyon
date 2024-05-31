from flask_script import Command
from pokemon_api import db
from pokemon_api.models.pokemons import Pokemon


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()