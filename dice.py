import random

#Generates random number between 1 and max value, including both ends
def dice(maxvalue:int):
    rnd = random.randint(1,maxvalue)
    return rnd