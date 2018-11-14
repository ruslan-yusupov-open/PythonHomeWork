# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms import TextField, StringField, validators
from wtforms_alchemy import ModelForm

from models import GuestBookItem


class PostForm(ModelForm):
    class Meta:
        model = GuestBookItem

    message = StringField(validators=[validators.Length(min=6)])
    # include = [
    #     'user_id',
    # ]
