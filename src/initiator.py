import os

import world
import characters

def new_game():
    os.system("clear")
    world.generate_world(5, 5)
    characters.generate_player()
    print("""
Welcome to Terminal Hero!
For a list of commands, type "help".
    """)