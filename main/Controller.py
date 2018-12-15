"""
Game controller class

Class made by Jari
"""

from Player import Player


class Controller:
    # these are private variables and should not be accessed outside this class.
    _round = 1  # stores games current round
    _turn = 0  # stores player that is turning ?randomize this number to have a random player start
    _players = []  # stores players in game
    _current_player = 0  # stores player playing

    # stores colors
    _color = [
        [141, 0, 0],  # red
        [51, 193, 0],  # green
        [0, 140, 183],  # blue
        [244, 225, 48],  # yellow
        [161, 0, 183],  # purple
        [191, 92, 0],  # orange
        [255, 255, 255],  # black
        [0, 0, 0]  # white
    ]

    # turn to next round
    def next_round(self):
        self._round += 1

    # get current round
    def get_round(self):
        return self._round

    def next_turn(self):
        self._turn += 1
        self._current_player += 1

        # TODO implement check if turn exceeds amount of players

    def get_turn(self):
        return self._turn

    def get_players(self):
        return self._players

    def get_current_player(self):
        return self._players[self._current_player]

    def add_player(self, name):
        self._players.append(Player())

        self._players[-1].set_name(name)
        self._players[-1].set_color(*self._color[len(self.get_players()) - 1])
        
    def remove_player(self, number):
        del self._players[number]
