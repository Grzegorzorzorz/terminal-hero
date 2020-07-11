import logger
import mainloop

# Create a new log file
logger.clean_file()

# Change the mainloop operation code to 2, starting the menu.
logger.log("main", "Starting mainloop on op code 2.")
mainloop.operation_code = 2
mainloop.loop()