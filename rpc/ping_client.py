# -*-utf8-*-
import json
import logging
import time

import pika

from connect import connect
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def ping_callback(channel, method, header, body):
    logger.info("received ping reply.")
    logger.info(body)
    channel.stop_consuming()


def main():
    channel = connect()

    channel.exchange_declare("rpc", "direct")
    channel.queue_declare("ping")
    channel.queue_bind("ping", "rpc", "ping")

    tmp_queue = channel.queue_declare(exclusive=True, auto_delete=True)

    msg = json.dumps({"client_name": "RPC Client 1.0", "time": time.time()})
    msg_props = pika.BasicProperties()
    msg_props.reply_to = tmp_queue.method.queue

    channel.basic_publish(body=msg, exchange="rpc", properties=msg_props, routing_key="ping")
    channel.basic_consume(ping_callback, queue=tmp_queue.method.queue, consumer_tag=tmp_queue.method.queue)
    channel.start_consuming()


if __name__ == "__main__":
    main()
