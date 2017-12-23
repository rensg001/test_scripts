#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import json

import requests
import redis

from wechat.views import ttl_client

# redis_client = redis.from_url('redis://127.0.0.1/0')


def get_access_token_key(key):
    return 'wechat:{app_id}_access_token'.format(app_id=key)


def get_refresh_token_key(key):
    return 'wechat:{app_id}_refresh_token'.format(app_id=key)


app_id = 'wx5b8908a1214e2349'
app_secret = '0581a2d10e69a7d6258db9f1001306f1'


def get_token():
    # url_base = 'https://api.weixin.qq.com/cgi-bin/token'
    # query_params = 'grant_type=client_credential&appid={APPID}&secret={APPSECRET}'
    # query_params = query_params.format(APPID=app_id, APPSECRET=app_secret)
    # url = '?'.join([url_base, query_params])
    #
    # resp = requests.get(url)
    # result = resp.json()

    ttl_client.fetch_access_token()
    # client.set(get_access_token_key(app_id),
    #            result['access_token'],
    #            result['expires_in'])
    # redis_client.set(get_refresh_token_key(app_id), result['refresh_token'],
    #                  ex=result['expires_in'])


def create_menu():
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={ACCESS_TOKEN}'
    access_token = ttl_client.get(get_access_token_key(app_id))
    url = url.format(
        ACCESS_TOKEN=access_token.decode('utf8'))
    menu_data = {
        "button": [
            {
                "type": "click",
                "name": "中文歌曲",
                "key": "V1001_TODAY_MUSIC"
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    # proxies = {
    #     "http": "http://127.0.0.1:8890",
    #     "https": "http://127.0.0.1:8890",
    # }
    # print(urlencode(menu_data))
    resp = requests.post(url,
                         data=json.dumps(menu_data, ensure_ascii=False),
                         headers=headers)
    print(resp.content)


if __name__ == '__main__':
    get_token()
    create_menu()
