"""
Items class

Class made by Jari

Get items name
    obj.get_name()
"""


# Don't use this class in code
class Item:
    _name = ''
    _image = ''

    # get name of item
    def get_name(self):
        return self._name

    def get_image(self):
        return self._image


# setup armor
class Armor(Item):
    def __init__(self):
        self._name = 'Armor'
        self._image = 'main_screen/cards/items/armor.png'


# setup first aid kit
class FirstAidKit(Item):
    def __init__(self):
        self._name = 'First aid kit'
        self._image = 'main_screen/cards/items/medkit.png'


# setup band aid
class BandAid(Item):
    def __init__(self):
        self._name = 'Band aid'
        self._image = 'main_screen/cards/items/band_aid.png'
