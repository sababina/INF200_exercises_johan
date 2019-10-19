# -*- coding: utf-8 -*-

import random

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class Walker:
    def __init__(self, start, home):
        self.position = start
        self.end_point = home
        self.steps = 0

    def move(self):
        self.position += 2 * random.randint(0, 1) - 1
        self.steps += 1

    def is_at_home(self):
        return self.position == self.end_point

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


def start_to_home(start, home):
    walker = Walker(start, home)

    while not walker.is_at_home():
        walker.move()

    return walker.get_steps()


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50, 100]
    num_tries = 5
    seed = 1

    random.seed(seed)

    for dist in distances:
        walk_length = [start_to_home(0, dist) for _ in range(num_tries)]
        print(f'Distance:  {dist:3d} -> Path Lengths: {sorted(walk_length)}')




