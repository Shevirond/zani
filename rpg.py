class Player:
    def __init__(self, name, hp, max_hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack

    def take_damage(self, amount):
        self.hp = self.hp - amount
        return

    def heal(self, amount):
        self.hp = self.hp + amount

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


p1 = Player("budi", 100, 100, 12)
p2 = Player("agus", 100, 100, 14)
p1.take_damage(p2.attack)


while True:
    print("=== OOP RPG ===n\" \
    "Choose your class:" \
    "1. Warrior" \
    "2. Mage" \
    ">)

    choose = int(input())

    if choose == 1:
        pass