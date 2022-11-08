from characters import Characters
from playerCharacters import PlayerCharacters
from dice import dice
import os
import colorama
from colorama import Fore

def printRules():
    print("---------------")
    print("Your " + Fore.BLUE + "party "+ Fore.RESET + "is fighting a evil " + Fore.RED + "Sorcerer"+ Fore.RESET + "...")
    print("Defeat his hoard of " + Fore.RED + "orcs "+ Fore.RESET + "to win!")
    print("You can choose your difficulty, the default is " + Fore.GREEN + "Easy" + Fore.RESET + ":")
    print(Fore.GREEN + "      Easy" + Fore.RESET + ": waves of 4 " + Fore.RED + "Orcs "+ Fore.RESET + "with default stats")
    print(Fore.YELLOW + "      Medium" + Fore.RESET + ": waves of 4 " + Fore.RED + "Orcs "+ Fore.RESET + "with enhanced stats")
    print(Fore.RED + "      Hard" + Fore.RESET + ": waves of 6 " + Fore.RED + "Orcs "+ Fore.RESET + "with enhanced stats")
    print("The default number of waves is 1, but you can choose how many waves you want before starting the first round!")
    print("You can exit the game by choosing not to start a new round and then choosing to exit")
    print("---------------")

def returnToNormal(string: str):
    return (Fore.RESET + colorama.Style.RESET_ALL + string)
class Program:
    
    clear = lambda: os.system('cls')
    characters = []

    warrior = PlayerCharacters(Fore.BLUE + "Warrior" + Fore.RESET, 32, 5, 2, 5, 2, True, [Fore.MAGENTA + "Rushdown" + Fore.RESET])
    priest = PlayerCharacters(Fore.YELLOW + "Priest" + Fore.RESET, 20, 25, 0, 2, 6, True, [Fore.MAGENTA + "Exorcism" + Fore.RESET, Fore.MAGENTA + "Mend" + Fore.RESET])
    
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
            print("Do you want to change game settings? " + (Fore.GREEN +"Y") + Fore.RESET + "/" + (Fore.RED + "N"))
            pInput = input(Fore.RESET + "Input: ").capitalize()
            numOfOrcs = 1
            if pInput == "Y":
                validInput = True
                print("What do you want to change?\n1 - Difficulty\n2 - Number of waves?")
                pInput = input("Input: ").capitalize()
                if pInput == "1":
                    validDifficulty = False
                    while not validDifficulty:
                        print("Which difficulty do you want?")
                        print(Fore.GREEN + "1 - Easy")
                        print(Fore.YELLOW +  "2 - Medium")
                        print(Fore.RED + "3 - Hard")
                        print(Fore.RESET + "Cancel - Go back")
                        pInput = input("Input: ").capitalize()
                        if pInput == "1":
                            validDifficulty = True
                            difficulty = "Easy"
                            print("Difficulty set to " + Fore.GREEN + "Easy" + Fore.RESET)
                        elif pInput == "2":
                            validDifficulty = True
                            difficulty = "Medium"
                            print("Difficulty set to " + Fore.YELLOW + "Medium" + Fore.RESET)
                        elif pInput == "3":
                            validDifficulty = True
                            difficulty = "Hard"
                            print("Difficulty set to " + Fore.RED + "Hard" + Fore.RESET)
                        elif pInput == "Cancel":
                            validDifficulty = True
                            print(Fore.RED + "No changes to difficulty!")
                            if difficulty == "Easy":
                                print(Fore.RESET + "Difficulty remains: " + Fore.GREEN + "Easy" + Fore.RESET)
                            elif difficulty == "Medium":
                                print(Fore.RESET + "Difficulty remains: " + Fore.YELLOW + "Medium" + Fore.RESET)
                            elif difficulty == "Hard":
                                print(Fore.RESET + "Difficulty remains: " + Fore.RED + "Hard" + Fore.RESET)
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
        orc = Characters(Fore.RED + orcName.strip() + Fore.RESET, orcStats[0], orcStats[1], orcStats[2], orcStats[3], orcStats[4], False)
        orcNames.pop(orcNames.index(orcName))
        characters.append(orc)
       
    inGame = True

    currentWave = 1
    playerChars = 2
    enemiesChars = numOfOrcs
    while inGame:
        
        
        print("Start new Round? " + (Fore.GREEN +"Y") + Fore.RESET + "/" + (Fore.RED + "N"))
        pInput = input(Fore.RESET + "Input: ").capitalize()

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
                        print("It's " + Fore.BLUE + char.name + Fore.RESET + " turn, what should he do?")
                        print("1 - " + Fore.RED + "Attack" + Fore.RESET + "\n2 - " + Fore.MAGENTA + "Cast Spell" + Fore.RESET)
                        pInput = input("Input: ")

                        if pInput == "1":
                            validInput = True
                            validTarget = False
                            while not validTarget:
                                print("---------------")
                                print("What is your target?")

                                for x in range(len(targetIndexes)):
                                    print(str(x+1)+" - " + characters[targetIndexes[x]].name)
                                
                                pInput = input("Input: ")

                                try:
                                    char.attack(characters[targetIndexes[int(pInput)-1]])
                                    validTarget=True
                                except:
                                    print("Invalid input")


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
                                        if(spell == Fore.MAGENTA + "Mend" + Fore.RESET):
                                            targetIndexes = []
                                            for x in characters:
                                                if x.isPlayer:
                                                    targetIndexes.append(characters.index(x))

                                        for x in range(len(targetIndexes)):
                                            print(str(x+1) + " - " + characters[targetIndexes[x]].name )

                                        pInput = input("Input: ")
                                        try:
                                            #print(spell)
                                            char.castSpells(spell, characters[targetIndexes[int(pInput)-1]])
                                            validTarget = True
                                        except:
                                            print("Invalid input")

                                elif validSpell and not canCast:
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
                            orc = Characters(Fore.RED + orcName.strip() + Fore.RESET, orcStats[0], orcStats[1], orcStats[2], orcStats[3], orcStats[4], False)
                            orcNames.pop(orcNames.index(orcName))
                            characters.append(orc)
                        enemiesChars = numOfOrcs
                    else:
                        inGame = False
                        playerWin = True
    
        elif pInput == "N":
            validInput = False
            while not validInput:
                print("What do you want to do?")
                print("1 - " + Fore.GREEN + "Inspect character" + Fore.RESET)
                print("2 - " + Fore.RED + "Exit" + Fore.RESET)
                print("Cancel - Go back")
                pInput = input("Input: ")
                
                if pInput == "1":
                    validInput = True
                    for char in characters:
                        char.inspectChar()
                elif pInput == "2":
                    validInput = True
                    print("You ended the game...")
                    break
                elif pInput == "Cancel":
                    validInput = True
                else:
                    print("Invalid Input")

        else:
            print("Invalid input")  

    if not inGame:
        if playerWin : print("PLAYER WINS!")
        else : print("Player lost...")