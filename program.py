from characters import Characters
from playerCharacters import PlayerCharacters
from dice import dice
import os
from rules import printRules

class Program:
    
    clear = lambda: os.system('cls')
    characters = []

    warrior = PlayerCharacters("Warrior", 32, 5, 2, 5, 2, True, ["Rushdown"])
    priest = PlayerCharacters("Priest", 20, 25, 0, 2, 6, True, ["Exorcism", "Mend"])
    
    characters.append(warrior)
    characters.append(priest)

    f = open("OrcNames.txt")
    orcNames = f.readlines()
    f.close()
    
    clear()
    printRules()
    startGame = False
    difficulty = "Easy"
    numOfWaves = 1
    while not startGame:
        validInput = False
        while not validInput:
            pInput = input("Do you want to change game settings? Y/N\nInput:").capitalize()
            numOfOrcs = 1
            if pInput == "Y":
                validInput = True
                print("What do you want to change?\n1 - Difficulty\n2 - Number of waves?")
                pInput = input("Input: ").capitalize()
                if pInput == "1":
                    validDifficulty = False
                    while not validDifficulty:
                        print("Which difficulty do you want?\n1 - Easy\n2 - Medium\n3 - Hard\nCancel - Go back")
                        pInput = input("Input: ").capitalize()
                        if pInput == "1":
                            validDifficulty = True
                            difficulty = "Easy"
                            print("Difficulty set to Easy")
                        elif pInput == "2":
                            validDifficulty = True
                            difficulty = "Medium"
                            print("Difficulty set to Medium")
                        elif pInput == "3":
                            validDifficulty = True
                            difficulty = "Hard"
                            print("Difficulty set to Hard")
                        elif pInput == "Cancel":
                            validDifficulty = True
                            print("No changes to difficulty!\nDifficulty remains", difficulty)
                        else:
                            print(pInput)
                            print("Invalid Input: ")
                elif pInput == "2":
                    validWaves = False
                    while not validWaves:
                        print("How many waves?")
                        pInput = input("Cancel - Go back\nNumber of waves: ").capitalize()
                        if pInput == "Cancel":
                            validWaves = True
                            print("No changes to number of waves!\nNumber of waves remains", numOfWaves)
                        else:
                            try:
                                numOfWaves = int(pInput)
                                validWaves = True
                                print("Number of waves changed to:", numOfWaves)
                            except:
                                print("Invalid Input")
                        


            elif pInput == "N":
                validInput = True
                startGame = True
                pass
            else:
                print("Invalid input")

    print("Starting game with", numOfWaves,"waves at", difficulty,"difficulty!")
    print("---------------")
    if difficulty == "Easy":
        numOfOrcs = 4
        orcStats = 15, 0, 2, 2, 2
    elif difficulty == "Medium":
        numOfOrcs = 4
        orcStats = 20, 0, 2, 3, 4
    elif difficulty == "Hard":
        numOfOrcs = 6
        orcStats = 20, 0, 2, 3, 4

    for x in range(numOfOrcs):
        orcName = orcNames[dice(len(orcNames))-1]
        orc = Characters(orcName.strip(), orcStats[0], orcStats[1], orcStats[2], orcStats[3], orcStats[4], False)
        orcNames.pop(orcNames.index(orcName))
        characters.append(orc)
       
    inGame = True

    currentWave = 1
    playerChars = 2
    enemiesChars = numOfOrcs
    while inGame:
        
        pInput = input("Start new round? Y/N\nInput: ").capitalize()

        if pInput == "Y":

            clear()
            print("Current wave:", currentWave) 

            for x in characters:
                x.calcTurnOrder()

            characters.sort()

            for char in characters:

                if char.isPlayer and enemiesChars > 0:

                    targetIndexes = []
                    for x in characters:
                        if not x.isPlayer:
                            targetIndexes.append(characters.index(x))

                    validInput = False
                    while not validInput:
                        
                        print("---------------")
                        print("It's",char.name,"turn, what should he do?")
                        print("1 - Attack\n2 - Cast Spell")
                        pInput = input("Input: ")

                        if pInput == "1":
                            validInput = True
                            validTarget = False
                            while not validTarget:
                                print("---------------")
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
                            validSpell = False
                            while not validSpell:
                                canCast = False
                                spell = ""
                                print("---------------")
                                print("Wich spell you want to use?")

                                for x in range(len(char.spells)):
                                    print(str(x + 1) + " - " + char.spells[x]) 

                                pInput = input("Input: ")
                                
                                print(char.spells[int(pInput)-1])

                                try:
                                    canCast = char.testSpells(char.spells[int(pInput)-1])
                                    validSpell = True
                                    spell = char.spells[int(pInput)-1]
                                except:
                                    print("Invalid input")

                                if canCast:
                                    validTarget = False
                                    while not validTarget:
                                        print("---------------")
                                        print("What's your target?")
                                        if(spell == "Mend"):
                                            targetIndexes = []
                                            for x in characters:
                                                if x.isPlayer:
                                                    targetIndexes.append(characters.index(x))

                                        for x in range(len(targetIndexes)):
                                            print(str(x+1) + " - " + characters[targetIndexes[x]].name )

                                        pInput = input("Input: ")

                                        try:
                                            char.castSpells(spell, characters[targetIndexes[int(pInput)-1]])
                                            validTarget = True
                                        except:
                                            print("Invalid input")
                                else:
                                    validInput = False
                                    print("---------------")
                                    print("Not enough Mana!")
                                    
                        else:
                            print("Invalid input!")  
                elif not char.isPlayer and playerChars > 0:
                    targetIndexes = []
                    for x in characters:
                        if x.isPlayer:
                            targetIndexes.append(characters.index(x))
                    target = dice(len(targetIndexes)) - 1
                    char.attack(characters[targetIndexes[target]])
            
                #Pop all characters who have 0 or less hp
                for char in characters:
                    if char.hp <= 0:
                        print("---------------")
                        print(char.name,"has died... press f")
                        characters.pop(characters.index(char))
            
                playerChars = 0
                enemiesChars = 0
                for x in characters:
                    if x.isPlayer:
                        playerChars += 1
                    else:
                        enemiesChars += 1
                
                if playerChars < 1:
                    inGame = False
                    playerWin = False
                elif enemiesChars < 1:
                    if currentWave < numOfWaves:
                        currentWave += 1
                        if len(orcNames) < numOfOrcs: 
                            f = open("OrcNames.txt")
                            orcNames = f.readlines()
                            f.close() 
                            
                        for x in range(numOfOrcs):
                            orcName = orcNames[dice(len(orcNames))-1]
                            orc = Characters(orcName.strip(), 15, 0, 2, 2, 2, False)
                            orcNames.pop(orcNames.index(orcName))
                            characters.append(orc)
                        enemiesChars = numOfOrcs
                    else:
                        inGame = False
                        playerWin = True
    
        elif pInput == "N":
            pInput = input("What do you wanna do?\n1 - Exit\n2 - Inspect characters\nInput: ")
            if pInput == "1":
                print("You ended the game...")
                break

        else:
            print("Invalid input")  

    if not inGame:
        if playerWin : print("PLAYER WINS!")
        else : print("Player lost...")