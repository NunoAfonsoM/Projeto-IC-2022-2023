from dice import dice
class Characters:

    #Character constructor where all properties are initialized
    def __init__(self, name: str, hp: int, mp: int, ap: int, wp: int, init: int, isPlayer: bool):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.ap = ap
        self.wp = wp
        self.init = init
        self.turnOrder = 0
        self.isPlayer = isPlayer
    
    #Sorting method, so that characters can be sorted in lists with list.sort
    def __lt__(self, other):
        if self.turnOrder == other.turnOrder:
            return self.init > other.init
        else:
            return self.turnOrder > other.turnOrder

    #Calculates the turn order based on the init of the character and a d20 roll
    def calcTurnOrder(self):
        self.turnOrder = self.init + dice(20)

    #Calculates the damage, applies the damage to the target and prints the information
    def attack(self, target):
        dmg = self.wp - target.ap
        target.hp -= dmg
        #If the target gets to a negative hp number set it to 0
        if target.hp < 0:
            target.hp = 0
        print("---------------")
        print(self.name + " attacked " + target.name + " for "+ str(dmg) + " damage!")
        print(target.name + " is now at: " + str(target.hp) + " hp.")
    
    #Prints the character information
    def inspectChar(self):
        print("Name:",self.name)
        print("HP:",self.hp)
        print("MP:",self.mp)
        print("AP:",self.ap)
        print("WP:",self.wp)
        print("Init:",self.init)