#Guessing game- secret number is contained by computer and user has to guess the number

import random
import sys

print("Welcome to the guessing number!")
print("Try to guess the whole number that your computer think about :)")

def guessNumber(x):
    compNumber=random.randint(1,x)

    myNumber=int(input(f"guess the number between 1 and {x}: "))
    userNumbers=[] # list where user numbers will be contained
    userNumbers.append(myNumber)

    if myNumber==compNumber:
        print('Congrats! You have guessed the numer at first try! Nice shot!')
    else:
        while myNumber != compNumber:
            userNumbers.append(myNumber)
            if myNumber<compNumber:
                myNumber=int(input(f'Your number {myNumber} is smaller than secret one. Try again: '))
            else:
                myNumber = int(input(f'Your number {myNumber} is bigger than secret one. Try again: '))
        guessNumber=len(userNumbers)
        print(f'Congrats! You have guessed the numer at {guessNumber} try!')


guessNumber(15)










