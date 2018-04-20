# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.core.cache import caches
from wechatpy.messages import TextMessage

from wechatpy.replies import TextReply
from wechatpy import parse_message, WeChatClient
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.oauth import WeChatOAuth
from .session_storage import DatabaseStorage

# Create your views here.

logger = logging.getLogger(__name__)


session_interface = DatabaseStorage(caches['default'])

user_open_id = []
app_id = 'wx5b8908a1214e2349'
app_secrete = '0581a2d10e69a7d6258db9f1001306f1'

client = WeChatClient(app_id, app_secrete, session=session_interface)

class TTLWechatClient(WeChatClient):

    def get_ttl(self, key):
        return self.session.get_ttl(key)

ttl_client = TTLWechatClient(app_id, app_secrete, session=session_interface)




class TestView(View):
    """微信回调接口"""

    token = 'test_token'

    def get(self, request):
        """回调接口验证"""

        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        try:
            check_signature(self.token, signature, timestamp, nonce)
        except InvalidSignatureException:
            logger.warn('InvalidSignatureException')
            raise
        else:
            return HttpResponse(echostr)

    def post(self, request):
        """处理消息"""

        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        try:
            check_signature(self.token, signature, timestamp, nonce)
        except InvalidSignatureException:
            logger.warn('InvalidSignatureException')
            raise

        msg = parse_message(request.body)
        user_open_id.append(msg.source)
        logger.info('user_open_ids: %s' % user_open_id)
        if isinstance(msg, TextMessage):
            logger.info('text message.')

        reply = TextReply(content='text reply', message=msg)
        # 转换成 XML
        xml = reply.render()
        return HttpResponse(xml)


class AuthTestView(View):
    """测试授权"""

    def get(self, request):
        next_page = request.GET.get('next')
        state = request.GET.get('state')
        auth_code = request.GET.get('code')
        wx_oauth = WeChatOAuth(app_id, app_secrete, redirect_uri=next_page, scope='snsapi_base', state='fuck')

        logger.info('state %s' % state)

        if next_page and not auth_code:
            logger.info('authorize url %s' % wx_oauth.authorize_url)
            return HttpResponseRedirect(wx_oauth.authorize_url)
        if auth_code:
            logger.info('auth code %s' % auth_code)
            result = wx_oauth.fetch_access_token(auth_code)
            open_id = result['openid']
            access_token = result['access_token']
            logger.info('openid %s, access token %s' % (open_id, access_token))

            resp = client.message.send_template(
                        user_id=open_id,
                        template_id=u"foH6nFW6D_KjKjOwuQdN7E5_-SsrIaAs4UJlwZjKpxI",
                        data={
                            u"one": {
                                u"value": u"你好啊！"
                            }
                        },
                    )
            return HttpResponse(b'heheda')
