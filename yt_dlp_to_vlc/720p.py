# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL


VLC_PATH="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

ydl = YoutubeDL({
    'format': '22',
})

print('Youtube_to_VLC'.center(70, '_'))
URL = input('Enter youtube url :  ')

r = ydl.extract_info(URL, download=False)

link = (r['url'])
command=f'{VLC_PATH} "{link}"'
subprocess.call(command)
