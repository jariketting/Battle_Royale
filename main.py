from Player import Player

test = Player()

print(test.get_hp())
print(test.is_alive())

test.do_damage(10)

print(test.get_hp())
print(test.is_alive())
