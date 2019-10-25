# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class LCGRand:

    slope = 7 ** 5
    congruence_class = 2 ** 32 - 1

    def __init__(self, seed):
        self._hidden_state = seed

    def rand(self):

        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        pass


class RandIter:
    def __init__(self, random_number_generator, length):
        pass

    def __iter__(self):
        pass
    
    def __next__(self):
        pass


if __name__ == '__main__':
    pass
