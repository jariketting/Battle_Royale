"""
Weapon class

Stores all weapons values

Get name of weapon:
    weapon.get_name()
Get damage weapon does (number between zero and two)
    weapon.get_damage(INT)
"""


# Don't use this class in code
class Weapon:
    _name = ''  # stores weapons name
    _damage_same_tile = 0  # stores damage when on same tile
    _damage_first_tile = 0  # stores damage when on first tile
    _damage_second_tile = 0  # stores damage when on second tile

    # get name of weapon
    def get_name(self):
        return self._name

    # get weapon damage done to player
    def get_damage(self, tile_count: int):
        # check damage to return based on number of tiles
        if tile_count == 0:
            return self._damage_same_tile  # damage done on same tile
        elif tile_count == 1:
            return self._damage_first_tile  # damage done one tile away
        elif tile_count == 2:
            return self._damage_second_tile  # damage done two tiles away
        else:
            return 0  # default value if for whatever reason number is wrong


# setup shotgun
class Shotgun(Weapon):
    def __init__(self):
        self._name = 'Shotgun'
        self._damage_same_tile = 7
        self._damage_first_tile = 3
        self._damage_second_tile = 0


# setup Assault rifle
class AssaultRifle(Weapon):
    def __init__(self):
        self._name = 'Assault rifle'
        self._damage_same_tile = 3
        self._damage_first_tile = 5
        self._damage_second_tile = 3


# setup sniper rifle
class SniperRifle(Weapon):
    def __init__(self):
        self._name = 'Sniper rifle'
        self._damage_same_tile = 1
        self._damage_first_tile = 4
        self._damage_second_tile = 7


