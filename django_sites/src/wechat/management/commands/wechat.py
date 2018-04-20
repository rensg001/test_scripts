# -*- coding: utf-8 -*-

import json
import ssl

from urllib import request
from urllib import parse

from django.core.management import BaseCommand
from wechatpy import WeChatClient
from wechatpy.session.redisstorage import RedisStorage
from redis import Redis

redis_client = Redis.from_url('redis://127.0.0.1:6379/0')
session_interface = RedisStorage(
    redis_client,
    prefix="wechatpy"
)
client = WeChatClient('wx5b8908a1214e2349', '0581a2d10e69a7d6258db9f1001306f1', session=session_interface)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def handle(self, *args, **options):
    #     client.menu.create({
    #         "button": [
    #             {
    #                 "type": "click",
    #                 "name": u"今日歌曲",
    #                 "key": "V1001_TODAY_MUSIC"
    #             },
    #             {
    #                 "type": "click",
    #                 "name": u"歌手简介",
    #                 "key": "V1001_TODAY_SINGER"
    #             },
    #             {
    #                 "name": u"菜单",
    #                 "sub_button": [
    #                     {
    #                         "type": "view",
    #                         "name": u"搜索",
    #                         "url": "http://www.soso.com/"
    #                     },
    #                     {
    #                         "type": "view",
    #                         "name": u"视频",
    #                         "url": "http://v.qq.com/"
    #                     },
    #                     {
    #                         "type": "click",
    #                         "name": u"赞一下我们",
    #                         "key": "V1001_GOOD"
    #                     }
    #                 ]
    #             }
    #         ]
    #     })

    def handle(self, *args, **options):
        access_token = client.access_token
        uri = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
        query = {"access_token": access_token}
        params = {
            "touser": "oYMMm0yAoDBwY81Fw3w39T9Bu0KI",
            "template_id": "foH6nFW6D_KjKjOwuQdN7E5_-SsrIaAs4UJlwZjKpxI",
            "url": "http://weixin.qq.com/download",
            "data": {
                "one": {
                    "value": "恭喜你购买成功！",
                    "color": "#173177"
                }
            }
        }
        headers = {"Content-Type": "application/json"}
        encoded_query = parse.urlencode(query)
        url = ''.join([uri, '?', encoded_query])
        body_str = json.dumps(params)
        body = body_str.encode('utf8')

        r = request.Request(url, body, headers)
        # r.set_proxy("127.0.0.1:8890", "https")
        context = ssl._create_unverified_context()
        resp = request.urlopen(r, cafile="/Users/renshangui/certificates2.cer")
        print(resp.read())
