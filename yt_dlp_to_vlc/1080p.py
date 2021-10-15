# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL

ydl_a = YoutubeDL({
    'format': '251',
})
ydl_v = YoutubeDL({
    'format': '248',
})
print('Youtube_to_VLC'.center(70, '_'))
URL = input('Enter youtube url :  ')
audio = ydl_a.extract_info(URL, download=False)['url']
video = ydl_v.extract_info(URL, download=False)['url']

command=f'"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" {video} --input-slave={audio}'
subprocess.call(command)


