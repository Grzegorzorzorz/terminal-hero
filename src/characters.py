import sys

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
        x = 3,
        y = 3,
        inventory=[],
        level=1,
        health=20,
        max_health=20
    )
    # Announce successful player generation
    sys.stdout.write("Done! \n")