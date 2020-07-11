import os

import config

file_path = (
        str(os.path.join(os.path.dirname(__file__), "../game.log"))
    )

def clean_file():
    global file_path
    file = open(file_path, "w")
    if config.Debug.logging == "True":
        file.write("------ START OF LOG FILE ----- \n")
    else:
        file.write("Logging is disabled.\n\n")
        file.write("Enable it in config.properties.")
    file.close()

def end_log():
    if config.Debug.logging == "True":
        global file_path
        file = open(file_path, "a")
        file.write("------ END OF LOG FILE -----")
        file.close()

def log(module, output):
    if config.Debug.logging == "True":
        global file_path
        file = open(file_path, "a")
        file.write(f"[{module}]: {output}\n")
        file.close()