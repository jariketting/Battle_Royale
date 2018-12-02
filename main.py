from Player import Player
import Weapons
import Items

test = Player()

test.set_first_item(Items.Armor())

print(test.get_first_item().get_name())

