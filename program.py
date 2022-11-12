from characters import Characters
from playerCharacters import PlayerCharacters
from dice import dice
import os
import colorama
from colorama import Fore

#Prints the rules of the game
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

class Program:
    
    #Define clear, that when called clears the console (only works on windows)
    #Does a print "cls: could not be found" on linux
    clear = lambda: os.system('cls')

    #Create an empty list where all characters will be placed
    characters = []


    #Instantiates a Warrior and a Priest that are a PlayerCharacter
    warrior = PlayerCharacters(Fore.BLUE + "Warrior" + Fore.RESET, 32, 5, 2, 5, 2, True, [Fore.MAGENTA + "Rushdown" + Fore.RESET])
    priest = PlayerCharacters(Fore.YELLOW + "Priest" + Fore.RESET, 20, 25, 0, 2, 6, True, [Fore.MAGENTA + "Exorcism" + Fore.RESET, Fore.MAGENTA + "Mend" + Fore.RESET])
    
    #Adds both to the list
    characters.append(warrior)
    characters.append(priest)

    #Opens the OrcNames file, reads all the lines then closes the file
    f = open("OrcNames.txt")
    orcNames = f.readlines()
    f.close()
    
    #Clear the console and print rules
    clear()
    printRules()

    #Define default settings
    startGame = False
    difficulty = "Easy"
    numOfWaves = 1

    #Initial inputs where the player can change the settings
    while not startGame:
        validInput = False
        while not validInput:
            print("Do you want to change game settings? " + (Fore.GREEN +"Y") + Fore.RESET + "/" + (Fore.RED + "N"))
            pInput = input(Fore.RESET + "Input: ").capitalize()
            numOfOrcs = 1
            #If the player wants to change settings
            if pInput == "Y":
                validInput = True
                print("What do you want to change?\n1 - Difficulty\n2 - Number of waves?")
                pInput = input("Input: ").capitalize()
                #Check what he wants to change
                #If "1" change difficulty
                if pInput == "1":
                    validDifficulty = False
                    while not validDifficulty:
                        print("Which difficulty do you want?")
                        print(Fore.GREEN + "1 - Easy")
                        print(Fore.YELLOW +  "2 - Medium")
                        print(Fore.RED + "3 - Hard")
                        print(Fore.RESET + "Cancel - Go back")
                        pInput = input("Input: ").capitalize()
                        #Set the difficulty based on input or cancel 
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
                #If "2" change number of rounds
                elif pInput == "2":
                    validWaves = False
                    while not validWaves:
                        print("How many waves?")
                        pInput = input("Cancel - Go back\nNumber of waves: ").capitalize()
                        if pInput == "Cancel":
                            validWaves = True
                            print("No changes to number of waves!\nNumber of waves remains", numOfWaves)
                        else:
                            #Tries to convert the str input into a int, if it can't the input is invalid
                            try:
                                #Set the number of waves
                                numOfWaves = int(pInput)
                                validWaves = True
                                print("Number of waves changed to:", numOfWaves)
                            except:
                                print("Invalid Input")
            #If the player does not want to change settings                  
            elif pInput == "N":
                validInput = True
                startGame = True
                pass
            else:
                print("Invalid input")

    #Starting the game
    print("Starting game with", numOfWaves,"waves at", difficulty,"difficulty!")
    print("---------------")
    #Sets the number of orcs and their stats based on the difficulty chosen
    if difficulty == "Easy":
        numOfOrcs = 4
        orcStats = 15, 0, 2, 2, 2
    elif difficulty == "Medium":
        numOfOrcs = 4
        orcStats = 20, 0, 2, 3, 4
    elif difficulty == "Hard":
        numOfOrcs = 6
        orcStats = 20, 0, 2, 3, 4


    #Instantiates number of orcs that are Characters
    for x in range(numOfOrcs):
        orcName = orcNames[dice(len(orcNames))-1]
        orc = Characters(Fore.RED + orcName.strip() + Fore.RESET, orcStats[0], orcStats[1], orcStats[2], orcStats[3], orcStats[4], False)
        orcNames.pop(orcNames.index(orcName))
        characters.append(orc)
       
    inGame = True

    currentWave = 1
    playerChars = 2
    enemiesChars = numOfOrcs

    #Main game loop
    while inGame:
        
        
        print("Start new Round? " + (Fore.GREEN +"Y") + Fore.RESET + "/" + (Fore.RED + "N"))
        pInput = input(Fore.RESET + "Input: ").capitalize()

        #Checks if the player wants to start a new round
        if pInput == "Y":

            clear()
            print("Current wave:", currentWave) 

            #Calculate turn order for all characters
            for x in characters:
                x.calcTurnOrder()

            #Sort characters based on turn order and init
            characters.sort()

            #Run through list of characters to perform their actions
            for char in characters:
                
                #If the character is a player and there still are enemies
                if char.isPlayer and enemiesChars > 0:
                    
                    #List of indexes with characters with isPlayer == False
                    targetIndexes = []
                    for x in characters:
                        if not x.isPlayer:
                            targetIndexes.append(characters.index(x))

                    validInput = False
                    #While the player has not chosen a valid input
                    while not validInput:
                        
                        print("---------------")
                        print("It's " + Fore.BLUE + char.name + Fore.RESET + " turn, what should he do?")
                        print("1 - " + Fore.RED + "Attack" + Fore.RESET + "\n2 - " + Fore.MAGENTA + "Cast Spell" + Fore.RESET)
                        pInput = input("Input: ")

                        #If "1" the player performs an attack
                        if pInput == "1":
                            validInput = True
                            validTarget = False
                            #while the player has not chosen a valid target
                            while not validTarget:
                                print("---------------")
                                print("What is your target?")

                                #Print the list of targets
                                for x in range(len(targetIndexes)):
                                    print(str(x+1)+" - " + characters[targetIndexes[x]].name)
                                
                                pInput = input("Input: ")

                                #Try to attack said target, if there's an exception, the player has chosen an invalid input
                                try:
                                    char.attack(characters[targetIndexes[int(pInput)-1]])
                                    validTarget=True
                                except:
                                    print("Invalid input")

                        #If "2" the player performs a spell
                        elif pInput == "2":
                            validInput = True
                            validSpell = False
                            #while the player has not chosen a valid spell
                            while not validSpell:
                                canCast = False
                                spell = ""
                                print("---------------")
                                print("Wich spell you want to use?")

                                #Print all the spells the PlayerCharacter has
                                for x in range(len(char.spells)):
                                    print(str(x + 1) + " - " + char.spells[x]) 

                                pInput = input("Input: ")

                                #Tries to check if the player can cast, if there's an exception, the player has chosen an invalid input
                                try:
                                    canCast = char.testSpells(char.spells[int(pInput)-1])
                                    validSpell = True
                                    spell = char.spells[int(pInput)-1]                                 
                                except:
                                    print("Invalid input")

                                #If canCast has returned True
                                if canCast:
                                    validTarget = False
                                    #While the player has not chosen a valid target
                                    while not validTarget:
                                        print("---------------")
                                        print("What's your target?")
                                        #If the spell is "Mend" change the targetIndexes list to get the indexes of characters with isPlayer == True
                                        if(spell == Fore.MAGENTA + "Mend" + Fore.RESET):
                                            targetIndexes = []
                                            for x in characters:
                                                if x.isPlayer:
                                                    targetIndexes.append(characters.index(x))

                                        #Print the list of targets
                                        for x in range(len(targetIndexes)):
                                            print(str(x+1) + " - " + characters[targetIndexes[x]].name )

                                        pInput = input("Input: ")
                                        #Try to cast to said target, if there's an exception, the player has chosen an invalid input
                                        try:
                                            char.castSpells(spell, characters[targetIndexes[int(pInput)-1]])
                                            validTarget = True
                                        except:
                                            print("Invalid input")
                                #If canCast returned False
                                elif validSpell and not canCast:
                                    #Turn valid input back to False so that the loop of choosing a action runs again
                                    validInput = False
                                    print("---------------")
                                    print("Not enough Mana!")
                        #Player has choosen an invalid input     
                        else:
                            print("Invalid input!")  
                #If the character isPlayer == False and there are still playerCharacters
                elif not char.isPlayer and playerChars > 0:
                    #List with the indexes of characters with isPlayer == True
                    targetIndexes = []
                    for x in characters:
                        if x.isPlayer:
                            targetIndexes.append(characters.index(x))

                    #Set the target to a random playerCharacter
                    target = dice(len(targetIndexes)) - 1
                    #Attack target
                    char.attack(characters[targetIndexes[target]])
            
                #Pop all characters who have 0 or less hp
                for char in characters:
                    if char.hp <= 0:
                        print("---------------")
                        print(char.name,"has died... press f")
                        characters.pop(characters.index(char))

                #Set playerChars and enemiesChars to 0
                playerChars = 0
                enemiesChars = 0
                #Count how many playerChars and enemiesChars there are in the characters list
                for x in characters:
                    if x.isPlayer:
                        playerChars += 1
                    else:
                        enemiesChars += 1
                
                #If there's less than 1 character with isPlayer == True
                if playerChars < 1:
                    #inGame turns to False to end the main game loop and set playerWin to false
                    inGame = False
                    playerWin = False
                #If there's less than 1 character with isPlayer == False
                elif enemiesChars < 1:
                    #Check if current wave is still less than the number of waves chosen
                    if currentWave < numOfWaves:
                        
                        #Increment currentWave
                        currentWave += 1
                        #Checks if there's still enough orcNames to the orcs needed
                        if len(orcNames) < numOfOrcs: 
                            #If not, open the OrcNames file, read all lines then close the file
                            f = open("OrcNames.txt")
                            orcNames = f.readlines()
                            f.close() 
                        
                        #Instantiate numOfOrcs orcs
                        for x in range(numOfOrcs):
                            orcName = orcNames[dice(len(orcNames))-1]
                            orc = Characters(Fore.RED + orcName.strip() + Fore.RESET, orcStats[0], orcStats[1], orcStats[2], orcStats[3], orcStats[4], False)
                            orcNames.pop(orcNames.index(orcName))
                            characters.append(orc)
                        enemiesChars = numOfOrcs
                    #currentWave was the last and all enemies have died
                    else:
                        #Set inGame to False to end the main game loop and set playerWIn to True
                        inGame = False
                        playerWin = True
        #If the player chose to not start a new round
        elif pInput == "N":
            validInput = False
            #While the player does not give a valid input
            while not validInput:
                print("What do you want to do?")
                print("1 - " + Fore.GREEN + "Inspect character" + Fore.RESET)
                print("2 - " + Fore.RED + "Exit" + Fore.RESET)
                print("Cancel - Go back")
                pInput = input("Input: ")
                
                #If "1" inspects all the characters alive
                if pInput == "1":
                    validInput = True
                    for char in characters:
                        char.inspectChar()
                #If "2" exits the game
                elif pInput == "2":
                    validInput = True
                    print("You ended the game...")
                    break
                #if "Cancel" cancels and goes back to "Do you want to start a new round"
                elif pInput == "Cancel":
                    validInput = True
                #The player did not give a valid input
                else:
                    print("Invalid Input")
        #The player did not give a valid input
        else:
            print("Invalid input")  

    #If the game ended print if the player won or not 
    if not inGame:
        if playerWin : print("PLAYER WINS!")
        else : print("Player lost...")