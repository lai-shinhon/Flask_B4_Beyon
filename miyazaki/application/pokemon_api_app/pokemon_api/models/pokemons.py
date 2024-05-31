from pokemon_api import db
from datetime import datetime

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    name = db.Column(db.String(100), primary_key=True, autoincrement = False)
    id = db.Column(db.Integer, unique=True)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    types = db.Column(db.Text)
    image_url = db.Column(db.Text)
    get_at = db.Column(db.DateTime)
    category = db.Column(db.Text)

    def __init__(self, name=None, id=None, height=None, weight=None, types=None, image_url=None, get_at=None, category=None):
        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
        self.types = types
        self.image_url = image_url
        self.get_at = get_at
        self.get_at = datetime.utcnow()
        self.category = category
