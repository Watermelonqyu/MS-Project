__author__ = 'Qiong'

from flask import render_template, flash, redirect, session, url_for, request, g
# from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
import json
# from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [ # fake array of posts
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'nickname': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            } ]

    if request.method == 'POST':
        '''
        jauthor = request.form['author']
        jbody = request.form['body']

        postauthor = {'author': jauthor}
        postbody = {'body': jbody}

        posts = [postauthor, postbody]
        '''
        posts = request.data
        print("hello\n")
        print("request.form", request.form)
        data = request.get_json(force=True)
        user = User(id='try',
                    nickname='trytry',
                    email='qyu1@memphis.edu',
                    body='POST')
        db.session.add(user)
        db.session.commit()
    #　user = g.user

    post = User.query.get("try")
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=post)