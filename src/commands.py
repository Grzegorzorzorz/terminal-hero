def help_(command=False):
    # Checks if command specific help is requested.
    if command == False:
        # Prints command list
        print(f"""
Available commands:
    "help", "exit"

For help with a specific command, type "help [command]"
        """)
    elif command == "HELP":
        # Prints help for the help command
        print("""
Displays help for commands.

Usage:
    help [command]
    
If provided with a command, displays specific help information about the
specified command.

Otherwise displays a list of all availible commands.
        """)
    elif command == "EXIT":
        # Prints help for the exit command
        print("""
Exits the game.

Usage:
    exit
    
This, however, does not save the game, so use with care.
        """)
    else:
        print("""
There is no help entry for the specified command.
        """)

def exit_():
    import mainloop

    mainloop.operation_code = 0