"""
Game controller class

Class made by Jari
"""

from Player import Player


class Controller:
    # these are private variables and should not be accessed outside this class.
    _round = 1  # stores games current round
    _players = []  # stores players in game
    _turn = 0  # stores player that is turning ?randomize this number to have a random player start

    # turn to next round
    def next_round(self):
        self._round += 1

    # get current round
    def get_round(self):
        return self._round

    def get_players(self):
        return self._players

    def add_player(self, name: str):
        self._players.append(Player())

        self._players[-1].set_name(name)
