from app import db, marshmallow

class Sub(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))

    def __init__(self, name, description):
        self.name = name
        self.description = description

if __name__ == 'models':
    db.create_all()