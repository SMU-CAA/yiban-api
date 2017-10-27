#!/usr/bin/env python3
# coding=utf-8
import re
import json
import time
import requests
import ybvote
import ybtopic
from yblogin import BASEURL, getUserToken, getInfo

r = requests.Session()

'''
获取一点字符 (Hitokoto API)
'''
def getHitokoto():

    Get_Hitokoto = r.get('https://sslapi.hitokoto.cn/', params={'c':'d','encode':'json'})
    Hitokoto = Get_Hitokoto.json()['hitokoto']
    From = Get_Hitokoto.json()['from']
    return Hitokoto + ' --' + From

'''
config.json 存储键值对
应为 'username': 'password'
'''
with open('config.json','r') as f:

    config = json.loads(f.read())

for user in config.keys():

    USERNAME = user
    PASSWD = config.get(user)
    yiban_user_token = getUserToken(USERNAME, PASSWD)
    token = dict(yiban_user_token=yiban_user_token)
    info = getInfo(token)
    group_id = config.get('group_id',info['group_id'])
    puid = config.get('puid',info['puid'])
    channel_id = config.get('channel_id',info['channel_id'])
    actor_id = config.get('actor_id',13047896) # Public Account

    '''
    调用示例
    获取 EPGA 数值信息
    '''
    def getEPGA(token):

        Get_EPGA = r.get(BASEURL+'newgroup/indexPub/group_id/' +
                        group_id + '/puid/' + puid, cookies=token)
        EPGA = re.search(r'EGPA：[0-9\.]*', Get_EPGA.text)
        return EPGA.group()

    print(getEPGA(token))

    for i in range(1, 10):

        print(ybtopic.topic(token, puid, group_id, channel_id).add('一言',getHitokoto()))
        time.sleep(4)

    for i in range(1, 10):

        print(ybvote.vote(token, puid, group_id).add('一言',getHitokoto(),getHitokoto(),getHitokoto()))
        time.sleep(4)
    
    for i in range(0, 10):

        article_id = ybtopic.topic(token, puid, group_id, channel_id).get()['data']['list'][i]['id']
        print(ybtopic.topic(token, puid, group_id, channel_id).up(article_id))

        for j in range(0, 3):

            print(ybtopic.topic(token, puid, group_id, channel_id).go(article_id, getHitokoto()))
            time.sleep(4)
