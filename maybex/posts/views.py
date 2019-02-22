#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
views
"""
from . import posts


@posts.route('/<pid>', methods=['GET'])
@posts.route('/<pid>/<cid>')
def post(pid, cid=None):
    return 'pid is: {}, cid is {}'.format(pid, cid)
