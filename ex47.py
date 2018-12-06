class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
def go(self, direction):
return self.paths.get(direction, None)
    def add_paths(self, paths):
        self.paths.update(paths)
        1 from nose.tools import *
        
from ex47.game import Room


def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it you can grab. There's a
            door to the north.""")
			assert_equal(gold.name, "GoldRoom")
			assert_equal(gold.paths, {})


assert_equal(gold.paths, {})
test_room_paths():
center = Room("Center", "Test room in the center.") north = Room("North", "Test room in the north.") south = Room("South", "Test room in the south.")
center.add_paths({'north': north, 'south': south})
test_room():
gold = Room("GoldRoom",
"""This room has gold in it you can grab. There's a
            door to the north.""")
assert_equal(gold.name, "GoldRoom")