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
        pass

