import mainloop
import config

def main(parameter):
    if parameter == None:
        # Exit to menu.
        mainloop.operation_code = 2
        if config.Debug.logging == "True":
            print(f"[DEBUG] mainloop.operation_code = {mainloop.operation_code}")
    elif parameter == "QUIT":
        # Exit program fully
        mainloop.operation_code = 0
        if config.Debug.logging == "True":
            print(f"[DEBUG] mainloop.operation_code = {mainloop.operation_code}")
    else:
        print("""
Parameter not recognised! 
Do "help exit" for a list of valid parameters
        """)