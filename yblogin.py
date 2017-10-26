#!/usr/bin/env python3
# coding=utf-8
import re
import requests
from urllib import parse
from base64 import b64encode
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

BASEURL = 'https://www.yiban.cn/'

'''
易班登陆拿Token
'''

def rsaEncrypt(password, key):

    cipher = PKCS1_v1_5.new(RSA.importKey(key))
    return b64encode(cipher.encrypt(password.encode()))

def getUserToken(user, passwd):

    LOGIN_PAGE = BASEURL+'login'
    LOGIN_URL = BASEURL+'login/doLoginAjax'

    r = requests.Session()
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
