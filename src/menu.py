import os

import initiator
import mainloop
import config

from logger import log

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

def run():
    log("menu", "Rendering 'MAIN'.")
    render("MAIN")
    user_input = input(" > ")
    log("menu", f"User inputted '{user_input}'.")
    if user_input == "1":
        log("menu", "Starting new game.")
        initiator.new_game()
        mainloop.operation_code = 1
    elif user_input == "2":
        log("menu", "Rendering 'ABOUT'.")
        render("ABOUT")
        input(" > ")
        log("menu", f"User inputted '{user_input}'.")
    elif user_input == "3":
        log("menu", "Setting op code to 0 -- Exiting game.")
        mainloop.operation_code = 0
        os.system("clear")

