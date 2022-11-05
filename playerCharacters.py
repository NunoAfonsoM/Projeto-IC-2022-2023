from characters import Characters
from dice import dice

class PlayerCharacters(Characters):

    def __init__(self, name: str, hp: int, mp: int, ap: int, wp: int, init: int, isPlayer: bool, spells: list):

        self.spells = spells
        super().__init__(name, hp, mp, ap, wp, init, isPlayer)

    def castSpells(self, spell: str, target: Characters):

        manaCost = 0
        if spell == "Rushdown":
            spellEffectValue = -1 *(self.wp + dice(4))
            manaCost = 5
            print(self.name + " used Rushdown on " + target.name + " for "+ str(abs(spellEffectValue)) + " damage!")

        elif spell == "Exorcism":
            spellEffectValue = -1 *(dice(4)*2)
            manaCost = 5
            print(self.name + " used Exorcism on " + target.name + " for "+ str(abs(spellEffectValue)) + " damage!")

        elif spell == "Mend":
            spellEffectValue = dice(6) + self.wp
            manaCost= 3
            print(self.name + " used Mend on " + target.name + " for "+ str(abs(spellEffectValue)) + " healing ")

        self.mp -= manaCost
        target.hp += spellEffectValue

        print(target.name + " is now at: " + str(target.hp) + " hp.")
        print("---------------")

    def testSpells(self, spell: str):

        manaCost = 0
        if spell == "Rushdown":
            manaCost = 5

        elif spell == "Exorcism":
            manaCost = 5
            

        elif spell == "Mend":
            manaCost= 3
        
        if self.mp < manaCost:
            return False
        else:
            return True
