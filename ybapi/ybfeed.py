#!/usr/bin/env python3
# coding=utf-8
import requests as r
from .yblogin import BASEURL


class feed:

    def __init__(self, token):

        self.token = token

    '''
    发起动态
    '''

    def add(self, content, privacy_level):

        payload = {
            'content': content,
            'privacy': privacy_level,
            'dom': '.js-submit'
        }

        Add_Feed = r.post(BASEURL + 'feed/add',
                          cookies=self.token, data=payload, timeout=10)
        return Add_Feed.json()['message']

    '''
    获取动态列表
    '''

    def get(self, num=0):

        payload = {
            'num': num,
            'topic_content': '',
            'scroll': 1
        }

        Get_Feed = r.post(BASEURL + 'feed/list',
                          cookies=self.token, data=payload, timeout=10)
        return Get_Feed.json()

    '''
    点赞
    '''

    def up(self, feed_id):

        payload = {
            'id': feed_id
        }

        UP_Feed = r.post(BASEURL + 'feed/up', cookies=self.token, data=payload, timeout=10)
        return UP_Feed.json()['message']

    '''
    同情
    '''

    def down(self, feed_id):

        payload = {
            'id': feed_id
        }

        Down_Feed = r.post(BASEURL + 'feed/down',
                           cookies=self.token, data=payload, timeout=10)
        return Down_Feed.json()['message']

    def delete(self, feed_id):

        payload = {
            'id': feed_id
        }

        Delete_Feed = r.post(BASEURL + 'feed/delete',
                             cookies=self.token, data=payload, timeout=10)
        return Delete_Feed.json()['message']
