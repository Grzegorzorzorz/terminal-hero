import os

import configparser

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "../config.properties")
config.read(config_file_path)

class Debug:
    logging = config["debug"]["logging"]

class Other:
    game_version = config["other"]["game-version"]