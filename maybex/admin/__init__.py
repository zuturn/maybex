#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__init__
"""
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views


@admin.before_request
def before_requst():
    print('------')
