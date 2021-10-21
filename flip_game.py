import random
import sys
from pprint import pprint
import functools
sys.setrecursionlimit(10**6)

# https://www.youtube.com/watch?v=f1vXAHGIpfc

money = 100
players_count = 1000
flips_per_player = 500

collective_money_onStart = money*players_count


def flip(m, round):
    r = random.randint(0, 1)
    if r == 1:
        m = m+(m*0.5)
    elif r == 0:
        m = m-(m*0.4)
    if round == 0:
        return m
    round = round-1
    return flip(m, round)


array = []

while players_count > 0:
    array.append(flip(money, flips_per_player))
    players_count = players_count-1

array.sort()
pprint(array)

positive_count = 0
for k in array:
    if k > money:
        positive_count = positive_count+1

collective_money_onEnd = functools.reduce(lambda a, b: a+b, array)

print(positive_count, ' players with positive cashflow')
print('collective money on Start: ', collective_money_onStart)
print('collective money in z End: ', collective_money_onEnd)
