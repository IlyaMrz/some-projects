from bs4 import BeautifulSoup as bs
# for personal usage to grab Playlist inks and video Links from whole youtube channel

# get links for each playlist video ---- uncomment to use
# with open('C:\\Users\\pk111\\Desktop\\cache\\bodyhtml.txt', 'rb') as f:
#     text = f.read()

# soup = bs(text, 'html.parser')
# for i in soup.select('a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer:nth-child(1)'):
#     link = i['href']
#     tlink = link.partition('&')[0]
#     print(f'https://www.youtube.com{tlink}')


# get all links for each video from whole channel ---- uncomment to use
with open('C:\\Users\\pk111\\Desktop\\cache\\bodyhtml.txt', 'rb') as f:
    text = f.read()
soup = bs(text, 'html.parser')
for i in soup.find_all("a", {"id": "video-title", "class": "yt-simple-endpoint style-scope ytd-grid-video-renderer"}):
    link = i['href']
    tlink = link.partition('&')[0]
    print(f'https://www.youtube.com{tlink}')
