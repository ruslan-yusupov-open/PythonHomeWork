# -*- coding: utf-8 -*-
import datetime

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    header = db.Column(db.String(140), nullable=False)
    message = db.Column(db.String(3000), nullable=False)

    def __str__(self):
        return '<id: {}, header: {}, text: {}>'.format(self.id, self.header, self.message)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
        nullable=False,
        index=True
    )
    post = db.relationship(Post, foreign_keys=[post_id, ])

    message = db.Column(db.String(3000), nullable=False)

    def __str__(self):
        return '<id: {}, message: {}>'.format(self.id, self.message)
