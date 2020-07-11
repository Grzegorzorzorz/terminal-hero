import world
import characters

def north():
    if characters.player.y > 0:
        characters.player.y = characters.player.y - 1
    else:
        characters.player.y = 4
    world.region_map[characters.player.x][characters.player.y].discovered = True

def east():
    if characters.player.x < 4:
        characters.player.x = characters.player.x + 1
    else:
        characters.player.x = 0
    world.region_map[characters.player.x][characters.player.y].discovered = True

def south():
    if characters.player.y < 4:
        characters.player.y = characters.player.y + 1
    else:
        characters.player.y = 0
    world.region_map[characters.player.x][characters.player.y].discovered = True

def west():
    if characters.player.x > 0:
        characters.player.x = characters.player.x - 1
    else:
        characters.player.x = 4
    world.region_map[characters.player.x][characters.player.y].discovered = True

def main(direction):
    if direction == "NORTH":
        north()
    elif direction == "EAST":
        east()
    elif direction == "SOUTH":
        south()
    elif direction == "WEST":
        west()
    elif direction == None:
        print("""
Incorrect usage, type "help move" for more information.
        """)
    else:
        print("An internal error occured.")