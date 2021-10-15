# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard

# youtub's format_ID:
# https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f#dash-video
# or check formats with command:
# yt-dlp -F YT_URL
# 299 1080 - 60fps
# 136 1080 - 30fps

VLC_PATH="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

def get_Data_with_format(format_ID):
    return YoutubeDL({
        'format': format_ID,
        })

ydl_a = get_Data_with_format('251')


try:
    ydl_v = get_Data_with_format('136')
    # print('Youtube_to_VLC'.center(70, '_'))
    # URL = input('Enter youtube url :  ')
    win32clipboard.OpenClipboard()
    URL = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    audio_url = ydl_a.extract_info(URL, download=False)['url']
    video_url = ydl_v.extract_info(URL, download=False)['url']

except:
    ydl_v = get_Data_with_format('299')
    video_url = ydl_v.extract_info(URL, download=False)['url']
finally:
    command=f'{VLC_PATH} {video_url} --input-slave={audio_url}'
    subprocess.call(command)