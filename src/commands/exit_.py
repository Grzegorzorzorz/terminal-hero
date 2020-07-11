import mainloop
import config

from logger import log

def main(parameter):
    if parameter == None:
        # Exit to menu.
        mainloop.operation_code = 2
        log("commands.exit_", "Changing op code to 2.")
    elif parameter == "QUIT":
        # Exit program fully
        mainloop.operation_code = 0
        log("commands.exit_", "Changing op_code to 0.")
    else:
        log("commands.exit_", "Parameter not recognised -- Displaying error.")
        print("""
Parameter not recognised! 
Do "help exit" for a list of valid parameters
        """)