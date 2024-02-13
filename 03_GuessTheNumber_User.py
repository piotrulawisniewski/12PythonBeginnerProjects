#Guessing game- secret number is chosen by user and computer is trying to guess the number

import random



def computerGuess():


    print("\nWelcome to the computer guessing number!\n")
    x = int(input('Choose the maximum whole number of the range that computer is going to find your number: '))
    myNumber=int(input(f"choose whole number from 1 to {x} that computer will try to guess: "))

    compMin=1
    compMax=x
    compNumber=0
    shots=[] # list where computer trials will be contained


    while compNumber != myNumber:
        shots.append(compNumber)

        if compNumber<myNumber:
            compMin=compNumber+1
            compNumber=random.randint(compMin,compMax)
        else:
            compMax=compNumber-1
            compNumber = random.randint(compMin, compMax)

    shots.append(compNumber)
    noOfShots=len(shots)-1
    print(f'Congrats Comp! You have guessed my number ({myNumber})  in {noOfShots} tries!')
    print('Your tries were: ',shots[1:])


computerGuess()













