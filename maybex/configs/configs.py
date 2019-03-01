#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
configs
"""

# ======DATABASE======
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_URI = 'postgresql://{username}:{password}@{host}:{port}/{db}'.format(
    username=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT,
    db=DB_NAME)
