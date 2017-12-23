#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pika

import time

from . import refresh_token_producer

def setup_rabbitmq():
    conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = conn.channel()

    channel.exchange_declare("token_ex",
                             exchange_type="direct",
                             durable=True)

    channel.queue_declare("token_q", durable=True)

    channel.queue_bind("token_q", exchange="token_ex", routing_key="token")
    return conn, channel

def token_handler(ch, method, properties, body):
    print("更新token:{token}....".format(token=body.decode("utf8")))
    time.sleep(3)
    new_token = refresh_token_producer.gen_token()
    refresh_token_producer.add_token_in_redis(new_token)
    print("更新完成,新token:{token}".format(token=new_token))
    ch.basic_ack(delivery_tag=method.delivery_tag)

conn, channel = setup_rabbitmq()

channel.basic_consume(token_handler, "token_q")
channel.start_consuming()
