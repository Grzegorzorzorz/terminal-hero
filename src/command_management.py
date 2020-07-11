import config
import commands.help_
import commands.exit_
import commands.map
import commands.move
import commands.observe

from logger import log

# Converts given commands to upper case, for execution.
def sanitiser(raw_data):
    log("command_management", "Sanitising input.")
    return raw_data.upper()

# Executes the provided command
def executor(command, parameter):
    log("command_management", f"Passed command '{command}' \
with parameter '{parameter}'. Attempting to execute...")
    if command == "HELP":
        commands.help_.main(parameter)
    elif command == "EXIT":
        commands.exit_.main(parameter)
    elif command == "MAP":
        commands.map.render()
    elif command == "MOVE":
        commands.move.main(parameter)
    elif command == "OBSERVE":
        commands.observe.main()
    else:
        log("command_management", "Command not found.")


# Tests if the inputted command is valid, and if it is, passes it to
# the executor.
def validator(sanitised_command):
    log("command_management", "Testing validity...")
    # Help command
    if sanitised_command[0:4] == "HELP":
        if sanitised_command[5:] == "":
            executor(sanitised_command[0:4], None)
        else:
            executor(sanitised_command[0:4], sanitised_command[5:])
    # Exit command
    elif sanitised_command[0:4] == "EXIT":
        if sanitised_command[5:] == "QUIT":
            executor(sanitised_command[0:4], "QUIT")
        elif sanitised_command[5:] == "":
            executor(sanitised_command[0:4], None)
        else:
            executor(sanitised_command[0:4], sanitised_command[5:])
    # Map command
    elif sanitised_command == "MAP":
        executor(sanitised_command, None)
    # Move command
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
    # Observe command
    elif sanitised_command[0:7] == "OBSERVE":
        executor(sanitised_command[0:7], None)
    else:
        log("command_management", "Command not found -- Displaying error.")
        print("""
Unknown command, for a list of commands, type "help"
        """)

# Unifies all of the sanitisation/validation/execution functions.
def run(command):
    validator(sanitiser(command))