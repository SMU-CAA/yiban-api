#!/usr/bin/env python3
import re
import json
import requests
import ybvote
import ybtopic
from ybutils import token, group_id, puid, channel_id, actor_id
from yblogin import BASEURL

r = requests.Session()

'''
获取 EPGA 数值信息
'''
def getEPGA(USERTOKEN):
    Get_EPGA = r.get(BASEURL+'newgroup/indexPub/group_id/' +
                     group_id + '/puid/' + puid, cookies=USERTOKEN)
    EPGA = re.search(r'EGPA：[0-9\.]*', Get_EPGA.text)
    return EPGA.group()

print(getEPGA(token))

# --Test--
#print(ybvote.vote(token).get())
#print(ybvote.go(token,19955713).reply('test'))
#print(ybtopic.topic(token).get())
