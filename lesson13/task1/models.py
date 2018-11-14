# -*- coding: utf-8 -*-
import datetime

from app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    author = db.Column(db.String(140), nullable=False)
    message = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return '<Post %r, user_id %s>'.format(self.title, self.user_id)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "message": self.message,
            "date_created": self.date_created,
            "is_deleted": self.is_deleted
        }
