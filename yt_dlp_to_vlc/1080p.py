# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard
from pprint import pprint

# youtub's format_ID:
# https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f#dash-video
# or check formats with command:
# yt-dlp -F YT_URL
# 299 1080 - 60fps
# 137 1080 - 30fps
# if u wanna use certain format use clipboard => URL,ID

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"


def setPropsToYT_dl(format_ID):
    return YoutubeDL({
        'format': format_ID,
        "player_client": "android",
    })


ydl_a = setPropsToYT_dl('251')

video_formats = ['137', '248', '299', '303', '335', '399', '699']  # 1080

win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

idx = 0
if len(URL.split(',')) == 2:
    URL, idxx = URL.split(',')
    idx = video_formats.index(str(idxx))

audio_url = ydl_a.extract_info(URL, download=False)['url']


def go(idx):
    try:
        ydl_v = setPropsToYT_dl(video_formats[idx])
        video_url = ydl_v.extract_info(URL, download=False)['url']
        return video_url
    except:
        idx = idx+1
        return go(idx)


video_url = go(idx)
command = f'{VLC_PATH} {video_url} --input-slave={audio_url}'
subprocess.call(command)
