from commands import *

# Converts given commands to upper case, for execution.
def sanitiser(raw_data):
    return raw_data.upper()

# Executes the provided command
def executor(command, parameter):
    if command == "HELP":
        help_.main(parameter)
    if command == "EXIT":
        exit_.main

# Tests if the inputted command is valid, and if it is, passes it to
# the executor.
def validator(sanitised_command):
    # Help command
    if sanitised_command[0:4] == "HELP":
        if sanitised_command[5:] == "":
            executor(sanitised_command[0:4], False)
        else:
            executor(sanitised_command[0:4], sanitised_command[5:])
    # Exit command
    elif sanitised_command[0:4] == "EXIT":
        executor(sanitised_command[0:4], None)
    else:
        print("""
Unknown command, for a list of commands, type "help"
        """)

# Unifies all of the sanitisation/validation/execution functions.
def run(command):
    validator(sanitiser(command))