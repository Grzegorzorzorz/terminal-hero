import sys

import config
import characters
import world

from logger import log

# The map should look something like the following:
"""
 N  ·-----------·   Key:
_|_ | # # # # # |   # - Unexplored
 |  | # # # # # |   P - Player location
    | # # P # # |   + - Explored
    | # # # # # |
    | # # # # # |
    ·-----------·
"""


def render():
    log("commands.map", "Rendering map...")
    # Line 0
    print("")
    # Line 1
    sys.stdout.write(" N  ")
    sys.stdout.write("·-----------·    ")
    sys.stdout.write("Key: \n")
    # Lines 2 - 6
    for y in range(0, 5):
        if y == 0:
            sys.stdout.write("_|_ | ")
        elif y == 1:
            sys.stdout.write(" |  | ")
        else:
            sys.stdout.write("    | ")
        for x in range(0, 5):
            if world.region_map[x][y].discovered == True:
                if characters.player.x == x and characters.player.y == y:
                    sys.stdout.write(f"{config.MapMarkers.player} ")
                else:
                    sys.stdout.write(f"{world.region_map[x][y].marker} ")
            else:
                sys.stdout.write(f"{config.MapMarkers.unexplored_region} ")
            if x == 4:
                if y == 0:
                    print(f"|    {config.MapMarkers.player}: Player")
                elif y == 1:
                    print(f"|    {config.MapMarkers.spawn_point}: Spawn region")
                elif y == 2:
                    print(f"|    {config.MapMarkers.boss_region}: Boss region")
                        
                elif y == 3:
                    print(f"|    {config.MapMarkers.explored_region}: Explored")
                elif y == 4:
                    print(
                    f"|    {config.MapMarkers.unexplored_region}: Unexplored")
                else:
                    print("|")
    # Line 7 - 8
    print("    ·-----------· \n")
    log("commands.map", "Map rendered successfully.")