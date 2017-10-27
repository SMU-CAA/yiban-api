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
获取一言字符 (Hitokoto API)
'''

def getHitokoto(cat):

    Get_Hitokoto = r.get('https://sslapi.hitokoto.cn/',
                         params={'c': cat, 'encode': 'json'})
    Hitokoto = Get_Hitokoto.json()['hitokoto']
    From = Get_Hitokoto.json()['from']
    return Hitokoto + ' --' + From


'''
config.json 存储键值对
应为 'username': 'password'
'''

with open('config.json', 'r') as f:

    config = json.loads(f.read())
    user = config['user']
    conf = config['configs']
    cat = conf.get('cat', 'b')

for username in user.keys():

    USERNAME = username
    PASSWD = user.get(username)
    yiban_user_token = getUserToken(USERNAME, PASSWD)
    token = dict(yiban_user_token=yiban_user_token)
    info = getInfo(token)
    group_id = conf.get('group_id', info['group_id'])
    puid = conf.get('puid', info['puid'])
    channel_id = conf.get('channel_id', info['channel_id'])
    actor_id = conf.get('actor_id', 13047896)  # Public Account
    range_i = conf.get('vote_count', 10)
    range_j = conf.get('topic_count', 10)
    range_k = conf.get('reply_count', 10)
    range_l = conf.get('add_reply_count', 6)

    '''
    调用示例
    获取 EPGA 数值信息
    '''

    def getEPGA(token):

        Get_EPGA = r.get(BASEURL + 'newgroup/indexPub/group_id/' +
                         group_id + '/puid/' + puid, cookies=token)
        EPGA = re.search(r'EGPA：[0-9\.]*', Get_EPGA.text)
        return EPGA.group()

    print(getEPGA(token))

    for i in range(1, range_i):

        try:
            print(USERNAME + ': ' + ybvote.vote(token, puid, group_id).add('一言' + time.asctime(
                time.localtime(time.time())), getHitokoto(cat), getHitokoto(cat), getHitokoto(cat)))
        except:
            print(USERNAME + ': 添加投票时未获取到的错误' + i)
        finally:
            time.sleep(3)

    for j in range(1, range_j):

        try:
            print(USERNAME + ': ' + ybtopic.topic(token, puid, group_id, channel_id).add(
                '一言' + time.asctime(time.localtime(time.time())), getHitokoto(cat)))
        except:
            print(USERNAME + ': 添加话题时未获取到的错误' + j)
        finally:
            time.sleep(3)

    for k in range(0, range_k):

        try:
            article_id = ybtopic.topic(token, puid, group_id, channel_id).get()['data']['list'][k]['id']

            for l in range(1, range_l):

                try:
                    print(USERNAME + ': ' + ybtopic.topic(token, puid,
                        group_id, channel_id).go(article_id, getHitokoto(cat)))
                except:
                    print(USERNAME + ': 添加评论时未获取到的错误' + l)
                finally:
                    time.sleep(3)

        except:
            print(USERNAME + ': 获取评论列表时未获取到的错误' + k)
        finally:
            time.sleep(3)
