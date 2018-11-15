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

    def to_dict(self, filter_fields=None):
        ret_dict = {
            "id": self.id,
            "author": self.author,
            "message": self.message,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # private "is_deleted": self.is_deleted
        }

        if len(filter_fields) > 0:
            new_dict = {}
            for field in ret_dict:
                if field in filter_fields:
                    new_dict[field] = ret_dict[field]
            return new_dict

        return ret_dict

    @staticmethod
    def get_field(field: str):
        if field == "id":
            return GuestBookItem.id
        if field == "author":
            return GuestBookItem.author
        if field == "message":
            return GuestBookItem.message
        if field == "created_at":
            return GuestBookItem.created_at
        if field == "updated_at":
            return GuestBookItem.updated_at
        return None
