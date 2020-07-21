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

class EnemyObject:
    def __init__(self, name, race, weapon, level, loot, type_):
        self.name = name
        self.race = race
        self.weapon = weapon
        self.loot = loot
        self.level = level
        self.max_health = (10 + level * 5)
        self.health = self.max_health
        self.type_ = type_

    def get_name(self):
        pass

# Declare the player as a global variable.
player = None

def generate_player():
    log("characters", "Generating player...")
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
    log("characters", "Generated player successfully.")
    sys.stdout.write("Done! \n")

def generate_enemy():
    # Define race and name file paths.
    bin_path = (
        os.path.join(os.path.dirname(__file__), "../bin")
    )
    name_file_path = (bin_path + "/enemy_names.txt")
    race_file_path = (bin_path + "/enemy_races.txt")

    # Open race and name files, assign their values to a list and close them.
    name_file = open(name_file_path, "r")
    race_file = open(race_file_path, "r")
    names = name_file.readlines()
    races = race_file.readlines()
    name_file.close()
    race_file.close()

    # Eliminate the newline character
    for x in range(0, len(names) - 1):
        names[x] = names[x].replace("\n", "")
    for x in range(0, len(races) - 1):
        races[x] = races[x].replace("\n", "")


    # Create the enemy object.
    enemy = EnemyObject(
        name=names[random.randint(0, len(names) - 1)],
        race=races[random.randint(0, len(races) - 1)],
        weapon=items.weapons[random.randint(0, len(items.weapons) - 1)],
        level=random.randint(1, 5),
        loot=[],
        type_="enemy"
    )

    return enemy