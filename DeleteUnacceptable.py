
rawSongs = open(
    'C:\\Games\\VScodeProjects\\album-splitter-master\\rawSongs.txt').read()
# x = list(input('enter songs'))

unacceptables = ['[', ']', '*']
writeSongs = open(
    'C:\\Games\\VScodeProjects\\album-splitter-master\\tracks.txt', 'w')

for i in rawSongs:
    if i not in unacceptables:
        # print(i, end='')
        writeSongs.write(i)

writeSongs.close()
