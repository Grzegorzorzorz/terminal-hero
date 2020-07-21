import config
import commands.help_
import commands.exit_
import commands.map
import commands.move
import commands.observe
import commands.inventory

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
    elif command == "INVENTORY":
        commands.inventory.main()
    else:
        log("command_management", "Command not found.")


# Tests if the inputted command is valid, and if it is, passes it to
# the executor.
def validator(sanitised_command):
    log("command_management", "Testing validity...")
    if help_(sanitised_command) == 0:
        pass
    elif exit_(sanitised_command) == 0:
        pass
    elif map_(sanitised_command) == 0:
        pass
    elif move(sanitised_command) == 0:
        pass
    elif observe(sanitised_command) == 0:
        pass
    elif inventory(sanitised_command) == 0:
        pass
    else:
        log("command_management", "Command not found -- Displaying error.")
        print("""
Unknown command, for a list of commands, type "help"
        """)

# Unifies all of the sanitisation/validation/execution functions.
def run(command):
    validator(sanitiser(command))

# Missing parameter error message.
def missing_parameter(command):
    log("command_management", "Command missing parameter -- Displaying error.")
    print(f"""
The "{command}" command either requires a parameter to function and one was not
provided, or the supplied parameter was invalid.

Type "help {command}" for a list of valid parameters.
    """)

# Command validator testing functions.
def help_(sanitised_command):
    if sanitised_command[0:4] == "HELP":
        if sanitised_command[5:] == "":
            executor("HELP", None)
            return 0
        else:
            executor("HELP", sanitised_command[5:])
            return 0

def exit_(sanitised_command):
    if sanitised_command[0:4] == "EXIT":
        if sanitised_command[5:] == "QUIT":
            executor("EXIT", "QUIT")
            return 0
        elif sanitised_command[5:] == "":
            executor("EXIT", None)
            return 0
        else:
            missing_parameter("exit")
            return 0

def map_(sanitised_command):
    if sanitised_command == "MAP":
        executor("MAP", None)
        return 0
    elif sanitised_command[:3] == "MAP" and sanitised_command[4:] != "":
        missing_parameter("map")
        return 0
    else:
        return 1

def move(sanitised_command):
    if sanitised_command[0:4] == "MOVE":
        if sanitised_command[5:] == "NORTH":
            executor("MOVE", "NORTH")
            return 0
        elif sanitised_command[5:] == "EAST":
            executor("MOVE", "EAST")
            return 0
        elif sanitised_command[5:] == "SOUTH":
            executor("MOVE", "SOUTH")
            return 0
        elif sanitised_command[5:] == "WEST":
            executor("MOVE", "WEST")
            return 0
        else:
            missing_parameter("move")
            return 0

def observe(sanitised_command):
    if sanitised_command == "OBSERVE":
        executor("OBSERVE", None)
        return 0
    elif sanitised_command[:7] == "OBSERVE" and \
        sanitised_command[8:] != "":
            missing_parameter("map")
            return 0
    else:
        return 1

def inventory(sanitised_command):
    if sanitised_command[0:9] == "INVENTORY":
        executor("INVENTORY", None)
        return 0
    elif sanitised_command[:9] == "INVENTORY" and \
        sanitised_command[10:] != "":
            missing_parameter("inventory")
            return 0
    else:
        return 1