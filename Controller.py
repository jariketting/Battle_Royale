"""
Game controller class

Class made by Jari
"""


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
