#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return 'This is a test page.'


if __name__ == '__main__':
    app.run()
