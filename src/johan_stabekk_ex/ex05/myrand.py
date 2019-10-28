# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class LCGRand:
    a = 7 ** 5
    b = 2 ** 32 - 1

    def __init__(self, seed):
        self._hidden_state = seed

    def rand(self):
        self._hidden_state = LCGRand.a * self._hidden_state % LCGRand.b

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self.rand(), length)
        pass

    def infinite_random_sequence(self):
        while True:
            yield self.rand()
        pass


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
        number = self.generator
        self.num_generated_numbers += 1
        return number


if __name__ == '__main__':
    generator = LCGRand(3)
    for rand in generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
