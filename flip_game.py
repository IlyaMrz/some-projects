import random
import sys
from pprint import pprint
sys.setrecursionlimit(10**6)

# https://www.youtube.com/watch?v=f1vXAHGIpfc

money = 100
players_count = 1000
flips_per_player = 700


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

print(positive_count, ' players with positive cashflow')
