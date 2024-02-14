# rock-paper-scissors game with computer

import random

def rpc_game():
    print("Welcome in the rock-paper-scissors game!\n")
    # parameters for the game:
    user = input("What's your select? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])


    if user == computer:
        return print('It\'s a draw!')

    is_win(user, computer):
        return print('You\'ve won!')

    return print('Computer wins!')

def is_win(player, opponent):
    # r>s, p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True

rpc_game()
