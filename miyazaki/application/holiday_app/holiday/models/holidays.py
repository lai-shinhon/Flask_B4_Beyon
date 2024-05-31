from holiday import db

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key = True, autoincrement = False)
    holi_text = db.Column(db.String(20))

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text