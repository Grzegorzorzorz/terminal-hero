import os
import time

import config

file_path = (
        str(os.path.join(os.path.dirname(__file__), "../game.log"))
    )

def clean_file():
    global file_path
    file = open(file_path, "w")
    if config.Logging.enable == "True":
        file.write("------ START OF LOG FILE ------\n")
        file.write(f"Current log verbosity: '{config.Logging.verbosity}'.\n")
        file.write("------ STARTING GAME LOG ------\n")
    else:
        file.write("Logging is disabled.\n\n")
        file.write("Enable it in config.properties.")
    file.close()

def end_log():
    if config.Logging.enable == "True":
        global file_path
        file = open(file_path, "a")
        file.write("------ END OF LOG FILE -----")
        file.close()

def log(module, output, severity="INFO"):
    if config.Logging.enable == "True":
        current_time = time.strftime("%H:%M:%S")
        global file_path
        file = open(file_path, "a")
        if config.Logging.verbosity == "DBUG":
            file.write(f"[{current_time}][{severity}][{module}]: {output}\n")
            file.close()
        elif config.Logging.verbosity == "INFO" and severity != "DBUG":
            file.write(f"[{current_time}][{severity}][{module}]: {output}\n")
            file.close()
        elif config.Logging.verbosity == "WARN" and severity != "DBUG" \
            and severity != "INFO":
            file.write(f"[{current_time}][{severity}][{module}]: {output}\n")
            file.close()
        elif config.Logging.verbosity == "EROR" and severity != "DBUG" \
            and severity != "INFO" and severity != "WARN":
            file.write(f"[{current_time}][{severity}][{module}]: {output}\n")
            file.close()