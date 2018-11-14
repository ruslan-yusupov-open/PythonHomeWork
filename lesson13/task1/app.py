# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    from models import GuestBookItem

    posts = GuestBookItem.query.all()
    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    posts = [dict(post.to_dict()) for post in posts]

    return jsonify(posts)


@app.route('/create', methods=['POST'])
def create():
    from models import GuestBookItem
    from forms import PostForm

    print(request.form)
    form = PostForm(request.form)

    if form.validate():
        post = GuestBookItem(**form.data)
        db.session.add(post)
        db.session.commit()

        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": str(form.errors)})

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = GuestBookItem(author="Ivan", message="Hi there!")

    db.session.add(ivan)
    db.session.commit()  # note


if __name__ == '__main__':
    from models import *

    db.create_all()

    if GuestBookItem.query.count() == 0:
        populate_db()

    # Running app:
    app.run()
