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
        """ This function calculates one step for the walker class.

        Returns nothing
        -------

        """
        self.position += 2 * random.randint(0, 1) - 1
        self.steps += 1

    def is_at_home(self):
        return self.position == self.end_point

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        self.start_pos = start
        self.end_pos = home
        self.seed = random.seed(seed)

    def single_walk(self):

        walker = Walker(self.start_pos, self.end_pos)

        while not walker.is_at_home():
            walker.move()

        return walker.get_steps()

    def run_simulation(self, num_walks):
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':
    print('Calculating list 1 -> 3 with start = 0 and home = 10')
    print(f'List 1:{Simulation(0, 10, 12345).run_simulation(20)}')
    print(f'List 2:{Simulation(0, 10, 12345).run_simulation(20)}')
    print(f'List 3:{Simulation(0, 10, 54321).run_simulation(20)}')
    print('Calculating list 4 -> 6 with start = 10 and home = 0')
    print(f'List 4:{Simulation(10, 0, 12345).run_simulation(20)}')
    print(f'List 5:{Simulation(10, 0, 12345).run_simulation(20)}')
    print(f'List 6:{Simulation(10, 0, 54321).run_simulation(20)}')
