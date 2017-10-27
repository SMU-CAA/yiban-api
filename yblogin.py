#!/usr/bin/env python3
# coding=utf-8
import re
import requests
from urllib import parse
from base64 import b64encode
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

BASEURL = 'https://www.yiban.cn/'

r = requests.Session()

'''
模拟 JSEncrypt 加密
加密方式为 PKCS1_v1_5
'''
def rsaEncrypt(password, key):

    cipher = PKCS1_v1_5.new(RSA.importKey(key))
    return b64encode(cipher.encrypt(password.encode()))

'''
易班登陆拿Token
参数: USERNAME, PASSWD
'''
def getUserToken(user, passwd):

    LOGIN_PAGE = BASEURL+'login'
    LOGIN_URL = BASEURL+'login/doLoginAjax'

    LoginPage = r.get(LOGIN_PAGE)
    RsaKey = re.search(r'data-keys=\'([\s\S]*?)\'',LoginPage.text).group(1)
    KeysTime = re.search(r'data-keys-time=\'(.*?)\'',LoginPage.text).group(1)
    Password = rsaEncrypt(passwd, RsaKey)

    data = {
        'account': user,
        'password': Password,
        'captcha': '',
        'keysTime': KeysTime,
        'is_rember': 1
    }
    
    LoginURL = r.post(LOGIN_URL, headers={'X-Requested-With': 'XMLHttpRequest'}, data=data)
    USERTOKEN = LoginURL.cookies['yiban_user_token']  # -> KeyError Exception
    r.close()
    return USERTOKEN

'''
获取群组信息
返回 JSON 字典
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
