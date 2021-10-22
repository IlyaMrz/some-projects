# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
COOKIE_PATH = ''  # txt

win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

if not "youtube.com/watch" in URL:
    print('Youtube_to_VLC'.center(70, '_'))
    URL = input('Enter youtube url :  ')


def direct_link(format_ID):
    yt_data = YoutubeDL({'format': format_ID})
    link = yt_data.extract_info(URL, download=False)['url']
    return link


try:
    link = direct_link('22')
except:
    link = direct_link('best[height<=720]')


# mark as watched
#command_mark_watched = f'yt-dlp --skip-download --cookies {COOKIE_PATH} --mark-watched {URL}'
# subprocess.call(command_mark_watched)

command = f'{VLC_PATH} {link}'
subprocess.call(command)
