import world

class PlayerObject:
    def __init__(self, region, inventory, level, health, max_health):
        self.region = region
        self.inventory = inventory
        self.level = level
        self.health = health
        self.max_health

player = PlayerObject(
    region=world.region_map[3][3],
    inventory=[],
    level=1,
    health=20,
    max_health=20
)