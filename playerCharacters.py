from characters import Characters

class PlayerCharacters(Characters):

    def __init__(self, name: str, hp: int, mp: int, ap: int, wp: int, init: int, isPlayer: bool, spells: list):

        self.spells = spells
        super().__init__(name, hp, mp, ap, wp, init, isPlayer)