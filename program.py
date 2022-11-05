from characters import Characters
from playerCharacters import PlayerCharacters



class Program:
    
    characters = []

    warrior = PlayerCharacters("Warrior", 32, 5, 2, 5, 2, True, ["Rushdown"])
    priest = PlayerCharacters("Priest", 20, 25, 0, 2, 6, True, ["Exorcism", "Mend"])
    
    characters.append(warrior)
    characters.append(priest)


    for x in range(2):
       orc = Characters("Orc "+ str(x+1), 15, 0, 2, 2, 2, False)
       characters.append(orc)

    megaorc = Characters("Mega Orc", 100, 0, 0, 0, 0, False)
    

    for x in characters:
        x.calcTurnOrder()
        

    characters.sort()
    
    priest.castSpells("Exorcism", megaorc)
