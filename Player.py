from Weapons import Weapon

"""
Player class

name:
    Set the players name:
        obj.set_name(string NAME)
    Get the players name:
        obj.get_name()

color:
    Set color:
        obj.set_color(string COLOR)
    Get color
        obj.get_color()

HP
    Add HP:
        obj.add_hp(int amount)
    Subtract HP
        obj.subtract_hp(int amount)
    Get HP
        obj.get_hp()
Armor
    Add armor:
        obj.add_armor(int amount)
    Subtract armor
        obj.subtract_armor(int amount)
    Get armor
        obj.get_armor()

Doing damage to a player
    Damage first subtracts from the armor and then from the health, this will be automatically calculated and set with
    this function
        obj.do_damage(int amount)

Checking if player is alive
    is_alive() returns true if alive and false if not
"""


class Player:
    # these are private variables and should not be accessed outside this class.
    _name = 'player name'  # stores player name
    _color = 'ffffff'  # stores player color ?RGB of hex color
    _hp = 10  # stores players health
    _armor = 0  # stores player armor

    _weapon = None  # stores players weapon
    _first_item = None  # stores players first item
    _second_item = None  # stores players second item

    _max_hp = 10  # maximum hp player can have
    _max_armor = 6  # maximum armor player can have

    # sets the players name
    def set_name(self, name: str):
        self._name = name  # overwrite current name with new name

    # get the players name
    def get_name(self):
        return self._name  # returns players name

    # sets color of player
    def set_color(self, color: str):
        self._color = color  # overwrite current color with new color

    # get color of player
    def get_color(self):
        return self._color

    # adds HP to player
    def add_hp(self, amount: int):
        # check if amount + current HP is not higher than max
        if self._hp + amount > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = self._hp + amount  # set new hp value

    def subtract_hp(self, amount: int):
        # check if amount - current HP is not lower than zero
        if self._hp - amount < 0:
            self._hp = 0
        else:
            self._hp = self._hp - amount  # set new hp value

    # get players hp
    def get_hp(self):
        return self._hp  # returns players hp

    # adds HP to player
    def add_armor(self, amount: int):
        # check if amount + current armor is not higher than max
        if self._armor + amount > self._max_armor:
            self._armor = self._max_armor
        else:
            self._armor = self._armor + amount  # set new hp value

    def subtract_armor(self, amount: int):
        # check if amount - current armor is not lower than zero
        if self._armor - amount < 0:
            self._armor = 0
        else:
            self._armor = self._armor - amount  # set new armor value

    # get players hp
    def get_armor(self):
        return self._armor  # returns players armor

    # do damage to a player
    def do_damage(self, amount: int):
        damage_hp = amount - self.get_armor()

        self.subtract_armor(amount)

        if damage_hp > 0:
            self.subtract_hp(damage_hp)

    # get if player is alive
    def is_alive(self):
        return self._hp > 0

    # get players weapon
    def get_weapon(self):
        return self._weapon

    # set players weapon
    def set_weapon(self, weapon: Weapon):
        self._weapon = weapon
