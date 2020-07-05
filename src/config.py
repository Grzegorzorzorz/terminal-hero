import os

import configparser

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "../config.properties")
config.read(config_file_path)

debug_logging = config["debug"]["logging"]
other_game_version = config["other"]["game-version"]