__author__ = 'Qiong'

from app import db

class User(db.Model):
    # use username as Primary Key
    username = db.Column(db.String(128), index=True, unique=True, primary_key=True)
    posts =  db.relationship('Post', backref='author', lazy='dynamic')
    
    # tell python how to print objects of this class, for debugging
    def __repr__(self):
        return '<User %r>' % (self.username)

class Post(db.Model):
    program = db.Column(db.String)
    output = db.Column(db.String) 
    timestamp = db.Column(db.DateTime)
    id = db.Column(db.String(128), primary_key=True)
    user_name = db.Column(db.String(128), db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Post %r>' % (self.program)
