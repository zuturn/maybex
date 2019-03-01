#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
logics
"""
from models import User
from app import db

def user_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user.check_password(password):
        return user 
    return None
