import random
from Hangman_words import words

print('Welcome to hangman game!')

# random choose of noun from list:
wordToGuess= random.choice(words)
wordToGuess=wordToGuess.lower()

# dividing word for letters and assemble it to to the
lettersToGuess = [letter for letter in wordToGuess]

wordLength = len(wordToGuess)
noOfLives = int(wordLength)

print(wordToGuess)
print(lettersToGuess)
print('Number of lives: ' , noOfLives)

# hiding the letters (user knows only the number of letters):
shownWord='_'*wordLength
print(shownWord)

# list for current situation- to shown letter if that has been guessed and underscore if not:
currentLetters=[lett for lett in shownWord]

# list for letters that have been used by user:
usedLetters = []

i = 0
while noOfLives > 0:
    guessedLetter=input('\nGuess the letter: ')
    guessedLetter=guessedLetter.lower().strip()
    if guessedLetter in usedLetters:
        while guessedLetter in usedLetters:
            guessedLetter=input('\nYou have tried this letter. Try other one:  ')
            guessedLetter = guessedLetter.lower().strip()

    usedLetters.append(guessedLetter)
    usedLetters.sort()

    # checking if chosen letter in seeking word:
    if guessedLetter in lettersToGuess:
        for i in range(0,len(lettersToGuess)):
            if lettersToGuess[i] in usedLetters:
                currentLetters[i]=lettersToGuess[i]
            i+=1
    else:
        noOfLives = noOfLives - 1

    # checking if word is guessed:
    word=''
    for singleLetter in currentLetters:
        word+=singleLetter

    if word == wordToGuess:
        print('Letters that have been used:', usedLetters)
        print('You have won! The word was:\n',word.upper())
        break
    else:
        print('Letters that have been used:', usedLetters,'\n')
        print('Word to guess:', currentLetters)
        print(noOfLives, ' lives remains')
else:
    print('\nGame Over!\nPlay again.')























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
