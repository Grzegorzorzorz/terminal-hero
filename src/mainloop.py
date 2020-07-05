import command_management
import menu

# Operation code definitions:
#    0 - Exit
#    1 - Run game

# Set the operation code to 1.

operation_code = 1


# Mainloop
def loop():
    while operation_code != 0:
        while operation_code == 1:
            user_input = input(" > ")
            command_management.run(user_input)