"""Rock, Paper, scissors(Always Win version)
By Al Sweigart al@inventwithpython.com
The Classic hand game of luck exept you always win.
View this code at https://nostarch.com/big-book-small-python-projets
Tags: tiny, game, humor"""

import time, sys

print('''Rock Paper Scissors, By Al  al@inventwithpython.com
-Rock beats scissors. 
-Paper beats rock. 
-Scissors beats paper.
''')

# These variables keep trackof the number of wins
wins = 0

while True: # main game loop
    while True: # keep asking player R, P, S, or Q,
        print('{} wins, 0 losses, 0 ties'.format(wins))
        print('Enter your move: (R)ock,(P)aper, (S)cissors or(Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing with me. See you soon! :D')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q')

    # Display what the player chose:
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('Ughhh! You win... this time at least.')
    wins = wins + 1 # Could also write 'wins += 1'