#!/usr/bin/env python3
# coding=utf-8
import re
import time
import requests as r
from .yblogin import BASEURL


class vote:

    def __init__(self, token, puid, group_id):

        self.token = token
        self.puid = puid
        self.group_id = group_id

    '''
    易班发起单选双项投票
    参数: 标题, 正文, 选项1, 选项2
    '''

    def add(self, title, subjectTxt, subjectTxt_1, subjectTxt_2, subjectPic=None, voteValue=1893427200, public_type=0, isAnonymous=0, istop=1, sysnotice=2, isshare=1):

        payload = {
            'puid': self.puid,
            'group_id': self.group_id,
            'scope_ids': self.group_id,
            'title': title,
            'subjectTxt': subjectTxt,
            'subjectPic': subjectPic,
            'options_num': 2,
            'scopeMin': 1,
            'scopeMax': 1,
            'minimum': 1,
            'voteValue': time.strftime("%Y-%m-%d %H:%M", time.localtime(voteValue)),
            'voteKey': 2,
            'public_type': public_type,
            'isAnonymous': isAnonymous,
            "voteIsCaptcha": 0,
            'istop': istop,
            'sysnotice': sysnotice,
            'isshare': isshare,
            'subjectTxt_1': subjectTxt_1,
            'subjectTxt_2': subjectTxt_2,
            'rsa': 1,
            'dom': '.js-submit'
        }

        Add_Vote = r.post(BASEURL + 'vote/vote/add',
                          cookies=self.token, data=payload, timeout=10)
        return Add_Vote.json()['message']

    '''
    获取投票
    返回 JSON 字典
    '''

    def get(self, size=10, page=0, status=1, sort=1, time=0):

        payload = {
            'puid': self.puid,
            'group_id': self.group_id,
            'page': page,
            'size': size,
            'status': status,
            'sort': sort,
            'time': time
        }

        Get_Vote = r.post(BASEURL + 'vote/index/getVoteList',
                          cookies=self.token, data=payload, timeout=10)
        return Get_Vote.json()["data"]["list"]


class go:

    '''
    准备投票参数
    参数: token, vote_id
    '''

    def __init__(self, token, puid, group_id, actor_id, vote_id, isOrganization=0, ispublic=0):

        self.token = token
        self.puid = puid
        self.group_id = group_id
        self.actor_id = actor_id
        self.vote_id = vote_id
        self.isOrganization = isOrganization
        self.ispublic = ispublic
        self.Get_Token = r.get(BASEURL + 'vote/vote/showDetail/vote_id/' + str(
            vote_id) + '/puid/' + self.puid + '/group_id/' + self.group_id, cookies=self.token, timeout=10)
        self.vote_token = re.search(
            r'g_config.token = "(.*)"', self.Get_Token.text).group(1)

        payload = {
            'vote_id': vote_id,
            'uid': self.actor_id,
            'puid': self.puid,
            'pagetype': 1,
            'group_id': self.group_id,
            'actor_id': self.actor_id,
            'token': self.vote_token,
            'isSchoolVerify': 1,
            'isLogin': 1,
            'isOrganization': isOrganization,
            'ispublic': ispublic
        }

        self.Get_Vote_Detail = r.post(
            BASEURL + 'vote/vote/getVoteDetail', cookies=self.token, data=payload, timeout=10)

        self.mount_id = self.Get_Vote_Detail.json(
        )['data']['vote_list']['Mount_id']

    '''
    参与单选投票
    '''

    def vote(self, auto=False, choice=0):

        if auto:
            vote_data = self.Get_Vote_Detail.json()['data']
            minimum = vote_data['vote_list']['minimum']
            scopemax = vote_data['vote_list']['scopeMax']
            voptions_id = []

            for i in range(0, int(minimum)):
                voptions_id.append(vote_data['option_list'][i]['id'])

            payload = {
                'puid': self.puid,
                'group_id': self.group_id,
                'vote_id': self.vote_id,
                'voptions_id': ','.join(voptions_id),
                'minimum': minimum,
                'scopeMax': scopemax
            }

        else:
            voptions_id = self.Get_Vote_Detail.json(
            )['data']['option_list'][choice]['id']

            payload = {
                'puid': self.puid,
                'group_id': self.group_id,
                'vote_id': self.vote_id,
                'voptions_id': voptions_id,
                'minimum': 1,
                'scopeMax': 1
            }

        Go_Vote = r.post(BASEURL + 'vote/vote/act',
                         cookies=self.token, data=payload, timeout=10)
        return Go_Vote.json()['message']

    '''
    评论投票
    参数: 正文
    '''

    def reply(self, content, comment_id=0, user_id=0):

        payload = {
            'mountid': self.mount_id,
            'msg': content,
            'group_id': self.group_id,
            'actor_id': self.actor_id,
            'vote_id': self.vote_id,
            'author_id': self.actor_id,
            'puid': self.puid,
            'reply_comment_id': comment_id,
            'reply_user_id': user_id
        }

        Go_Vote_Reply = r.post(BASEURL + 'vote/vote/addComment',
                               cookies=self.token, data=payload, timeout=10)
        return Go_Vote_Reply.json()['message']

    '''
    删除评论
    '''

    def remove(self, content, comment_id, user_id=0):

        payload = {
            'mountid': self.mount_id,
            'commentid': comment_id,
            'puid': self.puid,
            'group_id': self.group_id,
            'author_id': self.actor_id,
            'comment_author_id': self.actor_id,
            'reply_name': 'noname',
            'vote_id': self.vote_id
        }

        Del_Vote_Reply = r.post(BASEURL + 'vote/vote/addComment',
                                cookies=self.token, data=payload, timeout=10)
        return Del_Vote_Reply.json()['message']

    '''
    点赞投票
    '''

    def up(self):

        payload = {
            'group_id': self.group_id,
            'puid': self.puid,
            'vote_id': self.vote_id,
            'actor_id': self.actor_id,
            'flag': 1
        }

        Up_Vote = r.post(BASEURL + 'vote/vote/editLove',
                         cookies=self.token, data=payload, timeout=10)
        return Up_Vote.json()['message']

    '''
    取消点赞投票
    '''

    def down(self):

        payload = {
            'group_id': self.group_id,
            'puid': self.puid,
            'vote_id': self.vote_id,
            'actor_id': self.actor_id,
            'flag': 0
        }

        Down_Vote = r.post(BASEURL + 'vote/vote/editLove',
                           cookies=self.token, data=payload, timeout=10)
        return Down_Vote.json()['message']

    '''
    删除投票
    '''

    def delete(self):

        payload = {
            'group_id': self.group_id,
            'puid': self.puid,
            'vote_id': self.vote_id
        }

        Delete_Vote = r.post(BASEURL + 'vote/Expand/delVote',
                             cookies=self.token, data=payload, timeout=10)
        return Delete_Vote.json()['message']
