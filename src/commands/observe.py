import characters
import world

from logger import log

def main():
    log("commands.observe", "Fetching region...")
    region = world.region_map[characters.player.x][characters.player.y]
    if region.feature == "Boss":
        log("commands.observe", "Region type 'Boss', showing description.")
        print("""
Boss placeholder
        """)
    elif region.feature == "Forest":
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