#!/usr/bin/env python3
# coding=utf-8
import requests as r
from .yblogin import BASEURL


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
                           cookies=self.token, data=payload, timeout=10)
        return Add_Topic.json()['message']

    '''
    获取话题 <- 正则
    '''

    def get(self, size=0, page=0, Sections_id=-1, need_notice=0, my=0):
        tmp = []
        for i in range(1, (size//10) + 2): # Extend json list to control size
            payload = {
                'channel_id': self.channel_id,
                'puid': self.puid,
                'group_id': self.group_id,
                'page': i, # Should be 0 originally, work as disable page parse
                'size': 10, # Stick to 10 by stupid dev working yiban
                'orderby': 'updateTime',
                'Sections_id': Sections_id,
                'need_notice': need_notice,
                'my': my
            }

            Get_Topic = r.post(BASEURL + 'forum/article/listAjax',
                            cookies=self.token, data=payload, timeout=10)
            tmp.extend(Get_Topic.json()["data"]["list"])
        return tmp # Return larger list, the overflowing lists could be droped by function.

    '''
    获取评论
    '''

    def list(self, article_id, size=0):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id,
            'page': 0,
            'size': size,
            'order': 1
        }

        Get_List = r.post(BASEURL + 'forum/reply/listAjax',
                          cookies=self.token, data=payload, timeout=10)
        return Get_List.json()

    '''
    评论话题
    '''

    def reply(self, article_id, content, reply_id=0, syncFeed=0, isAnonymous=0):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id,
            'content': content,
            'reply_id': reply_id,
            'syncFeed': syncFeed,
            'isAnonymous': isAnonymous
        }

        Go_Topic = r.post(BASEURL + 'forum/reply/addAjax',
                          cookies=self.token, data=payload, timeout=10)
        return Go_Topic.json()['message']

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
                          cookies=self.token, data=payload, timeout=10)
        return Up_Topic.json()['message']

    '''
    取消点赞话题
    '''

    def down(self, article_id):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id
        }

        Down_Topic = r.post(BASEURL + 'forum/article/upDelArticleAjax',
                            cookies=self.token, data=payload, timeout=10)
        return Down_Topic.json()['message']

    '''
    删除评论
    '''

    def remove(self, article_id, reply_id):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id': article_id,
            'reply_id': reply_id
        }

        Remove_Reply = r.post(BASEURL + 'forum/reply/removeAjax',
                              cookies=self.token, data=payload, timeout=10)
        return Remove_Reply.json()['message']

    '''
    删除话题
    '''

    def delete(self, article_id):

        payload = {
            'channel_id': self.channel_id,
            'puid': self.puid,
            'article_id_list': article_id,
        }

        Delete_Topic = r.post(BASEURL + 'forum/article/setDelAjax',
                              cookies=self.token, data=payload, timeout=10)
        return Delete_Topic.json()['message']
