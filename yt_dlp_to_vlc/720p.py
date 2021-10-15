from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
ydl = YoutubeDL({
    'format': '22',
})
print('Youtube Downloader'.center(40, '_'))
URL = input('Enter youtube url :  ')
r = ydl.extract_info(URL, download=False)

link = (r['url'])
command=f'"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" "{link}"'
subprocess.call(command)
