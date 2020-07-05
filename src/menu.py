import os

import mainloop
import config

def header_text():
    print(f"""
Grzegorz Ciołek's
 _____                   _             _   _   _
|_   _|__ _ __ _ __ ___ (_)_ __   __ _| | | | | | ___ _ __ ___  
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | |_| |/ _ \ '__/ _ \ 
  | |  __/ |  | | | | | | | | | | (_| | | |  _  |  __/ | | (_) |
  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_| |_| |_|\___|_|  \___/ 

Version: {config.Other.game_version}
""")

def options():
    print("1.    Start game")
    print("2.    About")
    print("3.    Exit")

def render():
    os.system("clear")
    header_text()
    print("\n \n")
    options()
    print("")

def about():
    print("""
NOT YET ADDED
    """)

def start():
    menu_status = 1
    while menu_status == 1:
        render()
        user_input = input(" > ")
        if user_input == "1":
            menu_status = 0
            return 1
        if user_input == "3":
            menu_status = 0
            return 0
