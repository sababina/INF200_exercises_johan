# -*- coding: utf-8 -*-


__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class LCGRand:
    a = 7**5
    m = 2**32-1

    def __init__(self, seed):
        self.previous = seed

    def rand(self):
        self.previous = LCGrand.a * self.previous % LCGrand.m

        return self.previous


class ListRand:

    def __init__(self, list_of_numbers):
        self.list_nr = list_of_numbers.copy()
        self.next = 0

    def rand(self):

        number = self.list_nr[self.next]

        if self.next > len(self.list_nr):
            raise RuntimeError

        self.next += 1

        return number


if __name__ == '__main__':

    list_nr = ListRand([1, 5, 1, 2, 3, 4])
    last = LCGrand(256)

    for i in range(6):
        print(f'Random number from LCGrand {last.rand()} and i*th number '
              f'{list_nr.rand()}')
