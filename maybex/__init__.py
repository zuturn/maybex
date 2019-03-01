#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
app
"""
from flask import Flask
from posts import posts as posts_app
from admin import admin as admin_app
from configs import configs


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = configs.DB_URI


# setattr(app, 'db' , db)

app.register_blueprint(posts_app, url_prefix='/posts')
app.register_blueprint(admin_app, url_prefix='/admin')


@app.route('/')
def index():
    return 'maybex'

