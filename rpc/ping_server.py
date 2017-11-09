# -*-utf8-*-
import json
import logging

from connect import connect
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def api_ping(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    logger.info("received api call....replaying....")
    channel.basic_publish(body="Pong!" + str(msg_dict["time"]),
                          exchange="",
                          routing_key=header.reply_to)


def main():
    channel = connect()
    channel.exchange_declare("rpc", "direct")
    channel.queue_declare("ping")
    channel.queue_bind("ping", "rpc", "ping")

    channel.basic_consume(api_ping, queue="ping", consumer_tag="ping")

    channel.start_consuming()


if __name__ == '__main__':
    main()
