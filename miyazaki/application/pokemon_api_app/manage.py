from flask_script import Manager
from pokemon_api import app

from pokemon_api.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()