"""
Game controller class
"""


class Controller:
    # these are private variables and should not be accessed outside this class.
    _round = 1  # stores games current round
    _players = []  # stores players in game
    _turn = 0  # stores player that is turning ?randomize this number to have a random player start
