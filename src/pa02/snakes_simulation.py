# -*- coding: utf-8 -*-

import random

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class Board:
    snakes = {1: 4, 4: 10, 40: 67}
    ladders = {6: 2, 20: 15, 69: 27}
    goal = 90

    def __init__(self, snakes=None, ladders=None, goal=None):
        """

        Parameters
        ----------
        snakes
        ladders
        goal
        """

        if ladders is None:
            ladders = Board.ladders
        if snakes is None:
            snakes = Board.snakes

        self.snakes = dict(snakes)
        self.ladders = dict(ladders)

        if goal is None:
            self.goal = Board.goal
        else:
            self.goal = goal

        self.snakes_and_ladders = self.snakes.update(self.ladders)

    def goal_reached(self, position):
        return position >= self.goal

    def position_adjustment(self, position):
        new_position = self.snakes_and_ladders.get(position, position)

        return new_position - position


class Player:

    def __init__(self, board):
        self.board = board
        self.position = 0
        self.number_of_moves = 0

    def move(self):
        roll = random.randint(1, 6)

        self.position += roll
        self.position = self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class ResilientPlayer(Player):

    def __init__(self, board, plus_steps=1):

        super().__init__(board)
        self.plus_step = plus_steps
        self.fell_down = False

    def move(self):

        if self.fell_down:
            extra = self.plus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position = self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class LazyPlayer(Player):
    def __init__(self, board, minus_steps=1):
        super().__init__(board)
        self.minus_step = minus_steps
        self.climbed = False

    def move(self):

        if self.climbed:
            extra = self.minus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position = self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class Simulation:
    def __init__(self, players, randomize_players=False,
                 seed=None, board=Board()
                 ):
        """

        Parameters
        ----------
        players
        randomize_players
        seed
        """
        self.board = board
        self.player_types = frozenset(c.__name__ for c in players)
        self.players = players
        self.seed = random.seed(seed)
        self.randomize_players = randomize_players
        self.results = []

        if self.randomize_players is True:
            self.players = self.players.random.shuffle()

    def single_game(self):
        while True:
            for player in self.players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.number_of_moves, type(player).__name__

    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass


if __name__ == '__main__':
    pass