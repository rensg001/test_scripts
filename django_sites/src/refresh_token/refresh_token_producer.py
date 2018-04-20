#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import random
import string
import threading
import time

import pika

from redis import Redis

redis_client = Redis.from_url("redis://127.0.0.1/0")

app_id = "jdhdj63662"

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def gen_token():
    token = randomword(10)
    return "{token}:{expire}".format(token=token, expire=10)

def add_token_in_redis(token):
    """产生副作用"""
    key_name = "wxtoken"
    redis_client.rpush(key_name, token)

def setup_rabbitmq():
    conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = conn.channel()

    channel.exchange_declare("token_ex",
                             exchange_type="direct",
                             durable=True)

    channel.queue_declare("token_q", durable=True)

    channel.queue_bind("token_q", exchange="token_ex", routing_key="token")
    return conn, channel

def heart_beat(conn):
    while True:
        conn.process_data_events()
        time.sleep(30)

def main():
    conn, channel = setup_rabbitmq()
    heart_beat_thread = threading.Thread(target=heart_beat,
                                         args=(conn, ),
                                         daemon=True)
    heart_beat_thread.start()

    add_token_in_redis(gen_token())

    while True:
        token_item_tuple = redis_client.blpop("wxtoken")
        token_item = token_item_tuple[1].decode("utf8")
        print(token_item)
        token, expire = token_item.split(":")
        msg_props = pika.BasicProperties()
        msg_props.content_type = "text/plain"
        msg_props.delivery_mode = 2  # 持久化消息
        channel.basic_publish("token_ex",
                              routing_key="token",
                              body=token,
                              properties=msg_props)
        time.sleep(int(10))

if __name__ == "__main__":
    main()
