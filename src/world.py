import sys
import random

import config
import characters

from logger import log

class Region:
    def __init__(
        self,
        spawntile=False,
        discovered=False,
        feature=0,
        NPC=None,
        marker=config.MapMarkers.explored_region
        ):
        self.spawntile = spawntile
        self.discovered = discovered
        self.feature = self.generate()
        self.NPC = NPC
        self.marker = marker

    def generate(self):
        feature_id = random.randint(0, 1)
        if feature_id == 0:
            return "Forest"
        elif feature_id == 1:
            return "Mountain"

# Declare the region_map list
region_map = []

# Declares the generate world function
def generate_world():
    log("world", "Starting generation...")
    global region_map
    # Announce world generation.
    sys.stdout.write("Generating world...    ")
    # Declare the world map as a 2D array.
    log("world", "Creating region map...")
    region_map = ([[0 for x in range(5)] for y in range(5)])
    for y in range(0, 5):
        for x in range(0, 5):
            region_map[x][y] = Region()
            region_map[x][y].NPC = characters.generate_enemy()
            log("world", f"Created region {x},{y}.")
    log("world", "Generated all regions successfully.")
    # Change spawn region parameters.
    log("world", "Generating spawn region...")
    region_map[2][2].spawntile = True
    region_map[2][2].marker = config.MapMarkers.spawn_point
    region_map[2][2].discovered = True
    region_map[2][2].NPC = None

    # Announce the end of world generation.
    log("world", "Finished world generation.")
    sys.stdout.write("Done! \n")