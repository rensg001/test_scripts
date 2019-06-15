#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import threading


class Buff(object):
    MAX_BUFF_LEN = 10

    def __init__(self):
        self._buff = [None for i in range(0, self.MAX_BUFF_LEN)]
        self._producer_point = 0
        self._consumer_point = 0

    def produce(self, value):
        self._buff[self._producer_point % self.MAX_BUFF_LEN] = value
        self._producer_point += 1

    def consume(self):
        value = self._buff[self._consumer_point % self.MAX_BUFF_LEN]
        self._consumer_point += 1
        return value

    @property
    def max_buff_len(self):
        return self.MAX_BUFF_LEN


class Repository(object):
    MAX_PRODUCE_NUM = 200

    def __init__(self):
        self._buff = Buff()
        self._mutex = threading.Semaphore()
        self._nempty = threading.Semaphore(self._buff.max_buff_len)
        self._nstored = threading.Semaphore(0)

    def produce(self):
        for i in range(0, self.MAX_PRODUCE_NUM):
            self._nempty.acquire()
            self._mutex.acquire()
            self._buff.produce(i)
            self._mutex.release()
            self._nstored.release()

    def consume(self):
        for i in range(0, self.MAX_PRODUCE_NUM):
            self._nstored.acquire()
            self._mutex.acquire()
            print(self._buff.consume())
            self._mutex.release()
            self._nempty.release()


class Runner(object):
    def __init__(self):
        self._repository = Repository()

    def run(self):
        producer = threading.Thread(
            target=self._repository.produce, name='producer'
        )
        consumer = threading.Thread(
            target=self._repository.consume, name='consumer'
        )
        producer.start()
        consumer.start()

        producer.join()
        consumer.join()


if __name__ == '__main__':
    runner = Runner()
    runner.run()
