#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


default = {
    'org': {
        'sub_org1': {},
        'sub_org2': {}
    }
}

org = default.setdefault('org', {})
print(org)