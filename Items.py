"""
Items class
"""


# Don't use this class in code
class Item:
    _name = ''


# setup armor
class Armor(Item):
    def __init__(self):
        self._name = 'Armor'


# setup first aid kit
class FirstAidKit(Item):
    def __init__(self):
        self._name = 'First aid kit'


# setup band aid
class BandAid(Item):
    def __init__(self):
        self._name = 'Band aid'


# setup grenade
class Grenade(Item):
    def __init__(self):
        self._name = 'Grenade'
