__author__ = 'Qiong'

from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from datetime import datetime
from .models import User, Post


@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])
def index():
   
    if request.method == 'POST':
        # get data from request
        data = request.get_json(force=True)

        # convert data into dictionary
        userData = {}
        for i in data:
            userData.update(i)

        # print("data: ", data2['username'])

        existUser = User.query.get(userData['username'])

        if existUser:
            p = Post(program=userData['body'],
                 timestamp=datetime.now(),
                 author=existUser)
            print("existUser: ", p)

            db.session.add(p)

        else:
            user = User(username=userData['username'])
            p = Post(program=userData['program'],
                 timestamp=datetime.now(),
                 author=user)
            print("not existing user: ", user)
            print("not existing post: ", p)
            db.session.add(user)
            db.session.add(p)

        db.session.commit()


    postUsers = User.query.all()

    for user in postUsers:
        userpost = user.posts.all()
        print('\n', user.username,
              '\n', userpost)

    return render_template('index.html',
                            title='Home',
                            user=user)