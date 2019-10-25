# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class LCGRand:

    a = 7 ** 5
    m = 2 ** 32 - 1

    def __init__(self, seed):
        self.previous = seed

    def rand(self):

        random = (LCGRand.a * self.previous) % LCGRand.m
        self.previous = random

        return random


class RandIter:
    def __init__(self, random_number_generator, length):
        pass

    def __iter__(self):
        pass
    
    def __next__(self):
        pass

