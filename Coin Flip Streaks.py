import random

# changeable variables
exprange = 10000
flipsides = ['T', 'H']
streak = 6

# do not change below
count = 1
numberofstreaks = 0

a = flipsides[random.randint(0, 1)]

for i in range(exprange - 1):
    b = flipsides[random.randint(0, 1)]
    if b == a:
        count += 1
        if count == streak:
            numberofstreaks += 1
    else:
        count = 1
    a = b

chance = numberofstreaks / (exprange/streak)

# output
print('number of streaks: ', + numberofstreaks)
print(f'Chance of streak: {numberofstreaks/100:.2f}%')
