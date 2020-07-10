import mainloop
import config

def main():
    mainloop.operation_code = 0
    if config.Debug.logging == "True":
        print(f"mainloop.operation_code = {mainloop.operation_code}")