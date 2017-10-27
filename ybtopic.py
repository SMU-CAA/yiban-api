#!/usr/bin/env python3
# coding=utf-8
import requests as r
from yblogin import BASEURL


class topic:

    def __init__(self, token, puid, group_id, channel_id):

        self.token = token
        self.puid = puid
        self.group_id = group_id
        self.channel_id = channel_id

    '''
    易班发起话题
    '''

    def add(self, title, content):

        payload = {
            'puid': self.puid,
            'pubArea': self.group_id,
            'title': title,
            'content': content,
            'isNotice': 'false',
            'dom': '.js-submit'
        }

        Add_Topic = r.post(BASEURL + 'forum/article/addAjax',
                           cookies=self.token, data=payload)
        return Add_Topic.json()['code']

    '''
    获取话题 <- 正则
    '''

    def get(self):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'group_id': self.group_id,
            'page': 0,
            'size': 0,
            'orderby': 'updateTime',
            'Sections_id': -1,
            'need_notice': 0,
            'my': 0
        }

        Get_Topic = r.post(BASEURL + 'forum/article/listAjax',
                           cookies=self.token, data=payload)
        return Get_Topic.json()

    '''
    评论话题
    '''

    def go(self, article_id, content):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id,
            'content': content,
            'reply_id': 0,
            'syncFeed': 0,
            'isAnonymous': 0
        }

        Go_Topic = r.post(BASEURL + 'forum/reply/addAjax',
                          cookies=self.token, data=payload)
        return Go_Topic.json()['code']

    '''
    点赞话题
    '''

    def up(self, article_id):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id
        }

        Up_Topic = r.post(BASEURL + 'forum/article/upArticleAjax',
                          cookies=self.token, data=payload)
        return Up_Topic.json()['code']
