from characters import Characters
from dice import dice
from colorama import Fore

#Class derived from characters, implements all the sames stats plus the spells
class PlayerCharacters(Characters):

    #Constructor of PlayerCharacters class
    def __init__(self, name: str, hp: int, mp: int, ap: int, wp: int, init: int, isPlayer: bool, spells: list):
        #Initializes spells property
        self.spells = spells
        #Calls parent class constructor
        super().__init__(name, hp, mp, ap, wp, init, isPlayer)

    #Performs the selected spell
    def castSpells(self, spell: str, target: Characters):

        manaCost = 0
        print("---------------")

        #Select the correct spell based on the str argument "spell"
        #Calculates the damage for that spell
        #Sets the mana cost
        #Print the action
        if spell == Fore.MAGENTA + "Rushdown" + Fore.RESET:
            spellEffectValue = -1 *(self.wp + dice(4))
            manaCost = 5
            print(self.name + " used " + spell + " on " + target.name + " for "+ str(abs(spellEffectValue)) + " damage!")

        elif spell == Fore.MAGENTA + "Exorcism" + Fore.RESET:
            spellEffectValue = -1 *(dice(4)*2)
            manaCost = 5
            print(self.name + " used " + spell + " on " + target.name + " for "+ str(abs(spellEffectValue)) + " damage!")

        elif spell == Fore.MAGENTA + "Mend" + Fore.RESET:
            spellEffectValue = dice(6) + self.wp
            manaCost= 3
            print(self.name + " used " + spell + " on " + target.name + " for "+ str(abs(spellEffectValue)) + " healing ")

        #Takes the mana cost from the caster mana pool
        self.mp -= manaCost
        #Applies the damage to the target
        target.hp += spellEffectValue
        
        #If the target gets to a negative hp number set it to 0
        if target.hp < 0:
            target.hp = 0

        #Print the target current health
        print(target.name + " is now at: " + str(target.hp) + " hp.")

    #Checks if caster has enough mana to cast the spell
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
