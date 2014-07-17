from app import db


class User(db.Model):
    username = db.Column(db.String(64), primary_key=True)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False



class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    size = db.Column(db.Integer)
    
