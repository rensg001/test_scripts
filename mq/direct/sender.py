#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import threading

import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.exchange_declare("first_direct", exchange_type="direct")

channel.queue_declare("direct_q")

channel.queue_bind("direct_q", exchange="first_direct", routing_key="nimei")

def heart_beat():
    while True:
        conn.process_data_events()
        time.sleep(30)

def main():
    heart_beat_thread = threading.Thread(target=heart_beat, daemon=True)
    heart_beat_thread.start()

    while True:
        message = input("请发布消息: ")
        if message == "exit":
            break
        channel.basic_publish("first_direct",
                              routing_key='nimei',
                              body=message)

if __name__ == "__main__":
    main()