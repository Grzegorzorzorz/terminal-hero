import os
import sys

import mainloop
import world
import menu

# Start the main menu.
menu_output = menu.start()
if menu_output == 0:
    exit()
# If the user selects the start game option, begin game startup.
elif menu_output == 1:
    os.system("clear")
    sys.stdout.write("Generating world...    ")
    world.generate_world(5, 5)
    sys.stdout.write("Done! \n")
    print("""
Welcome to Terminal Hero!
For a list of commands, type "help".
    """)
    mainloop.loop()

