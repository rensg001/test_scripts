#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time
from datetime import datetime

class People(object):
    def __init__(self, gender):
        self._gender = gender

    def wear_clothes(self, clothes):
        raise NotImplemented()

    @property
    def gender(self):
        return self._gender


class Model(People):
    def wear_clothes(self, clothes):
        return self.gender + clothes


class ModelFactory(object):
    Pool = {}

    @classmethod
    def create(cls, gender):
        if gender in cls.Pool:
            return cls.Pool.get(gender)
        else:
            model = Model(gender)
            cls.Pool[gender] = model
            return model

class ModelManager(object):
    FitingRoom = {}

    def add(self, gender, clothes, _id):
        model = ModelFactory.create(gender)
        self.FitingRoom[_id] = {"model": model, "clothes": clothes}

    def wear(self):
        for key, value in self.FitingRoom.items():
            value["model"].wear_clothes(value["clothes"])

if __name__ == "__main__":
    print(datetime.fromtimestamp(time.time()))
    model_manager = ModelManager()
    for i in range(50000):
        model_manager.add("male" if i % 2 else "female", "第"+str(i)+"衣服", i)
    model_manager.wear()
    print(datetime.fromtimestamp(time.time()))