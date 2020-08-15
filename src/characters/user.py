import os
import random
import sys

import config
import items
import world

from logger import log

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

def generate():
    log("characters.user", "Generating player...")
    # Announce generation of the player.
    sys.stdout.write("Generating player...   ")
    global player
    player = PlayerObject(
        x = 2,
        y = 2,
        inventory={
            "equipped" : items.weapons[1],
            1 : items.potions[0],
            2 : items.other[0],
            3 : items.other[0],
            "money" : 20
        },
        level=1,
        health=20,
        max_health=20
    )
    # Announce successful player generation.
    log("characters.user", "Generated player successfully.")
    sys.stdout.write("Done! \n")
