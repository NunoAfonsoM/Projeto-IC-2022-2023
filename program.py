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
        
        pInput = input("Start new round? Y/N")
        pInput = pInput.capitalize()

        if pInput == "Y":
        
            for x in characters:
                x.calcTurnOrder()

            characters.sort()

            for char in characters:
                if char.isPlayer:

                    targetIndexes = []
                    for x in characters:
                        if not x.isPlayer:
                            targetIndexes.append(characters.index(x))

                    validInput = False
                    while not validInput:

                        print("It's",char.name,"turn, what should he do?")
                        print("1 - Attack\n2 - Cast Spell")
                        pInput = input("Input: ")

                        if pInput == "1":
                            validInput = True
                            validTarget = False
                            while not validTarget:
                                print("What is your target? ")

                                for x in range(len(targetIndexes)):
                                    print(str(x+1)+" - "+ characters[targetIndexes[x]].name)
                                
                                pInput = input("input: ")

                                try:
                                    char.attack(characters[targetIndexes[int(pInput)-1]])
                                    validTarget=True
                                except:
                                    print("Invalid input ")


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
        
        elif pInput == "N":
            print("OK")

        else:
            print("Invalid input")

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
