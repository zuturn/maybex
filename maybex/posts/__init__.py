#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__init__
"""
from flask import Blueprint


posts = Blueprint('posts', __name__)


from . import views
