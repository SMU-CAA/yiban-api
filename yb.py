#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import re
import json
import time
import requests
import getopt
import ybvote
import ybtopic
import ybfeed
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
user 应为 'username': 'password'
'''
try:
    opts, args = getopt.getopt(sys.argv[1:], "c:",["config"])
    global f
    for o, a in opts:
        if o in ("-c", "--config"):
            f = open(a, 'r')
    else:
        f = open(os.path.split(os.path.realpath(__file__))[0]+'/config.json', 'r')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

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
    actor_id = conf.get('actor_id', info['actor_id'])
    nick = info['nick']

    range_i = conf.get('vote_count', 2)
    range_m = conf.get('vote_reply_count', 2)
    range_n = conf.get('add_vote_reply_count', 6)
    range_j = conf.get('topic_count', 2)
    range_k = conf.get('topic_reply_count', 2)
    range_l = conf.get('add_topic_reply_count', 6)

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

    for i in range(0, range_i):

        try:
            print(nick + ': 添加投票 ' + ybvote.vote(token, puid, group_id).add('一言 ' + time.asctime(
                time.localtime(time.time())), getHitokoto(cat), getHitokoto(cat), getHitokoto(cat)) + str(i + 1))
        except:
            print(nick + ': 添加投票时未获取到的错误' + str(i + 1))
        finally:
            time.sleep(3)

    for j in range(0, range_j):

        try:
            print(nick + ': 添加话题 ' + ybtopic.topic(token, puid, group_id, channel_id).add(
                '一言 ' + time.asctime(time.localtime(time.time())), getHitokoto(cat)) + str(j + 1))
        except:
            print(nick + ': 添加话题时未获取到的错误' + str(j + 1))
        finally:
            time.sleep(3)

    for m in range(0, range_m):

        try:
            vote_id = ybvote.vote(token, puid, group_id).get(
                range_m)['data']['list'][m]['id']

            for n in range(0, range_n):

                try:
                    print(nick + ': 添加投票评论 ' + ybvote.go(token, puid, group_id, actor_id,
                                                         vote_id, 0, 0).reply(getHitokoto(cat), 0, 0) + str(n + 1))
                except:
                    print(nick + ': 添加投票评论时未获取到的错误' + str(n + 1))
                finally:
                    time.sleep(3)
        except:
            print(nick + ': 获取投票列表时未获取到的错误' + str(m + 1))
        finally:
            time.sleep(3)

    for k in range(0, range_k):

        try:
            article_id = ybtopic.topic(token, puid, group_id, channel_id).get(range_k)[
                'data']['list'][k]['id']

            for l in range(0, range_l):

                try:
                    print(nick + ': 添加话题评论 ' + ybtopic.topic(token, puid,
                                                             group_id, channel_id).reply(article_id, getHitokoto(cat)) + str(l + 1))
                except:
                    print(nick + ': 添加话题评论时未获取到的错误' + str(l + 1))
                finally:
                    time.sleep(3)

        except:
            print(nick + ': 获取话题列表时未获取到的错误' + str(k + 1))
        finally:
            time.sleep(3)
