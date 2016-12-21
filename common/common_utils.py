#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import hashlib
import re
import json
import logging
import logging.config
import io
import random
import time
import datetime

import common_setting



__author__ = 'raymondlei'



def init_log(default_path='logs/logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    初始化log
    :param default_path , default_level , env_key
    @desc : 參考logging的實現 http://www.iplaypython.com/code/c245.html
    @desc : 每个 Python 程序员都要知道的日志实践 http://python.jobbole.com/81666/
    """

    path = default_path
    value = os.getenv(env_key, None)

    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        if common_setting.IS_DEBUG:  # 判定系統狀態,把日誌同時輸出到屏幕和文件
            config['root']['level'] = "DEBUG"
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return