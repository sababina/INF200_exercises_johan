# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class LCGRand:
    a = 7 ** 5
    b = 2 ** 31 - 1

    def __init__(self, seed):
        self._hidden_state = seed

    def rand(self):
        self._hidden_state = LCGRand.a * self._hidden_state % LCGRand.b

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError('Can not iterate through twice')

        self.num_generated_numbers = 0
        return self

    def __next__(self):
        if self.num_generated_numbers is None:
            raise RuntimeError(
                'Can not call ``next`` before the the iteration is started'
                )
        if self.num_generated_numbers == self.length:
            raise StopIteration
        number = self.generator.rand()
        self.num_generated_numbers += 1
        return number
