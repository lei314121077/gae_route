#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

from common_setting import  IS_DEBUG
from route import route
from common.common_utils import init_log
from contacts import test

# from google.appengine.ext import webapp

app = webapp2.WSGIApplication(routes=route.handlers, debug=IS_DEBUG)

if __name__ == '__main__':

    init_log()
    run_wsgi_app(app)

