import sys
import random

import config

from logger import log

class Region:
    def __init__(
        self,
        spawntile=False,
        discovered=False,
        feature=0,
        marker=config.MapMarkers.explored_region
        ):
        self.spawntile = spawntile
        self.discovered = discovered
        self.feature = self.generate()
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
            log("world", f"Created region {x},{y}.")
            region_map[x][y] = Region()
    log("world", "Generated all regions successfully.")

    # Generate the spawn region.
    log("world", "Generating spawn region...")
    region_map[2][2].spawntile = True
    region_map[2][2].marker = config.MapMarkers.spawn_point
    # "Discover" the spawn region.
    region_map[2][2].discovered = True

    # Generate the boss region.
    log("world", "Generating boss region...")
    corner = random.randint(0,3)
    if corner == 0:
        boss_x = 0
        boss_y = 0
    elif corner == 1:
        boss_x = 4
        boss_y = 0
    elif corner == 2:
        boss_x = 0
        boss_y = 4
    elif corner == 3:
        boss_x = 4
        boss_y = 4
    region_map[boss_x][boss_y].feature = "Boss"
    region_map[boss_x][boss_y].marker = config.MapMarkers.boss_region
    log("world", f"Boss region generated at {boss_x}, {boss_y}.")

    # Announce the end of world generation.
    log("world", "Finished world generation.")
    sys.stdout.write("Done! \n")