import os

import world
import characters

from logger import log

def new_game():
    log("initiator", "Starting new game...")
    os.system("clear")
    world.generate_world()
    characters.generate_player()
    print("""
Welcome to Terminal Hero!
For a list of commands, type "help".
    """)
    log("initiator", "Started game successfully.")