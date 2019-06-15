#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from pexpect import pxssh
from pexpect import spawn
import getpass
try:
    s = pxssh.pxssh()
    hostname = 'rsg.centos.aliyun'
    username = 'root'
    # password = getpass.getpass('password: ')
    s.login(hostname, username)
    s.sendline('sh test.sh')   # run a command
    s.expect(r'yes/no:\s+')
    s.sendline('yes')

    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    sftp = spawn('sftp root@rsg.centos.aliyun')
    sftp.expect('.*sftp>')
    sftp.sendline('put /Users/renshangui/commitizen.json /root/commitizen.json')
    s.sendline('ls -l')
    s.prompt()
    print(s.before)
    s.sendline('df')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)