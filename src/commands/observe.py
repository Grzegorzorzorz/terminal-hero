import characters
import world

from logger import log

def main():
    log("commands.observe", "Fetching region...")
    region = world.region_map[characters.player.x][characters.player.y]
    # Observe region features
    if region.feature == "Forest":
        log("commands.observe", "Region type 'Forest', showing description.")
        print("""
Forest placeholder    
        """)
    elif region.feature == "Mountain":
        log("commands.observe", "Region type 'Mountain', showing description.")
        print("""
Mountain placeholder
        """)
    else:
        log("commands.observe", "Region type not found.")
    
    # Observe region NPCs.
    if region.NPC == None:
        log("commands.observe", "NPC not found.")
    elif region.NPC.type_ == "enemy":
        log("commands.observe", "Enemy NPC found: showing description.")
        print(f"""
You also see a Level {region.NPC.level} {region.NPC.race} walking nearby.
        """)