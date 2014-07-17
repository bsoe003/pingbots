from app import db


class User(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    
    def __repr__(self):
        return '<User %r>' % (self.username)
