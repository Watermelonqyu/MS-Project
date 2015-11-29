from smtpd import program
__author__ = 'Qiong'

from flask import render_template, flash, redirect, session, url_for, request, g, Response
from app import app, db
from time import gmtime, strftime, sleep

from datetime import datetime
from .models import User, Post

from random import randint

import subprocess
        
@app.route('/server_time')
def server_time():
    def user_stream():
        while True:
            userss = User.query.all()
            postss = Post.query.all()
            
            for user in userss:
                for perpost in postss:
                    if perpost.id == user.username: 
                        yield "UserID: " + perpost.id +  "\t\tOutput: " + perpost.output + "\t\tTimestamp: " + perpost.timestamp.strftime("%Y-%m-%d %H:%M:%S") + "\n"
                        #  + "\nProgram:\n" + perpost.program + "\n\n"
                        # yield "<a href= " + "{{ url_for('.user', username=" + user.username + ") }}>" + user.username + "</a>"
            # yield 'event: mesg\ndata: {0}\n\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            sleep(60)

            
    return Response(user_stream(), mimetype="text/event-stream")
    # return Response(event_stream(), mimetype="text/html")
    # return render_template('data.html', sentString=user_stream())

@app.route('/usersubmit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # get data from request
        data = request.get_json(force=True)

        # convert data into dictionary
        userData = {}
        for i in data:
            userData.update(i)

        # print("data: ", data2['username'])

        existUser = User.query.get(userData['username'])
        intid = "u" + str(randint(0,300))
            
        if existUser:
            p = Post(program=userData['program'],
                    output=userData['output'], 
                    timestamp=datetime.now(),
                    id=intid,
                    user_name=existUser.username)
            print("existUser: ", intid)

            db.session.add(p)

        else:
            user = User(username=userData['username'])
            p = Post(program=userData['program'],
                     output=userData['output'],
                     timestamp=datetime.now(),
                     id=intid,
                     user_name=userData['username'])
            print("not existing user: ", intid)
            db.session.add(user)
            db.session.add(p)

        db.session.commit()
        
    return 'post';


@app.route('/',  methods=['GET'])
@app.route('/index',  methods=['GET'])
def index():
    postUsers = User.query.all()
    allPosts = Post.query.all()
    
    return render_template('index.html',
                            title='Home',
                            users=postUsers,
                            posts=allPosts)
    

@app.route('/user/<postid>')
def user(postid):
    posts = Post.query.filter_by(id=postid).first()
    users = posts.user_name
    output = ""
    
    if user is None:
        print(username)
        return redirect(url_for('.index'))
    
    return render_template('user.html',
                           users=users,
                           posts=posts,
                           outputs=output)
    
@app.route('/delete_data')
def deleteRecords():
    postUsers = User.query.all()
    allPosts = Post.query.all()
    
    for user in postUsers:
        db.session.delete(user)
    for post in allPosts:
        db.session.delete(post)
        
    db.session.commit()
    
    return render_template('delete_data.html')
    
    
@app.route('/deleteone', methods=['GET', 'POST'])
def deleteOne():
    if request.method == 'POST':
        # get data from request
        data = request.get_json(force=True)
        print(data)
        # convert data into dictionary
        userData = {}
        for i in data:
            userData.update(i)
            
        Post.query.filter_by(id=userData['id']).delete()
        
    db.session.commit()
    
    return redirect(url_for('index'))
    
    
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        data = request.get_json(force=True)
        
        # convert data into dictionary
        userData = {}
        for i in data:
            userData.update(i)

        
        filepath = "D:\\3.py"
        
        print(userData["program"])
        
        programFile = open(filepath, 'w')
        programFile.write(userData["program"])
        
        proc = subprocess.Popen(["python", "D:\\3.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print (proc)
        out= proc.communicate()
        print (out)
        outstr = out[0].decode("utf-8")
        errstr = out[1].decode("utf-8")
        
        outputs = outstr + errstr
        print("outstr and errstr", outputs)

            
        
        posts = Post.query.filter_by(id=userData["id"]).update({"program": userData["program"]})
        db.session.commit()
        
        updatedposts = Post.query.filter_by(id=userData["id"]).first()
        print(updatedposts.program)
        users = updatedposts.user_name
        
        print("running till here")
        
        return render_template('user.html',
                           users=users,
                           posts=updatedposts,
                           outputs=outputs)
    