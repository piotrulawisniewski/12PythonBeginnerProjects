import random
from Hangman_words import words

print('Welcome to hangman game!')

# random choose of noun from list:
wordToGuess= random.choice(words)


# dividing word for letters and assemble it to to the
lettersToGuess = [letter for letter in wordToGuess]

wordLength = len(wordToGuess)
noOfLives = int(wordLength)

print(wordToGuess)
print(lettersToGuess)

shownWord='_'*wordLength
print(shownWord)


currentLetters=[lett for lett in shownWord]
# container for letters that have been used by user:
usedLetters = []

n=0
i=0

while True:
    guessedLetter=input('\nGuess the letter: ')
    usedLetters.append(guessedLetter)
    for i in range(0,len(lettersToGuess)):
        if lettersToGuess[i] in usedLetters:
            currentLetters[i]=lettersToGuess[i]
        else:
            currentLetters[i] = '_'
        i+=1
    print(currentLetters)






















#
# # container for letters that have been used by user:
# usedLetters = []
#
# shownWord = ''


#
# while n<noOfLives:
#     guessedLetter=input('\nGuess the letter: ')
#     usedLetters.append(guessedLetter)
#     for i in wordToGuess:
#         if i in usedLetters:
#             shownWord=shownWord+i
#         else:
#             shownWord=shownWord+'-'
#             n+=1
#     print(shownWord)
















# print('Guess the word:\n')
#
# for i in hiddenLetters:
#     shownWord=shownWord+('_')
# print(shownWord)
#
# guessLetter=input('\nGuess the letter: ')
# usedLetters.append(guessLetter)
#
# for i in hiddenLetters:
#     if i in usedLetters:
