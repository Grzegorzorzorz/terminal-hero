import config
import commands.help_
import commands.exit_
import commands.map
import commands.move

# Converts given commands to upper case, for execution.
def sanitiser(raw_data):
    return raw_data.upper()

# Executes the provided command
def executor(command, parameter):
    if config.Debug.logging == "True":
        print(f"[DEBUG] Command: {command}, Parameter: {parameter}")
    if command == "HELP":
        commands.help_.main(parameter)
    elif command == "EXIT":
        commands.exit_.main(parameter)
    elif command == "MAP":
        commands.map.render()
    elif command == "MOVE":
        commands.move.main(parameter)


# Tests if the inputted command is valid, and if it is, passes it to
# the executor.
def validator(sanitised_command):
    # Help command
    if sanitised_command[0:4] == "HELP":
        if sanitised_command[5:] == "":
            executor(sanitised_command[0:4], None)
        else:
            executor(sanitised_command[0:4], sanitised_command[5:])
    # Exit command
    elif sanitised_command[0:4] == "EXIT":
        if sanitised_command[5:] == "":
            executor(sanitised_command[0:4], None)
        elif sanitised_command[5:] == "QUIT":
            executor(sanitised_command[0:4], "QUIT")
    # Map command
    elif sanitised_command == "MAP":
        executor(sanitised_command, None)
    elif sanitised_command[0:4] == "MOVE":
        if sanitised_command[5:] == "NORTH":
            executor("MOVE", "NORTH")
        elif sanitised_command[5:] == "EAST":
            executor("MOVE", "EAST")
        elif sanitised_command[5:] == "SOUTH":
            executor("MOVE", "SOUTH")
        elif sanitised_command[5:] == "WEST":
            executor("MOVE", "WEST")
        else:
            executor("MOVE", None)

    else:
        print("""
Unknown command, for a list of commands, type "help"
        """)

# Unifies all of the sanitisation/validation/execution functions.
def run(command):
    validator(sanitiser(command))