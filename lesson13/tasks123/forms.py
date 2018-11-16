# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms import TextField, StringField, validators, IntegerField
from wtforms.validators import Optional
from wtforms_alchemy import ModelForm

from models import GuestBookItem


class PostForm(ModelForm):
    class Meta:
        model = GuestBookItem
        validators = {'message': [validators.Length(min=6)]}


class PatchPostForm(ModelForm):
    class Meta:
        model = GuestBookItem
        field_args = {
            'message': {'validators': [validators.Length(min=6), Optional()]},
            'author': {'validators': [Optional()]}
        }


class QueryItemsForm(ModelForm):
    page = IntegerField(validators=[validators.Optional()])
    per_page = IntegerField(validators=[validators.Optional()])
    sort = StringField(validators=[validators.Optional()])
    fields = StringField(validators=[validators.Optional()])

