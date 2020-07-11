def main(command=None):
    # Checks if command specific help is requested.
    if command == None:
        command_list()
    elif command == "HELP":
        help_()
    elif command == "EXIT":
        exit_()

    else:
        print("""
There is no help entry for the specified command.
        """)

def command_list():
     print(f"""
Available commands:
    "help", "exit"

For help with a specific command, type "help [command]"
        """)

def help_():
    print("""
Displays help for commands.

Usage:
    help [command]
    
If provided with a command, displays specific help information about the
specified command.

Otherwise displays a list of all availible commands.
        """)

def exit_():
    print("""
Exits the game.

Usage:
    exit [parameter]

By default, the game exits into the menu, WITHOUT saving.

Parameters:
    "quit" -- Exits the game fully, does NOT save.
        """)