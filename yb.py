#!/usr/bin/env python3
# coding=utf-8
import re
import json
import requests
import ybvote
import ybtopic
from yblogin import BASEURL
import time

r = requests.Session()

'''
单用户调用示例
获取 EPGA 数值信息
'''
from ybutils import token, group_id, puid, channel_id, actor_id
def getEPGA(USERTOKEN):

    Get_EPGA = r.get(BASEURL+'newgroup/indexPub/group_id/' +
                     group_id + '/puid/' + puid, cookies=USERTOKEN)
    EPGA = re.search(r'EGPA：[0-9\.]*', Get_EPGA.text)
    return EPGA.group()

print(getEPGA(token))

'''
获取一点字符 (Hitokoto API)
'''
def getHitokoto():

    Get_Hitokoto = r.get('https://sslapi.hitokoto.cn/', params={'c':'d','encode':'json'})
    Hitokoto = Get_Hitokoto.json()['hitokoto']
    From = Get_Hitokoto.json()['from']
    return Hitokoto + ' --' + From

'''
多用户调用示例
multiuser.json 键值对应为 username: password
'''
with open('multiuser.json','r') as f:
    config = json.loads(f.read())

for user in config.keys():

    from yblogin import getUserToken, getInfo
    USERNAME = user
    PASSWD = config.get(user)
    yiban_user_token = getUserToken(USERNAME, PASSWD)
    token = dict(yiban_user_token=yiban_user_token)
    info = getInfo(token)
    group_id = config.get('group_id',info['group_id'])
    puid = config.get('puid',info['puid'])
    channel_id = config.get('channel_id',info['channel_id'])
    actor_id = config.get('actor_id',13047896) # Public Account

    for i in range(1, 10):

        print(ybtopic.topic(token).add('一言',getHitokoto()))
        time.sleep(4)

    for i in range(1, 10):

        print(ybvote.vote(token).add('一言',getHitokoto(),getHitokoto(),getHitokoto()))
        time.sleep(4)
    
    for i in range(0, 10):

        article_id = ybtopic.topic(token).get()['data']['list'][i]['id']
        print(ybtopic.topic(token).up(article_id))

        for j in range(0, 3):

            print(ybtopic.topic(token).go(article_id, getHitokoto()))
            time.sleep(4)
