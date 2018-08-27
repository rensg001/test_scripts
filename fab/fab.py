#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from fabric import Connection

result = Connection('rsg.centos.aliyun', user='dev').run('uname -s', hide=True)

msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

print(msg.format(result))