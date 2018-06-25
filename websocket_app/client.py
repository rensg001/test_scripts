#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import base64

import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:8888/websocket/image")
ws.send("image")
b64_image_content = ws.recv()

image_content = base64.b64decode(b64_image_content)

with open("mountain2.jpeg", "wb") as image:
    image.write(image_content)