import sys
import os

import initiator
import command_management
import menu

from logger import log
from logger import end_log

# Operation code definitions:
#    0 - Exit
#    1 - Run game
#    2 - Run main menu
#    3 - Run battle menu

operation_code = 0

# Mainloop
def loop():
    global operation_code
    log("mainloop", f"Mainloop started, op code {operation_code}.")
    while operation_code != 0:
        while operation_code == 1:
            log("mainloop", "Awaiting user input.")
            user_input = input(" > ")
            log("mainloop", f"User inputted '{user_input}'.")
            command_management.run(user_input)
        while operation_code == 2:
            menu.run()
    log("mainloop", f"Exiting program with op code {operation_code}.")
    end_log()