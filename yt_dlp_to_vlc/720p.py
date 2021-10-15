# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard

VLC_PATH="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

ydl = YoutubeDL({
    'format': '22',
})

# print('Youtube_to_VLC'.center(70, '_'))
# URL = input('Enter youtube url :  ')
win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

r = ydl.extract_info(URL, download=False)

link = (r['url'])
command=f'{VLC_PATH} "{link}"'
subprocess.call(command)
