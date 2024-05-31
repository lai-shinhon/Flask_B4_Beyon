from holi import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.DateTime, primary_key=True)
    holi_text = db.Column(db.Text)

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return f'<Entry date:{self.holi_date} text:{self.holi_text}>'