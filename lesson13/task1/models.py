# -*- coding: utf-8 -*-
import datetime

from app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    author = db.Column(db.String(140), nullable=False)
    message = db.Column(db.String(3000), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return '<Post %r, author %s>'.format(self.message, self.author)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "message": self.message,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted
        }
