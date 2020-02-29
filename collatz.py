import sys


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
            print(number)
        else:
            number = number * 3 + 1
            print(number)
    return(number)


while True:
    try:
        number = abs(int(input('Enter your number: ')))
        collatz(number)
    except ValueError:
        print('Not integer')
