from dice import dice
class Characters:

    def __init__(self, name: str, hp: int, mp: int, ap: int, wp: int, init: int, isPlayer: bool):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.ap = ap
        self.wp = wp
        self.init = init
        self.turnOrder = 0
        self.isPlayer = isPlayer
    
    def __lt__(self, other):
        if self.turnOrder == other.turnOrder:
            return self.init > other.init
        else:
            return self.turnOrder > other.turnOrder

    def calcTurnOrder(self):
        self.turnOrder = self.init + dice(20)

    def attack(self, target):
        dmg = self.wp - target.ap
        target.hp -= dmg
        if target.hp < 0:
            target.hp = 0
        print("---------------")
        print(self.name + " attacked " + target.name + " for "+ str(dmg) + " damage!")
        print(target.name + " is now at: " + str(target.hp) + " hp.")
    
    def inspectChar(self):
        print("Name:",self.name)
        print("HP:",self.hp)
        print("MP:",self.mp)
        print("AP:",self.ap)
        print("WP:",self.wp)
        print("Init:",self.init)