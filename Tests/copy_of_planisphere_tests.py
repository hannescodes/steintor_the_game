from nose.tools import *
from planisphere import *

def test_room():
    gold = Room("GoldRoom",
                """this room has gold in it you can gryb. There is a door in the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")
    west = Room("West", "Test room in the west")  # define west room
    down = Room("Down", "Test room below")

    center.add_paths({'west': west, 'down': down})
    west.add_paths({'east': center})
    down.add_paths({'up': center})

def test_map():
    start = Room("Start", "you can go west and down a hole")
    west = Room("Trees", "There are trees herem you can go east")
    down = Room("Dungeon", "Test Room in the south")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)  # corrected arguments
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    from planisphere import load_room  # import load_room function
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)

    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
