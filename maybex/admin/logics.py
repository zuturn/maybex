#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
logics
"""
from models import User


def user_login(username, password):
    user = User.query.filter_by(username=username).first()

    # if user.check(password):
    if user.password == password:
        return user 
    return None
