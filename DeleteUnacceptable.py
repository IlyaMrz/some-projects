import re

rawSongs = open(
    'C:\\Games\\VScodeProjects\\some-projects\\rawSongs.txt').read()
# x = list(input('enter songs'))
writeSongs = open(
    'C:\\Games\\VScodeProjects\\some-projects\\tracks.txt', 'w')

# s = rawSongs
# s = re.sub(r"\d+:\d+", "", s)

rawSongs = rawSongs.replace('[', '').replace(']', '')
print(rawSongs)
writeSongs.write(rawSongs)


# unacceptables = ['[', ']', '*', '(', ')']
# for i in rawSongs:
#     if i not in unacceptables:
#         writeSongs.write(i)


writeSongs.close()
