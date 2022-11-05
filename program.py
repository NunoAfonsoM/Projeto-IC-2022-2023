from characters import Characters
from playerCharacters import PlayerCharacters



class Program:
    
    warrior = PlayerCharacters("Arthur", 32, 5, 2, 5, 2, True, ["Rushdown"])
    priest = PlayerCharacters("Priest", 20, 25, 0, 2, 6, True, ["Exorcism", "Mend"])
    
    orc = Characters("Orc", 15, 0, 2, 2, 2, False)

    print(warrior.name)