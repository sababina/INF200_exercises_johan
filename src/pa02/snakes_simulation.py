# -*- coding: utf-8 -*-

import random

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class Board:
    snakes = {
              1: 40, 8: 10, 24: 5, 33: 3, 36: 52, 42: 30, 43: 62, 49: 79,
              56: 37, 64: 27, 65: 82, 68: 85, 74: 12, 87: 70
              }
    goal = 90

    def __init__(self, snakes_and_ladders=None, goal=None):
        """

        Parameters
        ----------
        snakes_and_ladders
        goal
        """

        self.snakes_and_ladders = snakes_and_ladders
        self.goal = goal
        self.position = 0

    def goal_reached(self):
        return self.position == self.goal

    def position_adjustment(self):
        return


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0

    def move(self):
        pass


class ResilientPlayer(Player):
    pass


class LazyPlayer(Player):
    pass


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
        self.players = players
        self.seed = random.seed(seed)
        self.randomize_players = randomize_players

        if self.randomize_players is True:
            self.players = self.players.random.shuffle()

    def single_game(self):
        pass

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
