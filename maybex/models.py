#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
models
"""
from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_stuff = db.Column(db.Boolean, default=True, nullable=False)
    role = db.Column(db.Integer, default=0, nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)
