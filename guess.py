import random


x = random.randint(1, 10)
while True:
    z = int(input('Guess a number from 1 to 10: '))
    if z == x:
        print(f'You won! {z} is a secret number.')
        break
    else:
        print('Wrong, try more..')
