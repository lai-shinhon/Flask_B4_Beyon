from ballon import db
from datetime import datetime


class Entry(db.Model):
    __tablename__ = 'ballons'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    air = db.Column(db.Integer)
    message = db.Column(db.Text)
    country = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, size=None, air=None, message=None, country=None):
        self.size = size
        self.air = air
        self.message = message
        self.country = country
        self.created_at = datetime.utcnow()

    def __repr__(self):
        # return f'<Entry id:{self.id} size:{self.size} air:{self.air} message:{self.message} country:{self.country} date:{self.created_at}>'
        return f'{{\"id\": {self.id}, \"size\":{self.size}, \"air\": {self.air}, \"message\": \"{self.message}\"}}'