#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
models
"""
from db import db
from hashlib import sha512
from configs import SALT 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_stuff = db.Column(db.Boolean, default=True, nullable=False)
    role = db.Column(db.Integer, default=0, nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        pass_str = SALT + password
        password_c = sha512(pass_str.encode('utf-8')).hexdigest()
        return self.password == password_c


    def set_password(self, password):
        pass_str = SALT + password
        new_password = sha512(pass_str.encode('utf-8')).hexdigest()
        self.password = new_password
