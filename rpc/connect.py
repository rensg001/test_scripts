# -*-utf8-*-
import pika


def connect():
    credentials = pika.PlainCredentials("guest", "guest")
    conn_params = pika.ConnectionParameters("127.0.0.1", credentials=credentials)
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()
    return channel
