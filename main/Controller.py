"""
Game controller class

Class made by Jari
"""

from Player import Player
import Weapons
import Items
import random


class Controller:
    # these are private variables and should not be accessed outside this class.
    _round = 1  # stores games current round
    _players = []  # stores players in game
    _current_player = 0  # stores player playing
    _move_radiation_zone = False  # stores move state of radiation zone
    _radzone = 0
    
    _player_attack = [
        False,  # stores if player is attacking
        None,  # stores if player being attacked
    ]

    # stores weapons
    _weapons = [
        Weapons.Shotgun(),
        Weapons.AssaultRifle(),
        Weapons.SniperRifle()
    ]

    # stores items
    _items = [
        Items.Armor(),
        Items.BandAid(),
        Items.FirstAidKit()
    ]

    # stores colors
    _colors = [
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
        self.reset_player_attack()
        
        if self._current_player < len(self.get_players()) - 1:
            self._current_player += 1
        else:
            self._current_player = 0
            self._round += 1
            self._roll_radiation_zone()
            
        # don't allow dead players to play
        if self.get_current_player().is_dead():
            self.next_turn()

    def get_turn(self):
        return self._turn

    def _roll_radiation_zone(self):
        if random.randrange(1, 3) == 1:
            self._move_radiation_zone = True
            self._radzone += 1
        else:
            self._move_radiation_zone = False
    
    def get_radiation_zone(self):
        return self._move_radiation_zone

    def get_players(self):
        return self._players

    def get_current_player(self):
        return self._players[self._current_player]

    def add_player(self, name):
        self._players.append(Player())

        self._players[-1].set_name(name)
        self._players[-1].set_color(*self._colors[len(self.get_players()) - 1])
        
    def remove_player(self, number):
        del self._players[number]
        
    def get_weapons(self):
        return self._weapons

    def get_items(self):
        return self._items

    def reset_player_attack(self):
        self._player_attack = [False, None]

    def is_attacking(self):
        return self._player_attack[0]
    
    def get_player_attacking(self):
        return self._player_attack[1]
    
    def attack_player(self, tiles):
        self.get_player_attacking().do_damage(self.get_current_player().get_weapon().get_damage(tiles))
    
    def set_player_attacking(self, player):
        self._player_attack[1] = player

    def start_attack(self):
        self._player_attack[0] = True

    def get_radzone(self):
        return self._radzone
    
    def update_radzone(self):
        if self._radzone < 13:
            min_radzone = 0

            player_count = len(self.get_players())

            if player_count == 2:
                min_radzone = 8
            elif player_count == 3:
                min_radzone = 6
            elif player_count == 4:
                min_radzone = 4
            elif player_count == 5:
                min_radzone = 2
            elif player_count == 6:
                min_radzone = 1

            if self._radzone < min_radzone:
                self._radzone = min_radzone
        else:
            self._radzone = 13
            
    def has_winner(self):
        player_count = 0
        
        for player in self.get_players():
            if player.is_alive():
                player_count += 1
                
        if player_count == 1:
            return True
                
        return False
    
    def get_winner(self):
        for player in self.get_players():
            if player.is_alive():
                return player
                
        return None
