#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from __future__ import print_function

from fabric import Connection
from fabric import task
import fabric

# result = Connection('rsg.centos.aliyun', user='root').run('uname -s', hide=True)
#
# msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
#
# print(msg.format(result))

@task(optional=['count'])
def test(c, count=1):
    with Connection('rsg.centos.aliyun', user='root') as c:
        # result = c.run('sh test.sh',)
        print("count: {}".format(count))