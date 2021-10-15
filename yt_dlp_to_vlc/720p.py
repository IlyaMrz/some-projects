from __future__ import unicode_literals
# from pprint import pprint
import subprocess
from yt_dlp import YoutubeDL
ydl = YoutubeDL({
    'format': '22',
})
print('Youtube Downloader'.center(40, '_'))
URL = input('Enter youtube url :  ')
r = ydl.extract_info(URL, download=False)

link = (r['url'])
# pprint(link)
command=f'"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" "{link}"'
# print(command)
subprocess.call(command)
