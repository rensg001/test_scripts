#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time
import os
import base64

import tornado.ioloop
import tornado.web

from tornado.websocket import WebSocketHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class EchoWebSocket(WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message("You said: " + message)
        setattr(self, "what_you_said", message)

        if getattr(self, "timeout_handle", None):
            tornado.ioloop.IOLoop.instance().remove_timeout(
                getattr(self, "timeout_handle")
            )
        timeout_handle = tornado.ioloop.IOLoop.instance().add_timeout(
            time.time() + 20,
            self.time_out
        )
        setattr(self, "timeout_handle", timeout_handle)

    def time_out(self):
        print("invoked time_out.")

        try:
            self.write_message(
                "Your last words are {message}".format(
                    message=getattr(self, "what_you_said", "")
                )
            )
        except:
            pass
        finally:
            self.close()

    def on_close(self):
        print("WebSocket closed")
        self.close()


class ImageHandler(WebSocketHandler):
    def open(self):
        app_dir = os.path.dirname(os.path.abspath(__file__))
        setattr(self, "image_dir", os.path.join(app_dir, "images"))

    def on_message(self, message):
        if message == "image":
            image_path = os.path.join(getattr(self, "image_dir"), "mountain.jpeg")
            with open(image_path, "rb") as image:
                image_content = image.read()
                image_content = base64.b64encode(image_content)
                self.write_message(image_content)

    def on_close(self):
        self.close()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket$", EchoWebSocket),
        (r"/websocket/image$", ImageHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
