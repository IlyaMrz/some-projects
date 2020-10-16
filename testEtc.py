import requests
from bs4 import BeautifulSoup

with open(r'C:\\Users\\pk111\\Desktop\\cache\\pl.txt', 'r') as f:
    pl = f.read().splitlines()

# print(pl)


def GetPlaylistsLinks(plLink):
    res = requests.get(plLink).text
    soup = BeautifulSoup(res, 'html.parser')
    i = soup.find_all(
        'a')
    print(i)
    for l in i:
        print(l.get('href'))


GetPlaylistsLinks(pl[0])
