import random
import sys


ls = ["rock", "papper", "scissors"]
quit1 = ['q', 'exit', 'quit']
Ties = 0
Wins = 0
Losses = 0

print('-------------------------------------------')
print('Type "q", "exit" or "quit" to Quit game.')
print('-------------------------------------------')
while True:
    comp = random.choice(ls)
    while True:
        user = str(input("Choose and type: rock, papper or scissors: ")).lower()
        if user in quit1:
            print('Exit')
            sys.exit()
        elif user in ls:
            break
        else:
            print('Wrong input')

    if user == comp:
        print('Tie')
        Ties += 1
    elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'papper') or (user == 'papper' and comp == 'rock'):
        print(f'You won!!!!!! _________ You - {user} and Comp - {comp}')
        Wins += 1
    else:
        print(f'You lost!!!!! _________ You - {user} and Comp - {comp}')
        Losses += 1
    print(f'Stats: Ties: {Ties}, Wins: {Wins}, Losses: {Losses}')

# 1111
