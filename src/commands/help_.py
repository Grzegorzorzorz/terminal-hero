from logger import log

def main(command=None):
    # Checks if command specific help is requested.
    if command == None:
        command_list()
    elif command == "HELP":
        help_()
    elif command == "EXIT":
        exit_()
    elif command == "MAP":
        map()
    elif command == "MOVE":
        move()
    elif command == "OBSERVE":
        observe()
    else:
        print("""
There is no help entry for the specified command.
    """)

def command_list():
    log("commands.help_", "Displayed command list.")
    print(f"""
Available commands:
    "help", "exit", "map", "move", "observe"

For help with a specific command, type "help [command]"
    """)

def help_():
    log("commands.help_", "Displayed help for 'help'.")
    print("""
Displays help for commands.

Usage:
    help [command]
    
If provided with a command, displays specific help information about the
specified command.

Otherwise displays a list of all availible commands.
    """)

def exit_():
    log("commands.help_", "Displayed help for 'exit'.")
    print("""
Exits the game.

Usage:
    exit [parameter]

By default, the game exits into the menu, WITHOUT saving.

Parameters:
    "quit" -- Exits the game fully, does NOT save.
    """)

def map():
    log("commands.help_", "Displayed help for 'map'.")
    print("""
Displays a map of all regions.

Usage:
    map
    """)

def move():
    log("commands.help_", "Displayed help for 'move'.")
    print("""
Moves your character in a given direction.

Usage:
    move [parameters]

Parameters:
    "north" -- Moves your character North.
    "east" -- Moves your character East.
    "south" -- Moves your character South.
    "west" -- Moves your character West.
    """)

def observe():
    log("commands.help_", "Displayed help for 'observe'.")
    print("""
Outputs a description of your surroundings.

Usage:
    observe
    """)