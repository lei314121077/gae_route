#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'raymondlei'


from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# 如果修改这些scopes，请删除以前保存的凭据,凭据的目录如下
# at ~/.credentials/drive-python-quickstart.json

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'                               # 客户端加密文件
APPLICATION_NAME = 'drive API Python Quickstart'


def get_credentials():

    """
    从存储获取有效的用户凭据。

    如果没有存储任何内容，或者如果存储的凭证无效，
    完成OAuth2流程以获取新凭据。

    返回：
        凭证，获得的凭据。
    """

    # 根目录路径
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):

        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:

        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME

        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # 兼容 Python 2.6
            credentials = tools.run(flow, store)
        print('正在将凭据Credentials存储到 ' + credential_path)





def main():

    """
    显示Google云端硬盘API的基本用法。
    创建Google云端硬盘API服务对象并输出名称和ID
    最多10个文件。
    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('没有找到文件......')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))



if __name__ == '__main__':
    main()