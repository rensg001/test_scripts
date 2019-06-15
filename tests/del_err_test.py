#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from __future__ import print_function



class Robot:
    population = 0  # class variable, number of robots

    def __init__(self, name):

        self.name = name
        print('(initializing %s)' % self.name)

        Robot.population += 1

    def __del__(self):
        print('%s is being destroyed!' % self.name)
        print('pre1 %s type %s' % (Robot, type(Robot)))
        Robot.population -= 1

        print('pre2')
        if Robot.population == 0:
            print('%s was the last one.' % self.name)
        else:
            print('there are still %d robots working.' % Robot.population)

    def sayHi(self):
        print('%s says hi' % self.name)

    def howMany():
        print('there are %d robots' % Robot.population)

    howMany = staticmethod(howMany)


# instantiate 2 robots
mingos = Robot('alvergas')
mingos.sayHi()
Robot.howMany()
del mingos
print('end program')