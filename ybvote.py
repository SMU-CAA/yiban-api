#!/usr/bin/env python3
import re
import json
import requests as r
from ybutils import group_id, puid, channel_id, actor_id
from yblogin import BASEURL

class vote:

    def __init__(self, USERTOKEN):
        self.USERTOKEN = USERTOKEN

    '''
    易班发起投票
    标题，正文，选项1，选项2
    '''
    def add(self, title, subjectTxt, subjectTxt_1, subjectTxt_2):
        payload = {
            'puid': puid,
            'group_id': group_id,
            'scope_ids': group_id,
            'title': title,
            'subjectTxt': subjectTxt,
            'subjectPic': '',
            'options_num': 2,
            'scopeMin': 1,
            'scopeMax': 1,
            'minimum': 1,
            'voteValue': '2018-03-17 22:00',
            'voteKey': 2,
            'public_type': 0,
            'isAnonymous': 1,
            'istop': 1,
            'sysnotice': 2,
            'isshare': 1,
            'subjectTxt_1': subjectTxt_1,
            'subjectTxt_2': subjectTxt_2,
            'rsa': 1,
            'dom': '.js-submit'
        }
        Add_Vote = r.post(BASEURL+'vote/vote/add',
                          cookies=self.USERTOKEN, data=payload)
        return Add_Vote.json()['code']

    '''
    获取投票 <- 正则
    '''
    def get(self):
        payload = {
            'puid': puid,
            'group_id': group_id,
            'page': 0,
            'size': 0,
            'status': 1,
            'sort': 1,
            'time': 0
        }
        Get_Vote = r.post(BASEURL+'vote/index/getVoteList',
                          cookies=self.USERTOKEN, data=payload)
        return Get_Vote.json()

class go:

    '''
    准备投票参数
    '''
    def __init__(self, USERTOKEN, vote_id):
        self.USERTOKEN = USERTOKEN
        self.vote_id = vote_id
        self.Get_Token = r.get(BASEURL+'vote/vote/showDetail/vote_id/'+str(vote_id)+'/puid/'+puid+'/group_id/'+group_id, cookies=self.USERTOKEN)
        self.vote_token = re.search(r'g_config.token = "(.*)"', self.Get_Token.text).group(1)
        payload = {
            'vote_id': vote_id,
            'uid': actor_id,
            'puid': puid,
            'pagetype': 1,
            'group_id': group_id,
            'actor_id': actor_id,
            'token': self.vote_token,
            'isSchoolVerify': 1,
            'isLogin': 1,
            'isOrganization': 0,
            'ispublic': 0
        }
        self.Get_Vote_Detail = r.post(BASEURL+'vote/vote/getVoteDetail', cookies=self.USERTOKEN, data=payload)
        self.voptions_id = self.Get_Vote_Detail.json()['data']['option_list'][0]['id']
        self.mount_id = self.Get_Vote_Detail.json()['data']['vote_list']['Mount_id']

    '''
    参与投票
    '''
    def vote(self):
        
        payload = {
            'puid': puid,
            'group_id': group_id,
            'vote_id': self.vote_id,
            'voptions_id': self.voptions_id,
            'minimum': 1,
            'scopeMax': 1
        }
        Go_Vote = r.post(BASEURL+'vote/vote/act',
                        cookies=self.USERTOKEN, data=payload) # Multiple Choice Vote
        return Go_Vote.json()['code']

    '''
    评论投票
    '''
    def reply(self, content):
        
        payload = {
            'mountid': self.mount_id,
            'msg': content,
            'group_id':group_id,
            'actor_id':actor_id,
            'vote_id':self.vote_id,
            'author_id':actor_id,
            'puid':puid,
            'reply_comment_id':0,
            'reply_user_id':0
        }
        Go_Vote_Reply = r.post(BASEURL+'vote/vote/addComment',
                        cookies=self.USERTOKEN, data=payload)
        return Go_Vote_Reply.json()['code']
