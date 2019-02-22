#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
app
"""
from flask import Flask
from posts import posts as posts_app
from admin import admin as admin_app


app = Flask(__name__)

app.register_blueprint(posts_app, url_prefix='/posts')
app.register_blueprint(admin_app, url_prefix='/admin')


@app.route('/')
def index():
    return 'maybex'


if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=8089, debug=True)
