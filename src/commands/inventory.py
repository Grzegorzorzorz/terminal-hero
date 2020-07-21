import characters

from logger import log

def main():
    equipped = characters.player.inventory["equipped"]
    slots = [
        characters.player.inventory[1].name,
        characters.player.inventory[2].name,
        characters.player.inventory[3].name
    ]
    money = characters.player.inventory["money"]
    log("commands.inventory", "Displaying player inventory.")
    print("\nInventory:")
    print(f"   Equipped: {equipped.name}")
    for x in range(0,3):
        print(f"        Slot {x}: {slots[x]}")
    print(f"    Money: {money} Ducats\n")
    log("commands.inventory", "Inventory diplayed successfully.")