# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

from forms import *
from models import *

import config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    posts = Post.query.all()

    for post in posts:
        post.comments = Comment.query.filter_by(post=post).all()

    return render_template('home.txt', posts=posts)


@app.route('/createPost', methods=['POST'])
def create_post():
    print(request.form)
    form = PostForm(request.form)

    if form.validate():
        post = Post(**form.data)
        db.session.add(post)
        db.session.commit()
        flash('Post created!')
    else:
        flash('Form is not valid! Post was not created.')
        flash(str(form.errors))

    posts = Post.query.all()
    for post in posts:
        post.comments = Comment.query.filter_by(post=post).all()

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    return render_template('home.txt', posts=posts)


@app.route('/createComment', methods=['POST'])
def create_comment():
    print(request.form)
    form = CommentForm(request.form)
    print(form.data)

    if form.validate():
        comment = Comment(**form.data)
        db.session.add(comment)
        db.session.commit()
        flash('Post created!')
    else:
        flash('Form is not valid! Post was not created.')
        flash(str(form.errors))

    posts = Post.query.all()
    for post in posts:
        post.comments = Comment.query.filter_by(post=post).all()

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    return render_template('home.txt', posts=posts)


def populate_db():
    print('Creating default user')
    # Creating new ones:
    post1 = Post(header="Hi all", message="Hi there!")
    post2 = Post(header="Vsem privet", message="Kak dela")
    post3 = Post(header="Vsem privet3", message="Kak dela1")

    comment11 = Comment(post=post1, message="Hi1")
    comment12 = Comment(post=post1, message="Hi2")

    comment21 = Comment(post=post2, message="Hi3")

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)

    db.session.add(comment11)
    db.session.add(comment12)
    db.session.add(comment21)

    db.session.commit()  # note


if __name__ == '__main__':
    from models import *
    db.create_all()

    if Post.query.count() == 0:
        populate_db()

    # Running app:
    app.run()
