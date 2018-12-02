"""
Weapon class

Stores all weapons values
"""


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
