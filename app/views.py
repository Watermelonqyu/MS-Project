__author__ = 'Qiong'

from flask import render_template, flash, redirect, session, url_for, request, g
# from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from datetime import datetime
# from .forms import LoginForm
from .models import User, Post


@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])
def index():
    user = {'nickname': 'Miguel'}  # fake user

    if request.method == 'POST':
        '''
        jauthor = request.form['author']
        jbody = request.form['body']

        postauthor = {'author': jauthor}
        postbody = {'body': jbody}

        posts = [postauthor, postbody]
        '''
        # posts = request.form
        # posts.getlist('id')
        # print("request.form:", request.form)
        # print("request.data:", request.data)

        data = request.get_json(force=True)
        #vdata2 = { i.keys()[0] : i.values()[0] for i in data }
        # dict = dict(data)
        userId = data[0]
        userName = data[1]
        userBody = data[2]
        data2 = {}
        for i in data:
            data2.update(i)


        print("data: ", data2['username'])
        # print("end of pringting", dict['username'])

        # author = flask.jsonify(data)
        '''
        dict = defaultdict(data)

        for k, v in data:
            dict[k].append(v)

        needDict = dict((k, tuple(v)) for k, v in dict.iteritems())


        postsj = json.dumps(posts)

        # print("hello", request.json())
        postsjson = json.loads(postsj)

'''
        existUser = User.query.get(userId['id'])

        if existUser:
            p = Post(program=userBody['body'],
                 timestamp=datetime.now(),
                 author=existUser)
            print("existUser: ", p)

            db.session.add(p)

        else:
            user = User(id=userId['id'],
                    username=userName['username'])
            p = Post(program=userBody['body'],
                 timestamp=datetime.now(),
                 author=user)
            print("not existing user: ", user)
            print("not existing post: ", p)
            db.session.add(user)
            db.session.add(p)

        db.session.commit()
    #　user = g.user


    postUsers = User.query.all()

    for user in postUsers:
        userpost = user.posts.all()
        print('\n', user.id, user.username,
              '\n', userpost)

    return render_template('index.html',
                            title='Home',
                            user=user
                            # posts=postBody
                            )