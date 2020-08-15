import json
import os
import random
import sys

import config
import items
import world

from logger import log

class EnemyObject:
    def __init__(self, name, race, weapon, level, health, loot, type_):
        self.name = name
        self.race = race
        self.weapon = weapon
        self.loot = loot
        self.level = level
        self.health = health
        self.max_health = self.health
        self.type_ = type_

    def get_name(self):
        pass

def generate_enemy():
    # Define race and name file paths.
    bin_path = (
        os.path.join(os.path.dirname(__file__), "../../bin")
    )
    #name_file_path = (bin_path + "/enemy_names.txt")
    #race_file_path = (bin_path + "/enemy_races.txt")

    # Open race and name files, assign their values to a list and close them.
    #name_file = open(name_file_path, "r")
    #race_file = open(race_file_path, "r")
    #names = name_file.readlines()
    #races = race_file.readlines()
    #name_file.close()
    #race_file.close()

    # Eliminate the newline character
    #for x in range(0, len(names) - 1):
    #    names[x] = names[x].replace("\n", "")
    #for x in range(0, len(races) - 1):
    #    races[x] = races[x].replace("\n", "")

    # Get a raw list of class files
    class_files_names = os.listdir(bin_path + "/NPC/classes")
    class_files = []
    # Read the class files into a list, return a warning if the file is
    # invalid.
    for x in range(0, len(class_files_names)):
        try:
            class_files.append(json.load(open(bin_path + "/NPC/classes/" + class_files_names[x])))
        except:
            log("characters.NPC", f"{class_files_names[x]} is not a vaild \
json class file'", "WARN")
    
    # Assign a random file as the enemies class
    enemy_profile = class_files[random.randint(0, len(class_files) - 1)]
    # Open the name file and sanitise the outputs
    try:
        name_file = open(bin_path + "/NPC/name_lists/" + \
            enemy_profile["naming"]["name_list"], "r")
    except:
        log("characters.NPC", f"Name file " + enemy_profile["naming"]["name_list"] + " not found.", "WARN")
        name_file = open(bin_path + "/NPC/name_lists/fallback.txt", "r")
    names = name_file.readlines()
    name_file.close()
    for x in range(0, len(names) - 1):
        names[x] = names[x].replace("\n", "")

    # Create the enemy object.
    enemy = EnemyObject(
        name=names[random.randint(0, len(names) - 1)],
        race=enemy_profile["naming"]["class_name"],
        weapon=items.weapons[random.randint(0, len(items.weapons) - 1)],
        level=random.randint(1, 5),
        health=enemy_profile["base_attributes"]["health"],
        loot=[],
        type_="enemy"
    )

    return enemy