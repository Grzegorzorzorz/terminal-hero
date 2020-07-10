import sys

import initiator
import command_management
import menu

# Operation code definitions:
#    0 - Exit
#    1 - Run game
#    2 - Run menu

operation_code = 0

# Mainloop
def loop():
    global operation_code
    while operation_code != 0:
        while operation_code == 1:
            user_input = input(" > ")
            command_management.run(user_input)
        while operation_code == 2:
            menu.render()
            user_input = input(" > ")
            if user_input == "1":
                initiator.new_game()
                operation_code = 1
            if user_input == "3":
                operation_code = 0