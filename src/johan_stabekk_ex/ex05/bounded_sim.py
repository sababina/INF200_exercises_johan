# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left = left_limit
        self.right = right_limit

    def move(self):

        super().move()

        if self.position > self.right:
            self.position = self.right
        elif self.position < self.left:
            self.position = self.left


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.right = right_limit
        self.left = left_limit

    def walk(self):
        walker = BoundedWalker(self.start, self.home, self.left, self.right)

        stride = 0
        while not walker.is_at_home():
            walker.move()
            stride += 1

        return stride


if __name__ == '__main__':
    boundaries = [0, -10, -100, -1000, -10000]

    for boundary in boundaries:
        steps = BoundedSimulation(0, 20, 12345, boundary,
                                  20).run_simulation(20)
        print(f'Left boundary {boundary:8d}: {steps}')
