import os

file_path = (
        str(os.path.join(os.path.dirname(__file__), "../game.log"))
    )

def clean_file():
    global file_path
    file = open(file_path, "w")
    file.write("------ START OF LOG FILE ----- \n")
    file.close()

def end_log():
    global file_path
    file = open(file_path, "a")
    file.write("------ END OF LOG FILE -----")
    file.close()

def log(module, output):
    global file_path
    file = open(file_path, "a")
    file.write(f"[{module}]: {output}\n")
    file.close()