#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import re
import json
import time
import getopt
import random
import requests
import traceback
import ybvote
import ybtopic
#import ybfeed
from .yblogin import BASEURL, getUserToken, getInfo

r = requests.Session()

'''
调用示例
获取 EPGA 数值信息
'''

def getEPGA(token):

    Get_EPGA = r.get(BASEURL + 'newgroup/indexPub/group_id/' +
                     group_id + '/puid/' + puid, cookies=token, timeout=10)
    EPGA = re.search(r'EGPA：[0-9\.]*', Get_EPGA.text)
    return EPGA.group()


'''
获取一言字符 (Hitokoto API)
'''

def getHitokoto(CAT):

    Get_Hitokoto = r.get('https://sslapi.hitokoto.cn/',
                         params={'c': CAT, 'encode': 'json'}, timeout=10)
    Hitokoto = Get_Hitokoto.json()['hitokoto']
    From = Get_Hitokoto.json()['from']
    return Hitokoto + ' --' + From

def wait():
    return time.sleep(random.uniform(1, 3))


def fprint(I):
    return ' #' + str(I + 1)


'''
config.json 存储键值对
user 应为 'username': 'password'
'''

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:", ["config"])
    global f
    for o, a in opts:
        if o in ("-c", "--config"):
            f = open(a, 'r')
    else:
        f = open(os.path.split(os.path.realpath(__file__))
                 [0] + '/config.json', 'r')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

config = json.loads(f.read())

user = config['user']
conf = config['configs']
cat = conf.get('cat', 'b')

add_vote_count = conf.get('add_vote_count', 2)

vote_control_count = conf.get('vote_control_count', 5)
vote = conf.get('vote', True)
vote_up = conf.get('vote_up', True)
vote_reply_count = conf.get('vote_reply_count', 1)

add_topic_count = conf.get('add_topic_count', 2)

topic_control_count = conf.get('topic_control_count', 5)
topic_up = conf.get('topic_up', True)
topic_reply_count = conf.get('topic_reply_count', 1)

for username in user.keys():

    try:
        USERNAME = username
        PASSWD = user.get(username)
        yiban_user_token = getUserToken(USERNAME, PASSWD)
        if yiban_user_token == "711":
            print(USERNAME + ': 需要输入验证码。', traceback.format_exc())
            break
        token = dict(yiban_user_token=yiban_user_token)
        info = getInfo(token)

        group_id = conf.get('group_id', info['group_id'])
        puid = conf.get('puid', info['puid'])
        channel_id = conf.get('channel_id', info['channel_id'])
        actor_id = conf.get('actor_id', info['actor_id'])
        nick = info['nick']

        print(getEPGA(token))

        for i in range(0, add_vote_count):

            try:
                print(nick + ': 添加投票 ' + ybvote.vote(token, puid, group_id).add(getHitokoto(cat), getHitokoto(cat), getHitokoto(cat), getHitokoto(cat)) + fprint(i))
            except:
                print(nick + ': 添加投票时未获取到的错误' + fprint(i), traceback.format_exc())
            finally:
                wait()

        for i in range(0, add_topic_count):

            try:
                print(nick + ': 添加话题 ' + ybtopic.topic(token, puid, group_id, channel_id).add(
                    getHitokoto(cat), getHitokoto(cat)) + fprint(i))
            except:
                print(nick + ': 添加话题时未获取到的错误' + fprint(i), traceback.format_exc())
            finally:
                wait()

        for i in range(0, vote_control_count):

            try:
                vote_id = ybvote.vote(token, puid, group_id).get(
                    vote_control_count)['data']['list'][i]['id']

                if vote:

                    try:
                        print(nick + ': 参与投票 ' + str(ybvote.go(token, puid, group_id, actor_id,
                                                               vote_id, 0, 0).vote(auto=True)) + fprint(i))
                    except:
                        print(nick + ': 参与投票时未获取到的错误' + fprint(i), traceback.format_exc())
                    finally:
                        wait()

                if vote_up:

                    try:
                        print(nick + ': 点赞投票 ' + ybvote.go(token, puid, group_id, actor_id,
                                                           vote_id, 0, 0).up() + fprint(i))
                    except:
                        print(nick + ': 点赞投票时未获取到的错误' + fprint(i), traceback.format_exc())
                    finally:
                        wait()

                for j in range(0, vote_reply_count):

                    try:
                        print(nick + ': 添加投票评论 ' + ybvote.go(token, puid, group_id, actor_id,
                                                             vote_id, 0, 0).reply(getHitokoto(cat), 0, 0) + fprint(j))
                    except:
                        print(nick + ': 添加投票评论时未获取到的错误' + fprint(j), traceback.format_exc())
                    finally:
                        wait()

            except:
                print(nick + ': 获取投票列表时未获取到的错误' + fprint(i), traceback.format_exc())
            finally:
                wait()

        for i in range(0, topic_control_count):

            try:
                article_id = ybtopic.topic(token, puid, group_id, channel_id).get(topic_control_count)[
                    'data']['list'][i]['id']

                if topic_up:

                    try:
                        print(nick + ': 点赞话题 ' + ybtopic.topic(token, puid,
                                                               group_id, channel_id).up(article_id) + fprint(i))
                    except:
                        print(nick + ': 点赞话题时未获取到的错误' + fprint(i), traceback.format_exc())
                    finally:
                        wait()

                for j in range(0, topic_reply_count):

                    try:
                        print(nick + ': 添加话题评论 ' + ybtopic.topic(token, puid,
                                                                 group_id, channel_id).reply(article_id, getHitokoto(cat)) + fprint(j))
                    except:
                        print(nick + ': 添加话题评论时未获取到的错误' + fprint(j), traceback.format_exc())
                    finally:
                        wait()

            except:
                print(nick + ': 获取话题列表时未获取到的错误' + fprint(i), traceback.format_exc())
            finally:
                wait()

    except:
        print(USERNAME + ': 无法连接服务器或密码错误，请先在 www.yiban.cn 登陆一次后重试。', traceback.format_exc())
    finally:
        wait()
