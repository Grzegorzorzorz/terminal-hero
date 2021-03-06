import os

import configparser

config = configparser.ConfigParser()
config_file_path = (
    os.path.join(os.path.dirname(__file__), "../config.properties")
)
config.read(config_file_path)

class MapMarkers:
    global config
    player = config["map-markers"]["player"]
    explored_region = config["map-markers"]["explored-region"]
    unexplored_region = config["map-markers"]["unexplored-region"]
    spawn_point = config["map-markers"]["spawn-point"]
    boss_region = config["map-markers"]["boss-region"]

class Debug:
    global config
    logging = config["debug"]["logging"]
    debug_commands = config["debug"]["debug-commands"]

class Other:
    global config
    game_version = config["other"]["game-version"]