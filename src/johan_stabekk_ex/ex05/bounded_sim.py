# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation

__author__ = 'Johan Stabekk'
__email__ = 'johan.stabekk@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        # if left_limit > start:
        #    raise ValueError('Start position has to be inside the boundaries')
        # elif right_limit < home:
        #     raise ValueError('Home position has to be inside the boundaries')

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
        steps = BoundedSimulation(0, 20, 12345, boundary, 20).run_simulation(20)
        print(f'Left boundary {boundary:8d}: {steps}')









