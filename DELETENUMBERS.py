import re
x = open(
    'C:\\Games\\VScodeProjects\\some-projects\\rawSongs.txt').read()

# x = input('Enter text: ')

z = []

for item in x:
    if item != ':' and not item.isdigit():
        z += item

for i in z:
    print(i, end='')
