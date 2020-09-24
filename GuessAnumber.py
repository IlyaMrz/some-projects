from sys import argv
from random import randrange


print('==================== START ====================')

try:
    first = int(argv[1])
    second = int(argv[2])
except:
    print('No arguments were given or you gave wrong ones. Default\'s values setted.')
    first = 1
    second = 3

# try:
secret = randrange(first, second)
# except ValueError:
#     print('Give 2 arguments. 2 numbers. First should be lesser than second')


def guess(first, second):
    while True:
        try:
            guessed = int(
                input(f'Choose a number between {first} and {second-1}: '))
            if secret == guessed:
                print('________________________________________________________')
                print(
                    f'Congratulations! You guessed right! A secret number is {secret}')
                print('_________________________ DONE _________________________')
                break
            elif first > guessed or guessed > second-1:
                print(f"Hey, choose between {first} and {second-1}")
            else:
                print('Wrong! Try more!')
        except ValueError:
            print('You entered not a number')


guess(first, second)
