import re

rawSongs = open(
    'C:\\Games\\VScodeProjects\\some-projects\\rawSongs.txt').read()
# x = list(input('enter songs'))


# s = rawSongs
# s = re.sub(r"\d+:\d+", "", s)


writeSongs = open(
    'C:\\Games\\VScodeProjects\\some-projects\\tracks.txt', 'w')

unacceptables = ['[', ']', '*', '(', ')']
for i in rawSongs:
    if i not in unacceptables:
        # print(i, end='')
        writeSongs.write(i)
# writeSongs.write(s)

writeSongs.close()
