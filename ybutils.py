#!/usr/bin/env python3
# coding=utf-8
import re
import json
import requests as r
from yblogin import getUserToken, getInfo, BASEURL

'''
单用户使用
'''
with open('config.json','r') as f:
        config = json.loads(f.read())
        
USERNAME = config.get('username')
PASSWD = config.get('password')
yiban_user_token = config.get('cookie',getUserToken(USERNAME, PASSWD))
token = dict(yiban_user_token=yiban_user_token)
info = getInfo(token)
group_id = config.get('group_id',info['group_id'])
puid = config.get('puid',info['puid'])
channel_id = config.get('channel_id',info['channel_id'])
actor_id = config.get('actor_id',13047896) # Public Account
