class Nothing:
    def __init__(self, name):
        self.name = name

class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value

class Potion:
    def __init__(self, name, type_, effect, value):
        self.name = name
        self.type_ = type_
        self.effect = effect
        self.value = value
    """
    Possible potion types:
    Null - Does nothing.
    0 - Adds "effect" health points to the player.
    1 - Multiplies player damage by "effect".
    2 - Decreases enemy health points by "effect".
    """


weapons = {
    0 : Weapon(
        name="Fists",
        damage=[1,2],
        value=None
    ),
    1 : Weapon(
        name="Basic Sword",
        damage=[2,3],
        value=5
    )
}

potions = {
    0 : Potion(
        name="Healing Potion",
        type_=0,
        effect=5,
        value=5
)
}

other = {
    0 : Nothing(
        name="[Empty]"
    )
}