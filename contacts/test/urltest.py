#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'raymondlei'

from webapp2 import RequestHandler
from route import route

@route('/test')
class MainPage(RequestHandler):

    print route.handlers


    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World and this is my first gae app!!!!')
