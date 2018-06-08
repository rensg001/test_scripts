#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time

import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:8888/websocket")
for i in range(10):
    ws.send("I am client A")
    print(ws.recv())

print(ws.recv())