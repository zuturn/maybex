#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
views
"""
from . import admin 
from . import logics
from flask import render_template, request, make_response


@admin.route('/', methods=['GET', 'POST'])
def index():
    """
    登录首页
    1.登录状态直接跳转后台首页
    2.非登录状态跳转至登录页
    """
    error_msg = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            error_msg = 'username or password is empty'
        # 验证用户
        if logics.user_login(username, password):
            response = make_response(render_template('admin.html'))
            response.set_cookie('sessionid' , '1234567890')
            return response
        error_msg = 'username or password inviled'
    else:
        # 验证session
        if request.cookies.get('sessionid') == '1234567890':
            return render_template('admin.html')
    return render_template('admin_login.html', error_msg=error_msg)


@admin.route('/logout')
def logout():
    """
    清除用户记录并退出
    """
    response = make_response(render_template('admin_login.html'))
    response.set_cookie('sessionid' , '', 0)
    return response


@admin.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'GET':
        return render_template('list.html')
    return 'af'


@admin.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('list.html')
    return 'miss'


@admin.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template('list.html')
    return 'miss'
