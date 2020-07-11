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

def about():
    print("NOT YET IMPLEMENTED! \n")
    print("Press RETURN to continue...")

def render(menu):
    os.system("clear")
    header_text()
    print("\n \n")
    if menu == "MAIN":
        options()
    elif menu == "ABOUT":
        about()
    print("")

