#!/usr/bin/env python3
import re
import requests as r
from yblogin import getUserToken, BASEURL

USERNAME = ''
PASSWD = ''

'''
获取群组信息
'''
def getInfo(USERTOKEN):

    Get_Group_Info = r.get(BASEURL+'my/group/type/public', cookies=USERTOKEN)
    group_id = re.search(r'href="/newgroup/indexPub/group_id/(\d+)/puid/(\d+)"', Get_Group_Info.text).group(1)
    puid = re.search(r'href="/newgroup/indexPub/group_id/(\d+)/puid/(\d+)"', Get_Group_Info.text).group(2)
    payload = {
        'puid': puid,
        'group_id': group_id
    }
    Get_Channel_Info = r.post(BASEURL+'forum/api/getListAjax', cookies=USERTOKEN, data=payload)
    channel_id = Get_Channel_Info.json()['data']['channel_id']
    info = {
        'group_id': group_id,
        'puid': puid,
        'channel_id': channel_id
    }
    return info

yiban_user_token = getUserToken(USERNAME, PASSWD)
token = dict(yiban_user_token=yiban_user_token)
info = getInfo(token)
group_id = info['group_id']
puid = info['puid']
channel_id = info['channel_id']
actor_id = 13047896 # Public Account
