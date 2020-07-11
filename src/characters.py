import sys

import config
import world

class PlayerObject:
    def __init__(self, x, y, inventory, level, health, max_health):
        self.x = x
        self.y = y
        self.inventory = inventory
        self.level = level
        self.health = health
        self.max_health = max_health

# Declare the player as a global variable.
player = None

def generate_player():
    # Announce generation of the player.
    sys.stdout.write("Generating player...   ")
    global player
    player = PlayerObject(
        x = 2,
        y = 2,
        inventory=[],
        level=1,
        health=20,
        max_health=20
    )
    # "Discover" the spawn region.
    world.region_map[2][2].discovered = True
    # Announce successful player generation.
    sys.stdout.write("Done! \n")