# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms import TextField, StringField, validators, IntegerField
from wtforms_alchemy import ModelForm

from models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post

    message = StringField(validators=[validators.Length(min=6)])


class CommentForm(ModelForm):
    class Meta:
        model = Comment

    include = [
        'post_id',
    ]

    message = StringField(validators=[validators.Length(min=6)])
    post_id = IntegerField()
