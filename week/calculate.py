#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import math

from datetime import timedelta
from datetime import date

def get_week(start_date, the_date):
    assert start_date <= the_date
    days = (7 - start_date.weekday())
    print(days)
    next_monday = start_date + timedelta(days=days)
    weeks = 1
    if next_monday > the_date:
        return weeks
    print(next_monday)

    days_interval = the_date - next_monday
    print(days_interval.days)
    the_day = (days_interval.days + 1)  # 自从next_monday的第几天
    weeks += math.ceil(the_day / 7)
    return weeks  # 加上start_date落在的那一周

weeks = get_week(date(2018, 1, 10), date(2018, 1, 28))

print(weeks)