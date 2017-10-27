#!/usr/bin/env python3
# coding=utf-8
import requests as r
from ybutils import group_id, puid, channel_id
from yblogin import BASEURL

class topic:

    def __init__(self, USERTOKEN):

        self.USERTOKEN = USERTOKEN

    '''
    易班发起话题
    '''
    def add(self, title, content):

        payload = {
            'puid': puid,
            'pubArea': group_id,
            'title': title,
            'content': content,
            'isNotice': 'false',
            'dom': '.js-submit'
        }

        Add_Topic = r.post(BASEURL+'forum/article/addAjax',
                        cookies=self.USERTOKEN, data=payload)
        return Add_Topic.json()['code']

    '''
    获取话题 <- 正则
    '''
    def get(self):

        payload = {
            'channel_id': channel_id,
            'puid': puid,
            'group_id': group_id,
            'page': 0,
            'size': 0,
            'orderby': 'updateTime',
            'Sections_id': -1,
            'need_notice': 0,
            'my': 0
        }

        Get_Topic = r.post(BASEURL+'forum/article/listAjax',
                        cookies=self.USERTOKEN, data=payload)
        return Get_Topic.json()

    '''
    评论话题
    '''
    def go(self, article_id, content):

        payload = {
            'channel_id': channel_id,
            'puid': puid,
            'article_id': article_id,
            'content': content,
            'reply_id': 0,
            'syncFeed': 0,
            'isAnonymous': 0
        }

        Go_Topic = r.post(BASEURL+'forum/reply/addAjax',
                        cookies=self.USERTOKEN, data=payload)
        return Go_Topic.json()['code']

    '''
    点赞话题
    '''
    def up(self, article_id):

        payload = {
            'channel_id': channel_id,
            'puid': puid,
            'article_id': article_id
        }
        
        Up_Topic = r.post(BASEURL+'forum/article/upArticleAjax',
                        cookies=self.USERTOKEN, data=payload)
        return Up_Topic.json()['code']
