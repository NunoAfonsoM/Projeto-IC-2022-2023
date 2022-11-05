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