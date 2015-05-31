__author__ = 'Qiong'

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    posts =  db.relationship('Post', backref='author', lazy='dynamic')

    # tell python how to print objects of this class, for debugging
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
