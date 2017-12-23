#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.exchange_declare("first_fanout", exchange_type="fanout")

channel.queue_declare(queue="q_one")
channel.queue_declare(queue="q_two")
channel.queue_bind("q_one", exchange="first_fanout")
channel.queue_bind("q_two", exchange="first_fanout")

def main():
    while True:
        message = input("请发布消息: ")
        if message == "exit":
            break
        channel.basic_publish("first_fanout", routing_key='', body=message)

if __name__ == "__main__":
    main()