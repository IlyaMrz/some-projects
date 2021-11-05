# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard
import os

# youtub's format_ID:
# https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f#dash-video
# or check formats with command:
# yt-dlp -F YT_URL
# if u wanna use certain format use clipboard => URL,ID

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
COOKIE_PATH = ''  # txt
PATH_720p = '720p.py'
SUB_PATH = ''  # to enable subtitles add '/s' to end of yt url

TWITCH_FORMATS = ['1080p__source_', '1080p', '1080p50']
VIDEO_FORMATS = ['299', '137', '248', '303',
                 '335', '399', '699']  # 1080 youtube


def direct_link(format_ID):
    yt_data = YoutubeDL({'format': format_ID})
    link = yt_data.extract_info(URL, download=False)['url']
    return link


win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

if (not "youtu" in URL) and (not "twitch" in URL):
    print('Youtube_to_VLC'.center(70, '_'))
    URL = input('Enter youtube url :  ')

format_index = 0

if (',' in URL) and ("youtu" in URL):
    URL, frmt = URL.split(',')
    format_index = VIDEO_FORMATS.index(str(frmt))


if "twitch" in URL:
    for f in TWITCH_FORMATS:
        try:
            print(f'tryin {f}')
            video_url = direct_link(f)
            command = f'{VLC_PATH} {video_url}'
            subprocess.call(command)
            break
        except:
            continue
    exit()


audio_url = direct_link('bestaudio')

if URL[-2:] == '/s':
    SUB_PATH = 'sub.en.vtt'
    command_downl_subtitles = f'yt-dlp --sub-lang en --write-sub --sub-format vtt --skip-download -o "sub.%(ext)s" {URL}'
    subprocess.call(command_downl_subtitles)
    if not os.path.isfile(SUB_PATH):
        command_downl_subtitles = f'yt-dlp --sub-lang en --write-auto-sub --sub-format vtt --skip-download -o "sub.%(ext)s" {URL}'
        subprocess.call(command_downl_subtitles)
    if not os.path.isfile(SUB_PATH):
        SUB_PATH = ''


def getVideoUrl(format_index):
    if format_index == 7:
        try:
            print("1080p not available, going for 720p or lower...")
            subprocess.call(f'python {PATH_720p}')
            exit()
        except:
            exit()
    try:
        video_url = direct_link(VIDEO_FORMATS[format_index])
        return video_url
    except:
        format_index = format_index+1
        return getVideoUrl(format_index)

# mark as watched
#command_mark_watched = f'yt-dlp --skip-download --cookies {COOKIE_PATH} --mark-watched {URL}'
# subprocess.call(command_mark_watched)


video_url = getVideoUrl(format_index)
command = f'{VLC_PATH} {video_url} --input-slave={audio_url} --sub-file={SUB_PATH}'
subprocess.call(command)

if SUB_PATH:
    os.remove(SUB_PATH)
