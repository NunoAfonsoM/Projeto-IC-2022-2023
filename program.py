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

    inGame = True

    while inGame:
        for x in characters:
            x.calcTurnOrder()

        characters.sort()

        for char in characters:
            if char.isPlayer:
                print(char.name)
                validInput = False
                while not validInput:

                    print("It's",char.name,"turn, what should he do?")
                    print("1 - Attack\n2 - Cast Spell")
                    pInput = input("Input: ")

                    if pInput == "1":
                        validInput = True
                        char.attack(megaorc)

                    elif pInput == "2":
                        validInput = True
                        char.castSpells("Rushdown", megaorc)
                    else:
                        print("Invalid input!")  
            else:
                char.attack(megaorc)
        
        #Pop all characters who have 0 or less hp
        for char in characters:
            if char.hp <= 0:
                print(char.name,"has died... press f")
                characters.pop[char]
        
        if (warrior not in characters) and (priest not in characters):
            inGame = False
            playerWin = False
        elif characters.count(orc) < 1:
            inGame = False
            playerWin = True
    
    if playerWin:
        print("Player Won!")
    else:
        print("Player Lost...")
