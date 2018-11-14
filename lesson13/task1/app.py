# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

import config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


# noinspection PyUnusedLocal
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"success": False, "error": "Not found"}), 404


@app.route('/items', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    from models import GuestBookItem

    # ide генерирует ошибку, если запихивать false inline, is False не работает
    false = False
    posts = GuestBookItem.query.filter(GuestBookItem.is_deleted == false)

    posts = [dict(post.to_dict()) for post in posts]

    return jsonify(posts)


@app.route('/items', methods=['POST'])
def create():
    from models import GuestBookItem
    from forms import PostForm

    print(request.form)
    form = PostForm(request.form)

    if form.validate():
        post = GuestBookItem(**form.data)
        db.session.add(post)
        db.session.commit()

        resp = make_response(jsonify(post.to_dict()))
        resp.status_code = 201
        resp.headers['Location'] = '/items/{}'.format(post.id)

        return resp
    else:
        return jsonify({"success": False, "error": str(form.errors)}), 400


# восстанавливает все записи
@app.route('/items', methods=['PATCH'])
def index_patch():
    from models import GuestBookItem

    posts = GuestBookItem.query.all()

    for post in posts:
        post.is_deleted = False

    db.session.commit()

    posts = [dict(post.to_dict()) for post in posts]

    return jsonify(posts)


@app.route('/items', methods=['PUT'])
def index_put():
    from models import GuestBookItem

    # ide генерирует ошибку, если запихивать false inline, is False не работает
    false = False
    posts = GuestBookItem.query.filter(GuestBookItem.is_deleted == false)

    for post in posts:
        post.is_deleted = True

    db.session.commit()

    return jsonify([])


@app.route('/items/<int:post_id>', methods=['GET'])
def items_id(post_id):
    from models import GuestBookItem

    post = GuestBookItem.query.filter(GuestBookItem.id == post_id).first()

    if post and post.is_deleted is False:
        return jsonify(post.to_dict())
    else:
        abort(404)


@app.route('/items/<int:post_id>', methods=['DELETE'])
def items_id_delete(post_id):
    if len(request.form) == 0:
        from models import GuestBookItem
        post = GuestBookItem.query.filter(GuestBookItem.id == post_id).first()

        if post and post.is_deleted is False:
            post.updated_at = datetime.datetime.utcnow()
            post.is_deleted = True
            db.session.commit()

            return jsonify({"success": True})
        else:
            return "", 204
    else:
        return jsonify({"success": False, "error": "Bad request"}), 400


@app.route('/items/<int:post_id>', methods=['PUT'])
def items_id_put(post_id):
    from models import GuestBookItem
    post = GuestBookItem.query.filter(GuestBookItem.id == post_id).first()

    if post and post.is_deleted is False:
        from forms import PostForm
        form = PostForm(request.form)

        print(request.form)
        if form.validate():
            post.author = form.data['author']
            post.message = form.data['message']

            post.updated_at = datetime.datetime.utcnow()

            db.session.commit()

            resp = make_response(jsonify(post.to_dict()))
            resp.status_code = 201
            resp.headers['Location'] = '/items/{}'.format(post.id)

            return resp
        else:
            return jsonify({"success": False, "error": str(form.errors)}), 400
    else:
        abort(404)


@app.route('/items/<int:post_id>', methods=['PATCH'])
def items_id_patch(post_id):
    from models import GuestBookItem
    post = GuestBookItem.query.filter(GuestBookItem.id == post_id).first()

    if post and post.is_deleted is False:
        from forms import PatchPostForm
        form = PatchPostForm(request.form)

        print(request.form)
        if form.validate():
            if 'author' in form.data and form.data['author'] != '':
                post.author = form.data['author']

            if 'message' in form.data and form.data['message'] != '':
                post.message = form.data['message']

            post.updated_at = datetime.datetime.utcnow()

            db.session.commit()

            resp = make_response(jsonify(post.to_dict()))
            resp.status_code = 201
            resp.headers['Location'] = '/items/{}'.format(post.id)

            return resp
        else:
            return jsonify({"success": False, "error": str(form.errors)}), 400
    else:
        abort(404)


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

    app.run()