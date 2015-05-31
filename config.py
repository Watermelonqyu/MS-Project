__author__ = 'Qiong'

import os

# enable CSRF
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# provide openid
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# database setup
basedir = os.path.abspath(os.path.dirname(__file__))
# this is required by the Flask-SQLAlchemy extension
# this is the path of our database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# the folder where store the SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')