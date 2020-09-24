import re
x = open(
    'C:\\Games\\VScodeProjects\\some-projects\\file2.txt').read()

# x = input('Enter text: ')

z = []

for item in x:
    if item != ':' and not item.isdigit():
        if item != '.':
            z += item

for i in z:
    print(i, end='')
