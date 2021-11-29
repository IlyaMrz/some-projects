# some stuff testing wtch зай
# count letters in this
import pprint

firstM_in_P = ["Zay1ianN8hA6VVncaafKBxipvT"]
print('for future testing')
print("""
old
ca9aba84
6ac9681a
aa66d380
11e91334
97ea18ef
98e5ac02
2d01c775
0955e188
09b78337
d15fe8ad
a0eb5ab7
1585caa4 -  u
4723781b
83dc9c12 - u
4123b9f2 -  u
2685f9af -  u

nEw 27-11-2021:
9daec0e3
ae182554
7715dbd9
4a2bcb2f
213bff94
ea80c4b1
b2e6ffd7
0eacbe0e
81612691
0e18393a
e057a14c
90dc6cc3
07428c40
cf0126ca
0ac81faa
2d6229ac""")


secondClmnz = ["Zay1!gwHh:S6KArF4Mb"]
print("HEROSDpV39RC_J9JeBYn8A")

print("obfusc")

count1 = {}
count2 = {}

for ch in firstM_in_P[0].lower():
    count1.setdefault(ch, 0)
    count1[ch] = count1[ch] + 1
for ch in secondClmnz[0].lower():
    count2.setdefault(ch, 0)
    count2[ch] = count2[ch] + 1

pprint.pprint(count1)
pprint.pprint(count2)
