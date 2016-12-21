#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

__author__ = 'raymondlei'


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)